import connexion
import six

from swagger_server.models.nonce_token1 import NonceToken1  # noqa: E501
from swagger_server.models.nonce_token2 import NonceToken2  # noqa: E501
from swagger_server.models.nonce_token3 import NonceToken3  # noqa: E501
from swagger_server.models.nonce_token4 import NonceToken4  # noqa: E501
from swagger_server.models.nonce_token5 import NonceToken5  # noqa: E501
from swagger_server.models.passphrase_update_token import PassphraseUpdateToken  # noqa: E501
from swagger_server.models.request_passphrase_reset_token import RequestPassphraseResetToken  # noqa: E501
from swagger_server.models.request_username_reminder import RequestUsernameReminder  # noqa: E501
from swagger_server.models.submit_captcha_token import SubmitCaptchaToken  # noqa: E501
from swagger_server.models.update_passphrase import UpdatePassphrase  # noqa: E501
from swagger_server.models.update_passphrase1 import UpdatePassphrase1  # noqa: E501
from swagger_server import util

from swagger_server.models.nonce_token2_content import NonceToken2Content  # noqa: F401,E501
from swagger_server.models.nonce_token4_content import NonceToken4Content  # noqa: F401,E501

def account_recovery_request_passphrase_reset_token(body):  # noqa: E501
    """account_recovery_request_passphrase_reset_token

    This can be called multiple times in the same session, if the user clicks the &#x27;resend mail&#x27; link # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NonceToken1
    """
    if connexion.request.is_json:
        body = RequestPassphraseResetToken.from_dict(connexion.request.get_json())  # noqa: E501
    return NonceToken1(nonce="abc"), 200


def account_recovery_request_username_reminder(body):  # noqa: E501
    """Send a username reminder mail

    Receive a mail containing the usernames associated with a given address. Note that the response does *not* reveal whether that email belongs to *any* account # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NonceToken5
    """
    if connexion.request.is_json:
        body = RequestUsernameReminder.from_dict(connexion.request.get_json())  # noqa: E501
    return NonceToken4(nonce="abc", content=NonceToken4Content(captcha_required=True)), 200


def account_recovery_submit_captcha_token(body):  # noqa: E501
    """account_recovery_submit_captcha_token

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NonceToken1
    """
    if connexion.request.is_json:
        body = SubmitCaptchaToken.from_dict(connexion.request.get_json())  # noqa: E501
    return NonceToken1(nonce="abc"), 200


def account_recovery_submit_passphrase_update_token(body):  # noqa: E501
    """Send a username reminder mail

    Receive a mail containing the usernames associated with a given address. Note that the response does *not* reveal whether that email belongs to *any* account # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NonceToken2
    """
    if connexion.request.is_json:
        body = PassphraseUpdateToken.from_dict(connexion.request.get_json())  # noqa: E501
    return NonceToken2(nonce="abc", content=NonceToken2Content(secret_question="1 + 1 = what?")), 200


def account_recovery_submit_secret_answer(body):  # noqa: E501
    """account_recovery_submit_secret_answer

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NonceToken4
    """
    if connexion.request.is_json:
        body = UpdatePassphrase1.from_dict(connexion.request.get_json())  # noqa: E501
    if body.content.secret_answer != "beep":
        return NonceToken1(nonce="abc"), 403
    else:
        return NonceToken1(nonce="abc"), 200


def account_recovery_update_passphrase(body):  # noqa: E501
    """account_recovery_update_passphrase

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: NonceToken3
    """
    if connexion.request.is_json:
        body = UpdatePassphrase.from_dict(connexion.request.get_json())  # noqa: E501
    return NonceToken3(nonce="abc"), 200
