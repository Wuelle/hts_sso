# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.change_verication_mail_address import ChangeVericationMailAddress  # noqa: E501
from swagger_server.models.email_verification_token import EmailVerificationToken  # noqa: E501
from swagger_server.models.finish_registration import FinishRegistration  # noqa: E501
from swagger_server.models.is_username_available import IsUsernameAvailable  # noqa: E501
from swagger_server.models.primary_account_details import PrimaryAccountDetails  # noqa: E501
from swagger_server.models.resend_verification_mail import ResendVerificationMail  # noqa: E501
from swagger_server.models.successful_authentication import SuccessfulAuthentication  # noqa: E501
from swagger_server.models.username import Username  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRegistrationController(BaseTestCase):
    """RegistrationController integration test stubs"""

    def test_register_change_verification_mail(self):
        """Test case for register_change_verification_mail

        Change the email linked with an account that is currently being registered.
        """
        body = ChangeVericationMailAddress()
        response = self.client.open(
            '/register/change_verification_email',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_finish_registration(self):
        """Test case for register_finish_registration

        Complete a users account
        """
        body = FinishRegistration()
        response = self.client.open(
            '/register/finish_registration',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_is_username_available(self):
        """Test case for register_is_username_available

        Check if a username is available
        """
        body = Username()
        response = self.client.open(
            '/register/is_username_available',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_resend_verification_mail(self):
        """Test case for register_resend_verification_mail

        Send another verification mail
        """
        body = ResendVerificationMail()
        response = self.client.open(
            '/register/resend_verification_mail',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_start_registration(self):
        """Test case for register_start_registration

        Reserve an account name and link it with an email
        """
        body = PrimaryAccountDetails()
        response = self.client.open(
            '/register/start_registration',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_verify_email_address(self):
        """Test case for register_verify_email_address

        Verify a users account email
        """
        body = EmailVerificationToken()
        response = self.client.open(
            '/register/verify_email_address',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
