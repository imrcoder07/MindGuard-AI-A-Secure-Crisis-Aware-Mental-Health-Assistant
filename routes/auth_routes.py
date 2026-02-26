from flask import Blueprint, render_template, request, jsonify, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from models.db_models import User
from extensions import db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth")
def auth_page():
    return render_template("auth.html")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"success": False, "error": "Username already exists."})

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    login_user(user)

    return jsonify({"success": True})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        login_user(user)
        return jsonify({"success": True})

    return jsonify({"success": False, "error": "Invalid credentials."})


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.auth_page"))