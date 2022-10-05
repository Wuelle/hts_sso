# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.captcha_prompt import CaptchaPrompt  # noqa: F401,E501
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class InlineResponse403(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: CaptchaPrompt=None):  # noqa: E501
        """InlineResponse403 - a model defined in Swagger

        :param nonce: The nonce of this InlineResponse403.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this InlineResponse403.  # noqa: E501
        :type content: CaptchaPrompt
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': CaptchaPrompt
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse403':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_403 of this InlineResponse403.  # noqa: E501
        :rtype: InlineResponse403
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this InlineResponse403.


        :return: The nonce of this InlineResponse403.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this InlineResponse403.


        :param nonce: The nonce of this InlineResponse403.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> CaptchaPrompt:
        """Gets the content of this InlineResponse403.


        :return: The content of this InlineResponse403.
        :rtype: CaptchaPrompt
        """
        return self._content

    @content.setter
    def content(self, content: CaptchaPrompt):
        """Sets the content of this InlineResponse403.


        :param content: The content of this InlineResponse403.
        :type content: CaptchaPrompt
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content