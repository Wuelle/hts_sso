# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NonceToken5Content(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, captcha_required: bool=None):  # noqa: E501
        """NonceToken5Content - a model defined in Swagger

        :param captcha_required: The captcha_required of this NonceToken5Content.  # noqa: E501
        :type captcha_required: bool
        """
        self.swagger_types = {
            'captcha_required': bool
        }

        self.attribute_map = {
            'captcha_required': 'captcha-required'
        }
        self._captcha_required = captcha_required

    @classmethod
    def from_dict(cls, dikt) -> 'NonceToken5Content':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NonceToken_5_content of this NonceToken5Content.  # noqa: E501
        :rtype: NonceToken5Content
        """
        return util.deserialize_model(dikt, cls)

    @property
    def captcha_required(self) -> bool:
        """Gets the captcha_required of this NonceToken5Content.


        :return: The captcha_required of this NonceToken5Content.
        :rtype: bool
        """
        return self._captcha_required

    @captcha_required.setter
    def captcha_required(self, captcha_required: bool):
        """Sets the captcha_required of this NonceToken5Content.


        :param captcha_required: The captcha_required of this NonceToken5Content.
        :type captcha_required: bool
        """
        if captcha_required is None:
            raise ValueError("Invalid value for `captcha_required`, must not be `None`")  # noqa: E501

        self._captcha_required = captcha_required
