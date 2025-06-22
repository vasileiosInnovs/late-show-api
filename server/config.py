from flask import Flask, app
from flask_jwt_extended import JWTManager

app = Flask(__name__)

jwt = JWTManager(app)