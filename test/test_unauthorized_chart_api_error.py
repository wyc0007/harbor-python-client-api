"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.chart_api_error import ChartAPIError
globals()['ChartAPIError'] = ChartAPIError
from harbor_client.model.unauthorized_chart_api_error import UnauthorizedChartAPIError


class TestUnauthorizedChartAPIError(unittest.TestCase):
    """UnauthorizedChartAPIError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUnauthorizedChartAPIError(self):
        """Test UnauthorizedChartAPIError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UnauthorizedChartAPIError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
