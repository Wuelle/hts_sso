# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200Content(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, captcha_required: bool=None):  # noqa: E501
        """InlineResponse200Content - a model defined in Swagger

        :param captcha_required: The captcha_required of this InlineResponse200Content.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'InlineResponse200Content':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_content of this InlineResponse200Content.  # noqa: E501
        :rtype: InlineResponse200Content
        """
        return util.deserialize_model(dikt, cls)

    @property
    def captcha_required(self) -> bool:
        """Gets the captcha_required of this InlineResponse200Content.


        :return: The captcha_required of this InlineResponse200Content.
        :rtype: bool
        """
        return self._captcha_required

    @captcha_required.setter
    def captcha_required(self, captcha_required: bool):
        """Sets the captcha_required of this InlineResponse200Content.


        :param captcha_required: The captcha_required of this InlineResponse200Content.
        :type captcha_required: bool
        """

        self._captcha_required = captcha_required