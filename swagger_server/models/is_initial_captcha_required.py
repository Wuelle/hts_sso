# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.is_initial_captcha_required_content import IsInitialCaptchaRequiredContent  # noqa: F401,E501
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class IsInitialCaptchaRequired(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: IsInitialCaptchaRequiredContent=None):  # noqa: E501
        """IsInitialCaptchaRequired - a model defined in Swagger

        :param nonce: The nonce of this IsInitialCaptchaRequired.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this IsInitialCaptchaRequired.  # noqa: E501
        :type content: IsInitialCaptchaRequiredContent
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': IsInitialCaptchaRequiredContent
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'IsInitialCaptchaRequired':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IsInitialCaptchaRequired of this IsInitialCaptchaRequired.  # noqa: E501
        :rtype: IsInitialCaptchaRequired
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this IsInitialCaptchaRequired.


        :return: The nonce of this IsInitialCaptchaRequired.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this IsInitialCaptchaRequired.


        :param nonce: The nonce of this IsInitialCaptchaRequired.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> IsInitialCaptchaRequiredContent:
        """Gets the content of this IsInitialCaptchaRequired.


        :return: The content of this IsInitialCaptchaRequired.
        :rtype: IsInitialCaptchaRequiredContent
        """
        return self._content

    @content.setter
    def content(self, content: IsInitialCaptchaRequiredContent):
        """Sets the content of this IsInitialCaptchaRequired.


        :param content: The content of this IsInitialCaptchaRequired.
        :type content: IsInitialCaptchaRequiredContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content