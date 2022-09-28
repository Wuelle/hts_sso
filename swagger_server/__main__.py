#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_session import Session


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'HackThisSite Single Sign-On API'}, pythonic_params=True)

    app.app.config["SESSION_TYPE"] = 'filesystem'
    app.app.config["SECRET_KEY"] = b"changeme"
    app.app.config["SESSION_COOKIE_NAME"] = 'LoginSession'
    app.app.config["PERMANENT_SESSION_LIFETIME"] = 300  # 5min
    Session(app.app)

    app.run(port=8080)


if __name__ == '__main__':
    main()
