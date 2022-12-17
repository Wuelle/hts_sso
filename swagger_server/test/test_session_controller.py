# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.nonce_token2 import NonceToken2  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSessionController(BaseTestCase):
    """SessionController integration test stubs"""

    def test_session_get_nonce_token(self):
        """Test case for session_get_nonce_token

        Get a nonce
        """
        query_string = [('area', 'area_example')]
        response = self.client.open(
            '/session/get_nonce_token',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
