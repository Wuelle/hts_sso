# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResendVerificationMail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, email: str=None):  # noqa: E501
        """ResendVerificationMail - a model defined in Swagger

        :param username: The username of this ResendVerificationMail.  # noqa: E501
        :type username: str
        :param email: The email of this ResendVerificationMail.  # noqa: E501
        :type email: str
        """
        self.swagger_types = {
            'username': str,
            'email': str
        }

        self.attribute_map = {
            'username': 'username',
            'email': 'email'
        }
        self._username = username
        self._email = email

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
    def username(self) -> str:
        """Gets the username of this ResendVerificationMail.


        :return: The username of this ResendVerificationMail.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this ResendVerificationMail.


        :param username: The username of this ResendVerificationMail.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this ResendVerificationMail.


        :return: The email of this ResendVerificationMail.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this ResendVerificationMail.


        :param email: The email of this ResendVerificationMail.
        :type email: str
        """

        self._email = email
