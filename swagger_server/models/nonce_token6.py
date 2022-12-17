# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.nonce_token5_content import NonceToken5Content  # noqa: F401,E501
from swagger_server import util


class NonceToken6(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: str=None, content: NonceToken5Content=None):  # noqa: E501
        """NonceToken6 - a model defined in Swagger

        :param nonce: The nonce of this NonceToken6.  # noqa: E501
        :type nonce: str
        :param content: The content of this NonceToken6.  # noqa: E501
        :type content: NonceToken5Content
        """
        self.swagger_types = {
            'nonce': str,
            'content': NonceToken5Content
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'NonceToken6':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NonceToken_6 of this NonceToken6.  # noqa: E501
        :rtype: NonceToken6
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> str:
        """Gets the nonce of this NonceToken6.


        :return: The nonce of this NonceToken6.
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: str):
        """Sets the nonce of this NonceToken6.


        :param nonce: The nonce of this NonceToken6.
        :type nonce: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> NonceToken5Content:
        """Gets the content of this NonceToken6.


        :return: The content of this NonceToken6.
        :rtype: NonceToken5Content
        """
        return self._content

    @content.setter
    def content(self, content: NonceToken5Content):
        """Sets the content of this NonceToken6.


        :param content: The content of this NonceToken6.
        :type content: NonceToken5Content
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
