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
from cloudmersive_image_api_client.api.resize_api import ResizeApi  # noqa: E501
from cloudmersive_image_api_client.rest import ApiException


class TestResizeApi(unittest.TestCase):
    """ResizeApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_image_api_client.api.resize_api.ResizeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_resize_post(self):
        """Test case for resize_post

        Resize an image with parameters  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
