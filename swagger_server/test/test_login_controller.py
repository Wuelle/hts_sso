# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.captcha_prompt import CaptchaPrompt  # noqa: E501
from swagger_server.models.init_login_session import InitLoginSession  # noqa: E501
from swagger_server.models.next_frame import NextFrame  # noqa: E501
from swagger_server.models.submitted_frame import SubmittedFrame  # noqa: E501
from swagger_server.models.successful_authentication import SuccessfulAuthentication  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoginController(BaseTestCase):
    """LoginController integration test stubs"""

    def test_login_init_session(self):
        """Test case for login_init_session

        Start logging in
        """
        body = InitLoginSession()
        response = self.client.open(
            '/login/init_session',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_submit_frame(self):
        """Test case for login_submit_frame

        Submit one of multiple credential frames
        """
        body = SubmittedFrame()
        response = self.client.open(
            '/login/submit_frame',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
