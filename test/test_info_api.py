# coding: utf-8

"""
    imageapi

    Image Recognition and Processing APIs let you use Machine Learning to recognize and process images, and also perform useful image modification operations.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_image_api_client
from cloudmersive_image_api_client.api.info_api import InfoApi  # noqa: E501
from cloudmersive_image_api_client.rest import ApiException


class TestInfoApi(unittest.TestCase):
    """InfoApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_image_api_client.api.info_api.InfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_info_get_dominant_color(self):
        """Test case for info_get_dominant_color

        Returns the dominant colors of the image  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
