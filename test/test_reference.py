"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import harbor_client
from harbor_client.model.annotations import Annotations
from harbor_client.model.platform import Platform
globals()['Annotations'] = Annotations
globals()['Platform'] = Platform
from harbor_client.model.reference import Reference


class TestReference(unittest.TestCase):
    """Reference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReference(self):
        """Test Reference"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Reference()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
