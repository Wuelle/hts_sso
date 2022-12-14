# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.login_frame import LoginFrame  # noqa: F401,E501
from swagger_server import util


class InitializedSessionContent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, first_frame: LoginFrame=None):  # noqa: E501
        """InitializedSessionContent - a model defined in Swagger

        :param first_frame: The first_frame of this InitializedSessionContent.  # noqa: E501
        :type first_frame: LoginFrame
        """
        self.swagger_types = {
            'first_frame': LoginFrame
        }

        self.attribute_map = {
            'first_frame': 'first-frame'
        }
        self._first_frame = first_frame

    @classmethod
    def from_dict(cls, dikt) -> 'InitializedSessionContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InitializedSession_content of this InitializedSessionContent.  # noqa: E501
        :rtype: InitializedSessionContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_frame(self) -> LoginFrame:
        """Gets the first_frame of this InitializedSessionContent.


        :return: The first_frame of this InitializedSessionContent.
        :rtype: LoginFrame
        """
        return self._first_frame

    @first_frame.setter
    def first_frame(self, first_frame: LoginFrame):
        """Sets the first_frame of this InitializedSessionContent.


        :param first_frame: The first_frame of this InitializedSessionContent.
        :type first_frame: LoginFrame
        """
        if first_frame is None:
            raise ValueError("Invalid value for `first_frame`, must not be `None`")  # noqa: E501

        self._first_frame = first_frame
