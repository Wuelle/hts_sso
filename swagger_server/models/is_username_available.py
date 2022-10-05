# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.is_username_available_content import IsUsernameAvailableContent  # noqa: F401,E501
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class IsUsernameAvailable(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: IsUsernameAvailableContent=None):  # noqa: E501
        """IsUsernameAvailable - a model defined in Swagger

        :param nonce: The nonce of this IsUsernameAvailable.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this IsUsernameAvailable.  # noqa: E501
        :type content: IsUsernameAvailableContent
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': IsUsernameAvailableContent
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'IsUsernameAvailable':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IsUsernameAvailable of this IsUsernameAvailable.  # noqa: E501
        :rtype: IsUsernameAvailable
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this IsUsernameAvailable.


        :return: The nonce of this IsUsernameAvailable.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this IsUsernameAvailable.


        :param nonce: The nonce of this IsUsernameAvailable.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> IsUsernameAvailableContent:
        """Gets the content of this IsUsernameAvailable.


        :return: The content of this IsUsernameAvailable.
        :rtype: IsUsernameAvailableContent
        """
        return self._content

    @content.setter
    def content(self, content: IsUsernameAvailableContent):
        """Sets the content of this IsUsernameAvailable.


        :param content: The content of this IsUsernameAvailable.
        :type content: IsUsernameAvailableContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
