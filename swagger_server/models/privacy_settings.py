# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.privacy_setting import PrivacySetting  # noqa: F401,E501
from swagger_server import util


class PrivacySettings(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, email: PrivacySetting=None, irc_nicks: PrivacySetting=None, linked_discord_accounts: PrivacySetting=None):  # noqa: E501
        """PrivacySettings - a model defined in Swagger

        :param email: The email of this PrivacySettings.  # noqa: E501
        :type email: PrivacySetting
        :param irc_nicks: The irc_nicks of this PrivacySettings.  # noqa: E501
        :type irc_nicks: PrivacySetting
        :param linked_discord_accounts: The linked_discord_accounts of this PrivacySettings.  # noqa: E501
        :type linked_discord_accounts: PrivacySetting
        """
        self.swagger_types = {
            'email': PrivacySetting,
            'irc_nicks': PrivacySetting,
            'linked_discord_accounts': PrivacySetting
        }

        self.attribute_map = {
            'email': 'email',
            'irc_nicks': 'irc-nicks',
            'linked_discord_accounts': 'linked-discord-accounts'
        }
        self._email = email
        self._irc_nicks = irc_nicks
        self._linked_discord_accounts = linked_discord_accounts

    @classmethod
    def from_dict(cls, dikt) -> 'PrivacySettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PrivacySettings of this PrivacySettings.  # noqa: E501
        :rtype: PrivacySettings
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> PrivacySetting:
        """Gets the email of this PrivacySettings.


        :return: The email of this PrivacySettings.
        :rtype: PrivacySetting
        """
        return self._email

    @email.setter
    def email(self, email: PrivacySetting):
        """Sets the email of this PrivacySettings.


        :param email: The email of this PrivacySettings.
        :type email: PrivacySetting
        """

        self._email = email

    @property
    def irc_nicks(self) -> PrivacySetting:
        """Gets the irc_nicks of this PrivacySettings.


        :return: The irc_nicks of this PrivacySettings.
        :rtype: PrivacySetting
        """
        return self._irc_nicks

    @irc_nicks.setter
    def irc_nicks(self, irc_nicks: PrivacySetting):
        """Sets the irc_nicks of this PrivacySettings.


        :param irc_nicks: The irc_nicks of this PrivacySettings.
        :type irc_nicks: PrivacySetting
        """

        self._irc_nicks = irc_nicks

    @property
    def linked_discord_accounts(self) -> PrivacySetting:
        """Gets the linked_discord_accounts of this PrivacySettings.


        :return: The linked_discord_accounts of this PrivacySettings.
        :rtype: PrivacySetting
        """
        return self._linked_discord_accounts

    @linked_discord_accounts.setter
    def linked_discord_accounts(self, linked_discord_accounts: PrivacySetting):
        """Sets the linked_discord_accounts of this PrivacySettings.


        :param linked_discord_accounts: The linked_discord_accounts of this PrivacySettings.
        :type linked_discord_accounts: PrivacySetting
        """

        self._linked_discord_accounts = linked_discord_accounts
