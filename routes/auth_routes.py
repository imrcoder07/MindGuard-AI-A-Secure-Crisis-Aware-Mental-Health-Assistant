from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, login_required
from models.db_models import User
from extensions import db
import re

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth")
def auth_page():
    return render_template("auth.html")


# -------------------------
# REGISTER
# -------------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    # Basic validations
    if not username or len(username) < 3:
        return jsonify({"success": False, "error": "Username must be at least 3 characters."}), 400

    email_regex = r"^[^@]+@[^@]+\.[^@]+$"
    if not re.match(email_regex, email):
        return jsonify({"success": False, "error": "Invalid email format."}), 400

    if len(password) < 8:
        return jsonify({"success": False, "error": "Password must be at least 8 characters long."}), 400

    # Check duplicates
    if User.query.filter_by(username=username).first():
        return jsonify({"success": False, "error": "Username already exists."}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"success": False, "error": "Email already registered."}), 400

    # Create user
    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    login_user(user, remember=False)

    return jsonify({"success": True}), 201


# -------------------------
# LOGIN
# -------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({"success": False, "error": "Missing credentials."}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"success": False, "error": "Invalid credentials."}), 401

    login_user(user, remember=False)

    return jsonify({"success": True}), 200


# -------------------------
# LOGOUT
# -------------------------
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.auth_page"))