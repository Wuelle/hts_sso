import connexion
import six

from swagger_server.models.captcha_prompt import CaptchaPrompt  # noqa: E501
from swagger_server.models.init_login_session import InitLoginSession  # noqa: E501
from swagger_server.models.next_frame import NextFrame  # noqa: E501
from swagger_server.models.submitted_frame import SubmittedFrame  # noqa: E501
from swagger_server.models.successful_authentication import SuccessfulAuthentication  # noqa: E501
from swagger_server import util


def login_init_session(body):  # noqa: E501
    """Start logging in

    Validates the users redirect url and, if it is valid, starts a login session on the server. If a username is provided, the client will not have to fill out the username frame while logging in (re-authentication) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NextFrame
    """
    if connexion.request.is_json:
        body = InitLoginSession.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
    return 'do some magic!'
