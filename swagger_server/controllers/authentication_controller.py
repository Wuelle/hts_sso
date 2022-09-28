import connexion
import six

from swagger_server.models.captcha_prompt import CaptchaPrompt  # noqa: E501
from swagger_server.models.login_body import LoginBody  # noqa: E501
from swagger_server.models.next_frame import NextFrame  # noqa: E501
from swagger_server.models.successful_authentication import SuccessfulAuthentication  # noqa: E501
from swagger_server import util

from base64 import b64decode

from flask import send_file, session, Response

class Account:
    def __init__(self, password, mfa=None, mfa_first=False):
        self.password = password
        self.mfa = mfa
        self.mfa_enabled = mfa is not None
        self.mfa_first = mfa_first

ACCOUNTS = {
    "Alaska": Account(password="beepboop"),
    "Kage": Account(password="boopbeep", mfa="123", mfa_first=True)
}

def session_is_complete(s):
    return s["username"] is not None and s["password"] is not None and s["mfa"] is not None

def next_expected_frame(s):
    """
    Return the next frame that should be submitted by the user or None if authentication is complete
    """
    if s["username"] is None:
        return "username"
    else:
        account = ACCOUNTS[s["username"]]
        if account.mfa_enabled and account.mfa_first and s["mfa"] is None:
            return "mfa"
        if s["password"] is None:
            return "password"
        else:
            return None


def login_start_reauth(redirect, username):  # noqa: E501
    """Reauthenticate a user in case their session expired, without needing to enter the username again

    Returns a html page guiding the user through the login process. The login is for a specific account, meaning the user does not have the option to enter a username and is instead directly shown the password screen # noqa: E501

    :param redirect: The AES-encrypted redirection url. If this is not a valid url belonging to hackthissite.org, the server must respond with a 403 Not Allowed.
    :type redirect: str
    :param username: The account name that should be reauthenticated
    :type username: str

    :rtype: None
    """
    try:
        domain = b64decode(redirect).decode("ascii")
    except UnicodeDecodeError:
        return "bad redirect domain", 400

    if domain.startswith("HTS"):
        # start a new login session
        session["password"] = None
        session["mfa"] = None
        session["redirect"] = domain[3:].strip()

        if username in ACCOUNTS.keys():
            session["username"] = username
            return send_file("static/index.html")  # TODO: start with pw/mfa frame here
        else:  # unknown username, fallback to regular login
            session["username"] = None
            return send_file("static/index.html")
    else:
        return "Unauthorized redirect domain", 403


def login_start_session(redirect):  # noqa: E501
    """Start logging in

    Returns a html page guiding the user through the login process. The first frame shown will prompt the user to enter their username, the order (and number) of subsequent frames is determined by the server. Also returns a session cookie that is used to keep track of login progress on the server # noqa: E501

    :param redirect: The AES-encrypted redirection url. If this is not a valid url belonging to hackthissite.org, the server must respond with a 403 Not Allowed.
    :type redirect: str

    :rtype: None
    """
    # make sure not to accidentally build some kind of oracle here... ^^
    try:
        domain = b64decode(redirect).decode("ascii")
    except UnicodeDecodeError:
        return "bad redirect domain", 400

    if domain.startswith("HTS"):
        # start a new login session
        session["username"] = None
        session["password"] = None
        session["mfa"] = None
        session["redirect"] = domain[3:].strip()

        return send_file("static/index.html")
    else:
        return "Unauthorized redirect domain", 403


def login_submit_frame(body, login_session=None):  # noqa: E501
    """Submit one of multiple credential frames

    This API allows the user to login to their hackthissite.org account. Authentication is done in three steps: Username, Password and MFA (if enabled). The order in which the user must enter these is unspecified (the client is told after submitting the previous value). After each step, the user may be required to complete a CAPTCHA. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param login_session: 
    :type login_session: str

    :rtype: NextFrame
    """
    if connexion.request.is_json:
        body = LoginBody.from_dict(connexion.request.get_json())  # noqa: E501

    if body.frame != next_expected_frame(session):
        return "unexpected frame", 409

    if body.frame == "username":
        username = body.value
        if username in ACCOUNTS.keys():
            session["username"] = username
            if username == "Alaska":  # Alaska is suspicious, let's make them complete a captcha
                return NextFrame(next_expected_frame(session), show_captcha=True), 200           
        else:
            return "user not found", 403

    elif body.frame == "password":
        password = body.value

        if ACCOUNTS[session["username"]].password == password:
            session["password"] = password
        else:
            return "wrong password", 403

    elif body.frame == "mfa":
        mfa = body._value

        if ACCOUNTS[session["username"]].mfa == mfa:
            session["mfa"] = mfa
        else:
            return "wrong mfa code", 403

    if (next_expected_frame(session) is None):
        return SuccessfulAuthentication(session["redirect"], "theauthtoken"), 201
    else:
        return NextFrame(next_expected_frame(session), show_captcha=False), 200
