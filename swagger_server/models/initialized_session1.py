# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.initialized_session1_content import InitializedSession1Content  # noqa: F401,E501
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class InitializedSession1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: InitializedSession1Content=None):  # noqa: E501
        """InitializedSession1 - a model defined in Swagger

        :param nonce: The nonce of this InitializedSession1.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this InitializedSession1.  # noqa: E501
        :type content: InitializedSession1Content
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': InitializedSession1Content
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'InitializedSession1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InitializedSession_1 of this InitializedSession1.  # noqa: E501
        :rtype: InitializedSession1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this InitializedSession1.


        :return: The nonce of this InitializedSession1.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this InitializedSession1.


        :param nonce: The nonce of this InitializedSession1.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> InitializedSession1Content:
        """Gets the content of this InitializedSession1.


        :return: The content of this InitializedSession1.
        :rtype: InitializedSession1Content
        """
        return self._content

    @content.setter
    def content(self, content: InitializedSession1Content):
        """Sets the content of this InitializedSession1.


        :param content: The content of this InitializedSession1.
        :type content: InitializedSession1Content
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
