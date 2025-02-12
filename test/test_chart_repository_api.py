"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.chart_repository_api import ChartRepositoryApi  # noqa: E501


class TestChartRepositoryApi(unittest.TestCase):
    """ChartRepositoryApi unit test stubs"""

    def setUp(self):
        self.api = ChartRepositoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chartrepo_repo_charts_name_version_labels_get(self):
        """Test case for chartrepo_repo_charts_name_version_labels_get

        Return the attahced labels of chart.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_labels_id_delete(self):
        """Test case for chartrepo_repo_charts_name_version_labels_id_delete

        Remove label from chart.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_labels_post(self):
        """Test case for chartrepo_repo_charts_name_version_labels_post

        Mark label to chart.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
