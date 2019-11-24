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
from cloudmersive_image_api_client.api.convert_api import ConvertApi  # noqa: E501
from cloudmersive_image_api_client.rest import ApiException


class TestConvertApi(unittest.TestCase):
    """ConvertApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_image_api_client.api.convert_api.ConvertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_convert_to_gif(self):
        """Test case for convert_to_gif

        Convert input image to GIF format  # noqa: E501
        """
        pass

    def test_convert_to_jpg(self):
        """Test case for convert_to_jpg

        Convert input image to JPG/JPEG format  # noqa: E501
        """
        pass

    def test_convert_to_png(self):
        """Test case for convert_to_png

        Convert input image to PNG format  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
