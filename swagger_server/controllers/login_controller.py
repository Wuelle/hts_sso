import connexion
import six

from swagger_server.models.init_login_session import InitLoginSession  # noqa: E501
from swagger_server.models.initialized_session import InitializedSession  # noqa: E501
from swagger_server.models.initialized_session1 import InitializedSession1  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.inline_response403 import InlineResponse403  # noqa: E501
from swagger_server.models.login_submit_frame_body import LoginSubmitFrameBody  # noqa: E501
from swagger_server.models.nonce_token1 import NonceToken1  # noqa: E501
from swagger_server import util


def login_init_session(body):  # noqa: E501
    """Start logging in

    Validates the users redirect url and, if it is valid, starts a login session on the server. If a username is provided, the client will not have to fill out the username frame while logging in (re-authentication) # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InitializedSession
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

    :rtype: InitializedSession1
    """
    if connexion.request.is_json:
        body = LoginSubmitFrameBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
