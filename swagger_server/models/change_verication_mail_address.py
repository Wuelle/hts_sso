# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ChangeVericationMailAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None, old_email: str=None, new_email: str=None):  # noqa: E501
        """ChangeVericationMailAddress - a model defined in Swagger

        :param username: The username of this ChangeVericationMailAddress.  # noqa: E501
        :type username: str
        :param old_email: The old_email of this ChangeVericationMailAddress.  # noqa: E501
        :type old_email: str
        :param new_email: The new_email of this ChangeVericationMailAddress.  # noqa: E501
        :type new_email: str
        """
        self.swagger_types = {
            'username': str,
            'old_email': str,
            'new_email': str
        }

        self.attribute_map = {
            'username': 'username',
            'old_email': 'old-email',
            'new_email': 'new-email'
        }
        self._username = username
        self._old_email = old_email
        self._new_email = new_email

    @classmethod
    def from_dict(cls, dikt) -> 'ChangeVericationMailAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChangeVericationMailAddress of this ChangeVericationMailAddress.  # noqa: E501
        :rtype: ChangeVericationMailAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this ChangeVericationMailAddress.


        :return: The username of this ChangeVericationMailAddress.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this ChangeVericationMailAddress.


        :param username: The username of this ChangeVericationMailAddress.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def old_email(self) -> str:
        """Gets the old_email of this ChangeVericationMailAddress.


        :return: The old_email of this ChangeVericationMailAddress.
        :rtype: str
        """
        return self._old_email

    @old_email.setter
    def old_email(self, old_email: str):
        """Sets the old_email of this ChangeVericationMailAddress.


        :param old_email: The old_email of this ChangeVericationMailAddress.
        :type old_email: str
        """
        if old_email is None:
            raise ValueError("Invalid value for `old_email`, must not be `None`")  # noqa: E501

        self._old_email = old_email

    @property
    def new_email(self) -> str:
        """Gets the new_email of this ChangeVericationMailAddress.


        :return: The new_email of this ChangeVericationMailAddress.
        :rtype: str
        """
        return self._new_email

    @new_email.setter
    def new_email(self, new_email: str):
        """Sets the new_email of this ChangeVericationMailAddress.


        :param new_email: The new_email of this ChangeVericationMailAddress.
        :type new_email: str
        """
        if new_email is None:
            raise ValueError("Invalid value for `new_email`, must not be `None`")  # noqa: E501

        self._new_email = new_email
