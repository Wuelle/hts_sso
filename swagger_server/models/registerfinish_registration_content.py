# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RegisterfinishRegistrationContent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, h_captcha_response: str=None, password: str=None, secret_question: str=None, secret_answer: str=None):  # noqa: E501
        """RegisterfinishRegistrationContent - a model defined in Swagger

        :param h_captcha_response: The h_captcha_response of this RegisterfinishRegistrationContent.  # noqa: E501
        :type h_captcha_response: str
        :param password: The password of this RegisterfinishRegistrationContent.  # noqa: E501
        :type password: str
        :param secret_question: The secret_question of this RegisterfinishRegistrationContent.  # noqa: E501
        :type secret_question: str
        :param secret_answer: The secret_answer of this RegisterfinishRegistrationContent.  # noqa: E501
        :type secret_answer: str
        """
        self.swagger_types = {
            'h_captcha_response': str,
            'password': str,
            'secret_question': str,
            'secret_answer': str
        }

        self.attribute_map = {
            'h_captcha_response': 'h-captcha-response',
            'password': 'password',
            'secret_question': 'secret-question',
            'secret_answer': 'secret-answer'
        }
        self._h_captcha_response = h_captcha_response
        self._password = password
        self._secret_question = secret_question
        self._secret_answer = secret_answer

    @classmethod
    def from_dict(cls, dikt) -> 'RegisterfinishRegistrationContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The registerfinish_registration_content of this RegisterfinishRegistrationContent.  # noqa: E501
        :rtype: RegisterfinishRegistrationContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def h_captcha_response(self) -> str:
        """Gets the h_captcha_response of this RegisterfinishRegistrationContent.

        A token proving the user has completed the hcaptcha challenge. Only required if the user was prompted to complete a captcha before  # noqa: E501

        :return: The h_captcha_response of this RegisterfinishRegistrationContent.
        :rtype: str
        """
        return self._h_captcha_response

    @h_captcha_response.setter
    def h_captcha_response(self, h_captcha_response: str):
        """Sets the h_captcha_response of this RegisterfinishRegistrationContent.

        A token proving the user has completed the hcaptcha challenge. Only required if the user was prompted to complete a captcha before  # noqa: E501

        :param h_captcha_response: The h_captcha_response of this RegisterfinishRegistrationContent.
        :type h_captcha_response: str
        """

        self._h_captcha_response = h_captcha_response

    @property
    def password(self) -> str:
        """Gets the password of this RegisterfinishRegistrationContent.

        The account password  # noqa: E501

        :return: The password of this RegisterfinishRegistrationContent.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this RegisterfinishRegistrationContent.

        The account password  # noqa: E501

        :param password: The password of this RegisterfinishRegistrationContent.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def secret_question(self) -> str:
        """Gets the secret_question of this RegisterfinishRegistrationContent.

        A question which the user can answer to recover the account in case they ever forget their password or lose their MFA device  # noqa: E501

        :return: The secret_question of this RegisterfinishRegistrationContent.
        :rtype: str
        """
        return self._secret_question

    @secret_question.setter
    def secret_question(self, secret_question: str):
        """Sets the secret_question of this RegisterfinishRegistrationContent.

        A question which the user can answer to recover the account in case they ever forget their password or lose their MFA device  # noqa: E501

        :param secret_question: The secret_question of this RegisterfinishRegistrationContent.
        :type secret_question: str
        """

        self._secret_question = secret_question

    @property
    def secret_answer(self) -> str:
        """Gets the secret_answer of this RegisterfinishRegistrationContent.

        The answer to the secret question.  # noqa: E501

        :return: The secret_answer of this RegisterfinishRegistrationContent.
        :rtype: str
        """
        return self._secret_answer

    @secret_answer.setter
    def secret_answer(self, secret_answer: str):
        """Sets the secret_answer of this RegisterfinishRegistrationContent.

        The answer to the secret question.  # noqa: E501

        :param secret_answer: The secret_answer of this RegisterfinishRegistrationContent.
        :type secret_answer: str
        """

        self._secret_answer = secret_answer
