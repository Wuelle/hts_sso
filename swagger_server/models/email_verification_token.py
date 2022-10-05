# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server.models.registerverify_email_address_content import RegisterverifyEmailAddressContent  # noqa: F401,E501
from swagger_server import util


class EmailVerificationToken(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: RegisterverifyEmailAddressContent=None):  # noqa: E501
        """EmailVerificationToken - a model defined in Swagger

        :param nonce: The nonce of this EmailVerificationToken.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this EmailVerificationToken.  # noqa: E501
        :type content: RegisterverifyEmailAddressContent
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': RegisterverifyEmailAddressContent
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'EmailVerificationToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmailVerificationToken of this EmailVerificationToken.  # noqa: E501
        :rtype: EmailVerificationToken
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this EmailVerificationToken.


        :return: The nonce of this EmailVerificationToken.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this EmailVerificationToken.


        :param nonce: The nonce of this EmailVerificationToken.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> RegisterverifyEmailAddressContent:
        """Gets the content of this EmailVerificationToken.


        :return: The content of this EmailVerificationToken.
        :rtype: RegisterverifyEmailAddressContent
        """
        return self._content

    @content.setter
    def content(self, content: RegisterverifyEmailAddressContent):
        """Sets the content of this EmailVerificationToken.


        :param content: The content of this EmailVerificationToken.
        :type content: RegisterverifyEmailAddressContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
