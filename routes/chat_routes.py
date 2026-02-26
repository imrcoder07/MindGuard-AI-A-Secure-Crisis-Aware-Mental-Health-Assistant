from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.crisis_engine import analyze_risk
from services.llama_service import generate_response
from services.memory_manager import (
    create_conversation,
    save_message,
    get_recent_messages
)
from utils.fallback_handler import crisis_response, technical_fallback
from models.db_models import Conversation

chat_bp = Blueprint("chat", __name__)

MAX_MESSAGE_LENGTH = 1000
MAX_HISTORY_MESSAGES = 12


# -------------------------------------------------------
# MAIN CHAT ROUTE (Fully Secured)
# -------------------------------------------------------

@chat_bp.route("/chat", methods=["POST"])
@login_required
def chat():
    try:
        data = request.get_json(silent=True)
        if not data or "message" not in data:
            return jsonify({"status": "error", "message": "'message' field required."}), 400

        user_message = str(data.get("message", "")).strip()
        conversation_id = data.get("conversation_id")

        if not user_message:
            return jsonify({"status": "error", "message": "Message cannot be empty."}), 400

        if len(user_message) > MAX_MESSAGE_LENGTH:
            return jsonify({"status": "error", "message": "Message too long."}), 400

        # ----------------------------------------------------
        # Ownership Validation / Creation
        # ----------------------------------------------------

        if conversation_id:
            conversation = Conversation.query.filter_by(
                id=conversation_id,
                user_id=current_user.id
            ).first()

            if not conversation:
                return jsonify({"status": "error", "message": "Unauthorized"}), 403
        else:
            conversation_id = create_conversation(current_user.id)

        # ----------------------------------------------------
        # Risk Analysis
        # ----------------------------------------------------

        risk_result = analyze_risk(user_message)
        risk_score = risk_result.get("risk_score", 0)
        risk_level = risk_result.get("risk_level", "low")

        # Immediate crisis override
        if risk_level == "high":
            save_message(conversation_id, "user", user_message, current_user.id, risk_score=risk_score)

            crisis_msg = crisis_response()

            save_message(
                conversation_id,
                "assistant",
                crisis_msg["response"],
                current_user.id,
                emotion="critical",
                risk_score=risk_score
            )

            return jsonify({
                "status": "success",
                "response": crisis_msg["response"],
                "conversation_id": conversation_id
            })

        # Save user message
        save_message(
            conversation_id,
            "user",
            user_message,
            current_user.id,
            risk_score=risk_score
        )

        # ----------------------------------------------------
        # Get Conversation History (Validated)
        # ----------------------------------------------------

        history = get_recent_messages(
            conversation_id,
            current_user.id,
            limit=MAX_HISTORY_MESSAGES
        )

        structured_history = [
            {"role": msg["sender"], "content": msg["content"]}
            for msg in history
        ]

        # ----------------------------------------------------
        # Call LLM
        # ----------------------------------------------------

        result = generate_response(structured_history)

        assistant_text = result.get("response", "")
        emotion = result.get("emotion", "neutral")

        save_message(
            conversation_id,
            "assistant",
            assistant_text,
            current_user.id,
            emotion=emotion
        )

        return jsonify({
            "status": "success",
            "response": assistant_text,
            "conversation_id": conversation_id
        })

    except Exception as e:
        print("Chat error:", e)
        return jsonify(technical_fallback()), 500


# -------------------------------------------------------
# LIST CONVERSATIONS (User Filtered)
# -------------------------------------------------------

@chat_bp.route("/conversations", methods=["GET"])
@login_required
def get_conversations():

    conversations = (
        Conversation.query
        .filter_by(user_id=current_user.id)
        .order_by(Conversation.updated_at.desc())
        .all()
    )

    result = []

    for c in conversations:
        first_msg = get_recent_messages(c.id, current_user.id, limit=1)
        preview = first_msg[0]["content"][:40] if first_msg else "New Conversation"

        result.append({
            "id": c.id,
            "preview": preview,
            "created_at": c.created_at.strftime("%Y-%m-%d %H:%M")
        })

    return jsonify({"conversations": result})


# -------------------------------------------------------
# GET CONVERSATION MESSAGES
# -------------------------------------------------------

@chat_bp.route("/conversations/<int:conversation_id>", methods=["GET"])
@login_required
def get_messages(conversation_id):

    conversation = Conversation.query.filter_by(
        id=conversation_id,
        user_id=current_user.id
    ).first()

    if not conversation:
        return jsonify({"status": "error", "message": "Access denied"}), 403

    messages = get_recent_messages(conversation_id, current_user.id, limit=50)

    return jsonify({
        "conversation_id": conversation_id,
        "messages": messages
    })