# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.linked_accounts import LinkedAccounts  # noqa: F401,E501
from swagger_server import util


class AccountInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_name: str=None, display_name: str=None, joined: str=None, last_login: str=None, email: str=None, website: str=None, timezone: int=None, avatar_url: str=None, about_me: str=None, linked_accounts: LinkedAccounts=None):  # noqa: E501
        """AccountInfo - a model defined in Swagger

        :param account_name: The account_name of this AccountInfo.  # noqa: E501
        :type account_name: str
        :param display_name: The display_name of this AccountInfo.  # noqa: E501
        :type display_name: str
        :param joined: The joined of this AccountInfo.  # noqa: E501
        :type joined: str
        :param last_login: The last_login of this AccountInfo.  # noqa: E501
        :type last_login: str
        :param email: The email of this AccountInfo.  # noqa: E501
        :type email: str
        :param website: The website of this AccountInfo.  # noqa: E501
        :type website: str
        :param timezone: The timezone of this AccountInfo.  # noqa: E501
        :type timezone: int
        :param avatar_url: The avatar_url of this AccountInfo.  # noqa: E501
        :type avatar_url: str
        :param about_me: The about_me of this AccountInfo.  # noqa: E501
        :type about_me: str
        :param linked_accounts: The linked_accounts of this AccountInfo.  # noqa: E501
        :type linked_accounts: LinkedAccounts
        """
        self.swagger_types = {
            'account_name': str,
            'display_name': str,
            'joined': str,
            'last_login': str,
            'email': str,
            'website': str,
            'timezone': int,
            'avatar_url': str,
            'about_me': str,
            'linked_accounts': LinkedAccounts
        }

        self.attribute_map = {
            'account_name': 'account-name',
            'display_name': 'display-name',
            'joined': 'joined',
            'last_login': 'last-login',
            'email': 'email',
            'website': 'website',
            'timezone': 'timezone',
            'avatar_url': 'avatar-url',
            'about_me': 'about-me',
            'linked_accounts': 'linked-accounts'
        }
        self._account_name = account_name
        self._display_name = display_name
        self._joined = joined
        self._last_login = last_login
        self._email = email
        self._website = website
        self._timezone = timezone
        self._avatar_url = avatar_url
        self._about_me = about_me
        self._linked_accounts = linked_accounts

    @classmethod
    def from_dict(cls, dikt) -> 'AccountInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccountInfo of this AccountInfo.  # noqa: E501
        :rtype: AccountInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_name(self) -> str:
        """Gets the account_name of this AccountInfo.


        :return: The account_name of this AccountInfo.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name: str):
        """Sets the account_name of this AccountInfo.


        :param account_name: The account_name of this AccountInfo.
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def display_name(self) -> str:
        """Gets the display_name of this AccountInfo.


        :return: The display_name of this AccountInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this AccountInfo.


        :param display_name: The display_name of this AccountInfo.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def joined(self) -> str:
        """Gets the joined of this AccountInfo.


        :return: The joined of this AccountInfo.
        :rtype: str
        """
        return self._joined

    @joined.setter
    def joined(self, joined: str):
        """Sets the joined of this AccountInfo.


        :param joined: The joined of this AccountInfo.
        :type joined: str
        """

        self._joined = joined

    @property
    def last_login(self) -> str:
        """Gets the last_login of this AccountInfo.


        :return: The last_login of this AccountInfo.
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login: str):
        """Sets the last_login of this AccountInfo.


        :param last_login: The last_login of this AccountInfo.
        :type last_login: str
        """

        self._last_login = last_login

    @property
    def email(self) -> str:
        """Gets the email of this AccountInfo.


        :return: The email of this AccountInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this AccountInfo.


        :param email: The email of this AccountInfo.
        :type email: str
        """

        self._email = email

    @property
    def website(self) -> str:
        """Gets the website of this AccountInfo.


        :return: The website of this AccountInfo.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: str):
        """Sets the website of this AccountInfo.


        :param website: The website of this AccountInfo.
        :type website: str
        """

        self._website = website

    @property
    def timezone(self) -> int:
        """Gets the timezone of this AccountInfo.


        :return: The timezone of this AccountInfo.
        :rtype: int
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone: int):
        """Sets the timezone of this AccountInfo.


        :param timezone: The timezone of this AccountInfo.
        :type timezone: int
        """

        self._timezone = timezone

    @property
    def avatar_url(self) -> str:
        """Gets the avatar_url of this AccountInfo.


        :return: The avatar_url of this AccountInfo.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url: str):
        """Sets the avatar_url of this AccountInfo.


        :param avatar_url: The avatar_url of this AccountInfo.
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def about_me(self) -> str:
        """Gets the about_me of this AccountInfo.


        :return: The about_me of this AccountInfo.
        :rtype: str
        """
        return self._about_me

    @about_me.setter
    def about_me(self, about_me: str):
        """Sets the about_me of this AccountInfo.


        :param about_me: The about_me of this AccountInfo.
        :type about_me: str
        """

        self._about_me = about_me

    @property
    def linked_accounts(self) -> LinkedAccounts:
        """Gets the linked_accounts of this AccountInfo.


        :return: The linked_accounts of this AccountInfo.
        :rtype: LinkedAccounts
        """
        return self._linked_accounts

    @linked_accounts.setter
    def linked_accounts(self, linked_accounts: LinkedAccounts):
        """Sets the linked_accounts of this AccountInfo.


        :param linked_accounts: The linked_accounts of this AccountInfo.
        :type linked_accounts: LinkedAccounts
        """

        self._linked_accounts = linked_accounts
