# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AccountRecoverysubmitSecretAnswerContent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, secret_answer: str=None):  # noqa: E501
        """AccountRecoverysubmitSecretAnswerContent - a model defined in Swagger

        :param secret_answer: The secret_answer of this AccountRecoverysubmitSecretAnswerContent.  # noqa: E501
        :type secret_answer: str
        """
        self.swagger_types = {
            'secret_answer': str
        }

        self.attribute_map = {
            'secret_answer': 'secret-answer'
        }
        self._secret_answer = secret_answer

    @classmethod
    def from_dict(cls, dikt) -> 'AccountRecoverysubmitSecretAnswerContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The account_recoverysubmit_secret_answer_content of this AccountRecoverysubmitSecretAnswerContent.  # noqa: E501
        :rtype: AccountRecoverysubmitSecretAnswerContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def secret_answer(self) -> str:
        """Gets the secret_answer of this AccountRecoverysubmitSecretAnswerContent.


        :return: The secret_answer of this AccountRecoverysubmitSecretAnswerContent.
        :rtype: str
        """
        return self._secret_answer

    @secret_answer.setter
    def secret_answer(self, secret_answer: str):
        """Sets the secret_answer of this AccountRecoverysubmitSecretAnswerContent.


        :param secret_answer: The secret_answer of this AccountRecoverysubmitSecretAnswerContent.
        :type secret_answer: str
        """
        if secret_answer is None:
            raise ValueError("Invalid value for `secret_answer`, must not be `None`")  # noqa: E501

        self._secret_answer = secret_answer
