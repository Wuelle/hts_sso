# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.captcha_prompt import CaptchaPrompt  # noqa: E501
from swagger_server.models.login_body import LoginBody  # noqa: E501
from swagger_server.models.next_frame import NextFrame  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_login_start_reauth(self):
        """Test case for login_start_reauth

        Reauthenticate a user in case their session expired, without needing to enter the username again
        """
        query_string = [('redirect', 'redirect_example'),
                        ('username', 'username_example')]
        response = self.client.open(
            '/reauth',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_start_session(self):
        """Test case for login_start_session

        Start logging in
        """
        query_string = [('redirect', 'redirect_example')]
        response = self.client.open(
            '/login',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_submit_frame(self):
        """Test case for login_submit_frame

        Submit one of multiple credential frames
        """
        body = LoginBody()
        response = self.client.open(
            '/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
