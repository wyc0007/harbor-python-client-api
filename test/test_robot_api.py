"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import harbor_client
from harbor_client.api.robot_api import RobotApi  # noqa: E501


class TestRobotApi(unittest.TestCase):
    """RobotApi unit test stubs"""

    def setUp(self):
        self.api = RobotApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_robot(self):
        """Test case for create_robot

        Create a robot account  # noqa: E501
        """
        pass

    def test_delete_robot(self):
        """Test case for delete_robot

        Delete a robot account  # noqa: E501
        """
        pass

    def test_get_robot_by_id(self):
        """Test case for get_robot_by_id

        Get a robot account  # noqa: E501
        """
        pass

    def test_list_robot(self):
        """Test case for list_robot

        Get robot account  # noqa: E501
        """
        pass

    def test_refresh_sec(self):
        """Test case for refresh_sec

        Refresh the robot secret  # noqa: E501
        """
        pass

    def test_update_robot(self):
        """Test case for update_robot

        Update a robot account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
