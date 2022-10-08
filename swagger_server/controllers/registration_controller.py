import connexion
import six

from swagger_server.models.change_verication_mail_address import ChangeVericationMailAddress  # noqa: E501
from swagger_server.models.email_verification_token import EmailVerificationToken  # noqa: E501
from swagger_server.models.finish_registration import FinishRegistration  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.invalid_verification_code import InvalidVerificationCode  # noqa: E501
from swagger_server.models.is_initial_captcha_required import IsInitialCaptchaRequired  # noqa: E501
from swagger_server.models.is_username_available import IsUsernameAvailable  # noqa: E501
from swagger_server.models.primary_account_details import PrimaryAccountDetails  # noqa: E501
from swagger_server.models.resend_verification_mail import ResendVerificationMail  # noqa: E501
from swagger_server.models.resend_verification_mail1 import ResendVerificationMail1  # noqa: E501
from swagger_server.models.username import Username  # noqa: E501
from swagger_server import util

from swagger_server.models.is_initial_captcha_required_content import IsInitialCaptchaRequiredContent  # noqa: E501
from swagger_server.models.is_username_available_content import IsUsernameAvailableContent  # noqa: F401,E501
from swagger_server.models.inline_response200_content import InlineResponse200Content  # noqa: F401,E501
from swagger_server.models.successful_authentication import SuccessfulAuthentication


def register_change_verification_mail(body):  # noqa: E501
    """Change the email linked with an account that is currently being registered.

    This exists in case the user mistyped their email. The user must be able to provide the email that was previously used as well as the username that should be registered. If the address was successfully changed, a new verification mail should be sent. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse401
    """
    if connexion.request.is_json:
        body = ChangeVericationMailAddress.from_dict(connexion.request.get_json())  # noqa: E501
    return InlineResponse401(nonce="new nonce"), 200


def register_finish_registration(body):  # noqa: E501
    """Complete a users account

    Allows the user to set their password/secret question to complete their account setup # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = FinishRegistration.from_dict(connexion.request.get_json())  # noqa: E501
    content = SuccessfulAuthentication(
            redirect="https://hackthissite.org",
            token="example login token"
    )
    return InlineResponse201(nonce="abc", content=content), 201;


def register_is_initial_captcha_required(body):  # noqa: E501
    """Whether the user needs to complete a captcha on the first frame

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: IsInitialCaptchaRequired
    """
    if connexion.request.is_json:
        body = ResendVerificationMail.from_dict(connexion.request.get_json())  # noqa: E501
    return IsInitialCaptchaRequired(nonce="new nonce", content=IsInitialCaptchaRequiredContent(True))


def register_is_username_available(body):  # noqa: E501
    """Check if a username is available

    If the username is not valid (too long/short etc) the server should ignore that and simply respond with &#x27;not available&#x27; # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: IsUsernameAvailable
    """
    if connexion.request.is_json:
        body = Username.from_dict(connexion.request.get_json())  # noqa: E501

    response = IsUsernameAvailable(nonce="abc")
    if body.content.username == "Alaska":
        response.content = IsUsernameAvailableContent(False)
    else:
        response.content = IsUsernameAvailableContent(True)
    return response


def register_resend_verification_mail(body):  # noqa: E501
    """Send another verification mail

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse401
    """
    if connexion.request.is_json:
        body = ResendVerificationMail1.from_dict(connexion.request.get_json())  # noqa: E501
    return InlineResponse401(nonce="new nonce"), 200;


def register_start_registration(body):  # noqa: E501
    """Reserve an account name and link it with an email

    This is the first stage of registration, the user will need to verify their email and then set their passphrase/account details # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse401
    """
    if connexion.request.is_json:
        body = PrimaryAccountDetails.from_dict(connexion.request.get_json())  # noqa: E501
    if body.content.username == "Alaska":  # totally invalid username
        return InlineResponse401(nonce="new nonce"), 403;
    else:
        return InlineResponse401(nonce="new nonce"), 200;



def register_verify_email_address(body):  # noqa: E501
    """Verify a users account email

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = EmailVerificationToken.from_dict(connexion.request.get_json())  # noqa: E501
    if body.content.verification_code != "123":
        return InlineResponse401(nonce="new nonce"), 403;
    else:
        return InlineResponse200(nonce="new nonce", content=InlineResponse200Content(True)), 200;
