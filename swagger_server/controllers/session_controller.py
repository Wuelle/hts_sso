import connexion
import six

from swagger_server.models.nonce_token1 import NonceToken1  # noqa: E501
from swagger_server import util


def session_get_nonce_token(area=None):  # noqa: E501
    """Get a nonce

    Get a one time session token for a specific area of the site (login, registration...) # noqa: E501

    :param area: 
    :type area: str

    :rtype: NonceToken1
    """
    return NonceToken1("example token")
