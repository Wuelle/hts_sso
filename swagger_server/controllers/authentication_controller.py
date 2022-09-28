import connexion
import six

from swagger_server.models.captcha_prompt import CaptchaPrompt  # noqa: E501
from swagger_server.models.init_login_session import InitLoginSession  # noqa: E501
from swagger_server.models.next_frame import NextFrame  # noqa: E501
from swagger_server.models.submitted_frame import SubmittedFrame  # noqa: E501
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

def next_expected_frame(s):
    """
    Return the next frame that should be submitted by the user or None if authentication is complete
    """
    if s.get("username", None) is None:
        return "username"
    else:
        account = ACCOUNTS[s["username"]]
        if account.mfa_enabled and account.mfa_first and s["mfa"] is None:
            return "mfa"
        if s["password"] is None:
            return "password"
        else:
            return None

def login_start_session(body):  # noqa: E501
    """Start logging in

    Validates the users redirect url and, if it is valid, starts a login session on the server. If a username is provided, the client will not have to fill out the username frame while logging in (re-authentication) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NextFrame
    """
    if connexion.request.is_json:
        body = InitLoginSession.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        domain = b64decode(body.redirect).decode("ascii")
    except UnicodeDecodeError:
        return "bad redirect domain", 400

    if domain.startswith("HTS"):
        # start a new login session
        session["password"] = None
        session["mfa"] = None
        session["redirect"] = domain[3:].strip()

        if body.username is not None and body.username in ACCOUNTS.keys():
            session["username"] = body.username
            return NextFrame(next_expected_frame(session)), 200
        else:  # unknown username, fallback to regular login
            session["username"] = None
            return NextFrame(next_expected_frame(session)), 200
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
        body = SubmittedFrame.from_dict(connexion.request.get_json())  # noqa: E501
    # username frames are always allowed
    if body.frame != next_expected_frame(session) and body.frame != "username":
        return "unexpected frame", 409

    if body.frame == "username":
        username = body.value
        if username in ACCOUNTS.keys():
            # username frames are special because they always restart authentication
            # (there is no way to submit a password and later the username, at least 
            # not with this stub)
            session["username"] = username
            session["password"] = None
            session["mfa"] = None
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
        # restrict cookie lifetime and domain stuff here
        return SuccessfulAuthentication(session["redirect"], "HackThisSite=theauthtoken"), 201
    else:
        return NextFrame(next_expected_frame(session), show_captcha=False), 200
