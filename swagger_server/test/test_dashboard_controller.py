# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dashboard_get_user_info_body import DashboardGetUserInfoBody  # noqa: E501
from swagger_server.models.dashboard_info_container import DashboardInfoContainer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDashboardController(BaseTestCase):
    """DashboardController integration test stubs"""

    def test_dashboard_get_user_info(self):
        """Test case for dashboard_get_user_info

        Get a users account data
        """
        body = DashboardGetUserInfoBody()
        response = self.client.open(
            '/dashboard/get_user_info',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
