import connexion
import six

from swagger_server.models.nonce_token2 import NonceToken2  # noqa: E501
from swagger_server import util


def session_get_nonce_token(area=None):  # noqa: E501
    """Get a nonce

    Get a one time session token for a specific area of the site (login, registration...) # noqa: E501

    :param area: 
    :type area: str

    :rtype: NonceToken2
    """
    return NonceToken2("example token")
