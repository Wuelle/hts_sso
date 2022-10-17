# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NonceToken3(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: str=None):  # noqa: E501
        """NonceToken3 - a model defined in Swagger

        :param nonce: The nonce of this NonceToken3.  # noqa: E501
        :type nonce: str
        """
        self.swagger_types = {
            'nonce': str
        }

        self.attribute_map = {
            'nonce': 'nonce'
        }
        self._nonce = nonce

    @classmethod
    def from_dict(cls, dikt) -> 'NonceToken3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NonceToken_3 of this NonceToken3.  # noqa: E501
        :rtype: NonceToken3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> str:
        """Gets the nonce of this NonceToken3.


        :return: The nonce of this NonceToken3.
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: str):
        """Sets the nonce of this NonceToken3.


        :param nonce: The nonce of this NonceToken3.
        :type nonce: str
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce
