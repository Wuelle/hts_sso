# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.nonce_token import NonceToken  # noqa: F401,E501
from swagger_server.models.registerstart_registration_content import RegisterstartRegistrationContent  # noqa: F401,E501
from swagger_server import util


class PrimaryAccountDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nonce: NonceToken=None, content: RegisterstartRegistrationContent=None):  # noqa: E501
        """PrimaryAccountDetails - a model defined in Swagger

        :param nonce: The nonce of this PrimaryAccountDetails.  # noqa: E501
        :type nonce: NonceToken
        :param content: The content of this PrimaryAccountDetails.  # noqa: E501
        :type content: RegisterstartRegistrationContent
        """
        self.swagger_types = {
            'nonce': NonceToken,
            'content': RegisterstartRegistrationContent
        }

        self.attribute_map = {
            'nonce': 'nonce',
            'content': 'content'
        }
        self._nonce = nonce
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'PrimaryAccountDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PrimaryAccountDetails of this PrimaryAccountDetails.  # noqa: E501
        :rtype: PrimaryAccountDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nonce(self) -> NonceToken:
        """Gets the nonce of this PrimaryAccountDetails.


        :return: The nonce of this PrimaryAccountDetails.
        :rtype: NonceToken
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: NonceToken):
        """Sets the nonce of this PrimaryAccountDetails.


        :param nonce: The nonce of this PrimaryAccountDetails.
        :type nonce: NonceToken
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501

        self._nonce = nonce

    @property
    def content(self) -> RegisterstartRegistrationContent:
        """Gets the content of this PrimaryAccountDetails.


        :return: The content of this PrimaryAccountDetails.
        :rtype: RegisterstartRegistrationContent
        """
        return self._content

    @content.setter
    def content(self, content: RegisterstartRegistrationContent):
        """Sets the content of this PrimaryAccountDetails.


        :param content: The content of this PrimaryAccountDetails.
        :type content: RegisterstartRegistrationContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
