# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_recoverysubmit_captcha_token_content import AccountRecoverysubmitCaptchaTokenContent  # noqa: F401,E501
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class SubmitCaptchaToken(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: AccountRecoverysubmitCaptchaTokenContent=None):  # noqa: E501
        """SubmitCaptchaToken - a model defined in Swagger

        :param nonce: The nonce of this SubmitCaptchaToken.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this SubmitCaptchaToken.  # noqa: E501
        :type content: AccountRecoverysubmitCaptchaTokenContent
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': AccountRecoverysubmitCaptchaTokenContent
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'SubmitCaptchaToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubmitCaptchaToken of this SubmitCaptchaToken.  # noqa: E501
        :rtype: SubmitCaptchaToken
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this SubmitCaptchaToken.


        :return: The nonce of this SubmitCaptchaToken.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this SubmitCaptchaToken.


        :param nonce: The nonce of this SubmitCaptchaToken.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> AccountRecoverysubmitCaptchaTokenContent:
        """Gets the content of this SubmitCaptchaToken.


        :return: The content of this SubmitCaptchaToken.
        :rtype: AccountRecoverysubmitCaptchaTokenContent
        """
        return self._content

    @content.setter
    def content(self, content: AccountRecoverysubmitCaptchaTokenContent):
        """Sets the content of this SubmitCaptchaToken.


        :param content: The content of this SubmitCaptchaToken.
        :type content: AccountRecoverysubmitCaptchaTokenContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
