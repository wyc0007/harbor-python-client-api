"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.system_cve_allowlist_api import SystemCVEAllowlistApi  # noqa: E501


class TestSystemCVEAllowlistApi(unittest.TestCase):
    """SystemCVEAllowlistApi unit test stubs"""

    def setUp(self):
        self.api = SystemCVEAllowlistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_cve_allowlist(self):
        """Test case for get_system_cve_allowlist

        Get the system level allowlist of CVE.  # noqa: E501
        """
        pass

    def test_put_system_cve_allowlist(self):
        """Test case for put_system_cve_allowlist

        Update the system level allowlist of CVE.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
