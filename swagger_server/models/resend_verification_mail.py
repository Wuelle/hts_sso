# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server import util


class ResendVerificationMail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None):  # noqa: E501
        """ResendVerificationMail - a model defined in Swagger

        :param nonce: The nonce of this ResendVerificationMail.  # noqa: E501
        :type nonce: NonceToken
        """
        self.swagger_types = {
            'nonce': NonceToken
        }

        self.attribute_map = {
            'nonce': 'nonce'
        }
        self._nonce = nonce

    @classmethod
    def from_dict(cls, dikt) -> 'ResendVerificationMail':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResendVerificationMail of this ResendVerificationMail.  # noqa: E501
        :rtype: ResendVerificationMail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this ResendVerificationMail.


        :return: The nonce of this ResendVerificationMail.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this ResendVerificationMail.


        :param nonce: The nonce of this ResendVerificationMail.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce
