# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.nonce_token1 import NonceToken1  # noqa: E501
from swagger_server.models.nonce_token2 import NonceToken2  # noqa: E501
from swagger_server.models.nonce_token3 import NonceToken3  # noqa: E501
from swagger_server.models.nonce_token4 import NonceToken4  # noqa: E501
from swagger_server.models.nonce_token5 import NonceToken5  # noqa: E501
from swagger_server.models.passphrase_update_token import PassphraseUpdateToken  # noqa: E501
from swagger_server.models.request_passphrase_reset_token import RequestPassphraseResetToken  # noqa: E501
from swagger_server.models.request_username_reminder import RequestUsernameReminder  # noqa: E501
from swagger_server.models.submit_captcha_token import SubmitCaptchaToken  # noqa: E501
from swagger_server.models.update_passphrase import UpdatePassphrase  # noqa: E501
from swagger_server.models.update_passphrase1 import UpdatePassphrase1  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountRecoveryController(BaseTestCase):
    """AccountRecoveryController integration test stubs"""

    def test_account_recovery_request_passphrase_reset_token(self):
        """Test case for account_recovery_request_passphrase_reset_token

        
        """
        body = RequestPassphraseResetToken()
        response = self.client.open(
            '/account_recovery/request_passphrase_update_token',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_recovery_request_username_reminder(self):
        """Test case for account_recovery_request_username_reminder

        Send a username reminder mail
        """
        body = RequestUsernameReminder()
        response = self.client.open(
            '/account_recovery/request_username_reminder',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_recovery_submit_captcha_token(self):
        """Test case for account_recovery_submit_captcha_token

        Prove that the user completed a captcha
        """
        body = SubmitCaptchaToken()
        response = self.client.open(
            '/account_recovery/submit_captcha_token',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_recovery_submit_passphrase_update_token(self):
        """Test case for account_recovery_submit_passphrase_update_token

        
        """
        body = PassphraseUpdateToken()
        response = self.client.open(
            '/account_recovery/submit_passphrase_update_token',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_recovery_submit_secret_answer(self):
        """Test case for account_recovery_submit_secret_answer

        
        """
        body = UpdatePassphrase1()
        response = self.client.open(
            '/account_recovery/submit_secret_answer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_recovery_update_passphrase(self):
        """Test case for account_recovery_update_passphrase

        
        """
        body = UpdatePassphrase()
        response = self.client.open(
            '/account_recovery/update_passphrase',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
