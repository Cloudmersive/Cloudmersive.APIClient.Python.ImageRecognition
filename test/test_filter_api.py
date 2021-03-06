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
from cloudmersive_image_api_client.api.filter_api import FilterApi  # noqa: E501
from cloudmersive_image_api_client.rest import ApiException


class TestFilterApi(unittest.TestCase):
    """FilterApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_image_api_client.api.filter_api.FilterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_filter_black_and_white(self):
        """Test case for filter_black_and_white

        Convert image to black-and-white grayscale  # noqa: E501
        """
        pass

    def test_filter_despeckle(self):
        """Test case for filter_despeckle

        Despeckle (remove point noise) from the image  # noqa: E501
        """
        pass

    def test_filter_edge_detect(self):
        """Test case for filter_edge_detect

        Detect and highlight edges in an image  # noqa: E501
        """
        pass

    def test_filter_emboss(self):
        """Test case for filter_emboss

        Emboss an image  # noqa: E501
        """
        pass

    def test_filter_gaussian_blur(self):
        """Test case for filter_gaussian_blur

        Perform a guassian blur on the input image  # noqa: E501
        """
        pass

    def test_filter_motion_blur(self):
        """Test case for filter_motion_blur

        Perform a motion blur on the input image  # noqa: E501
        """
        pass

    def test_filter_posterize(self):
        """Test case for filter_posterize

        Posterize the image by reducing distinct colors  # noqa: E501
        """
        pass

    def test_filter_swirl(self):
        """Test case for filter_swirl

        Swirl distort the image  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
