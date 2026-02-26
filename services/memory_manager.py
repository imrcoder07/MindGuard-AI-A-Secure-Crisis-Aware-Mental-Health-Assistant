from models.db_models import Message, Conversation
from extensions import db
from datetime import datetime


# ----------------------------------------------------
# Create Conversation (User Is Required)
# ----------------------------------------------------

def create_conversation(user_id):
    if not user_id:
        raise ValueError("User must be authenticated to create a sanctuary session.")

    conversation = Conversation(user_id=user_id)
    db.session.add(conversation)
    db.session.commit()
    return conversation.id


# ----------------------------------------------------
# Get Conversation (Ownership Validation)
# ----------------------------------------------------

def get_conversation(conversation_id, user_id):
    conversation = Conversation.query.filter_by(
        id=conversation_id,
        user_id=user_id
    ).first()

    if not conversation:
        raise PermissionError("Unauthorized access to conversation.")

    return conversation


# ----------------------------------------------------
# Save Message (Validated)
# ----------------------------------------------------

def save_message(conversation_id, sender, content, user_id, emotion=None, risk_score=0):
    if sender not in {"user", "assistant"}:
        raise ValueError("Invalid sender type")

    conversation = get_conversation(conversation_id, user_id)

    message = Message(
        conversation_id=conversation.id,
        sender=sender,
        content=content,
        emotion=emotion,
        risk_score=risk_score
    )

    db.session.add(message)

    # Update timestamp for resurfacing
    conversation.updated_at = datetime.utcnow()

    db.session.commit()
    return message.id


# ----------------------------------------------------
# Get Recent Messages (Validated + Chronological)
# ----------------------------------------------------

def get_recent_messages(conversation_id, user_id, limit=12):

    conversation = get_conversation(conversation_id, user_id)

    messages = (
        Message.query
        .filter_by(conversation_id=conversation.id)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )

    messages.reverse()

    return [
        {
            "id": m.id,
            "sender": m.sender,
            "content": m.content,
            "emotion": m.emotion,
            "risk_score": m.risk_score,
            "created_at": m.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        for m in messages
    ]