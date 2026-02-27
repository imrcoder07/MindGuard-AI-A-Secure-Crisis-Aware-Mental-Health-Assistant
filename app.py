from flask import Flask, render_template, redirect, url_for
from extensions import db
from config import Config
from routes.chat_routes import chat_bp
from flask_login import LoginManager, current_user
from models.db_models import User  # You must create this model


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # ---------------------------
    # LOGIN MANAGER
    # ---------------------------
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ---------------------------
    # BLUEPRINTS
    # ---------------------------
    app.register_blueprint(chat_bp)

    # you must create this blueprint file
    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    # ---------------------------
    # CREATE TABLES
    # ---------------------------
    with app.app_context():
        db.create_all()

    # ---------------------------
    # ROUTES
    # ---------------------------
    @app.route("/")
    def index():
        if not current_user.is_authenticated:
            return redirect(url_for("auth.auth_page"))
        return render_template("index.html")

    @app.route("/health")
    def health():
        return {"status": "Backend running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run()