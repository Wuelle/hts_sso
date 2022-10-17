# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_recoveryrequest_passphrase_update_token_content import AccountRecoveryrequestPassphraseUpdateTokenContent  # noqa: F401,E501
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class RequestPasswordResetToken(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: AccountRecoveryrequestPassphraseUpdateTokenContent=None):  # noqa: E501
        """RequestPasswordResetToken - a model defined in Swagger

        :param nonce: The nonce of this RequestPasswordResetToken.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this RequestPasswordResetToken.  # noqa: E501
        :type content: AccountRecoveryrequestPassphraseUpdateTokenContent
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': AccountRecoveryrequestPassphraseUpdateTokenContent
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'RequestPasswordResetToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestPasswordResetToken of this RequestPasswordResetToken.  # noqa: E501
        :rtype: RequestPasswordResetToken
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this RequestPasswordResetToken.


        :return: The nonce of this RequestPasswordResetToken.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this RequestPasswordResetToken.


        :param nonce: The nonce of this RequestPasswordResetToken.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> AccountRecoveryrequestPassphraseUpdateTokenContent:
        """Gets the content of this RequestPasswordResetToken.


        :return: The content of this RequestPasswordResetToken.
        :rtype: AccountRecoveryrequestPassphraseUpdateTokenContent
        """
        return self._content

    @content.setter
    def content(self, content: AccountRecoveryrequestPassphraseUpdateTokenContent):
        """Sets the content of this RequestPasswordResetToken.


        :param content: The content of this RequestPasswordResetToken.
        :type content: AccountRecoveryrequestPassphraseUpdateTokenContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
