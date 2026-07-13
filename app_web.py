from flask import Flask
from core.config import Config
from routes.auth import auth_bp
from routes.cv import cv_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth_bp)
app.register_blueprint(cv_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)