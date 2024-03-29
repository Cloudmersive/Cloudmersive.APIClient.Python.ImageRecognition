# coding: utf-8

"""
    imageapi

    Image Recognition and Processing APIs let you use Machine Learning to recognize and process images, and also perform useful image modification operations.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ImageSimilarityHashDistanceRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_hash1': 'str',
        'image_hash2': 'str'
    }

    attribute_map = {
        'image_hash1': 'ImageHash1',
        'image_hash2': 'ImageHash2'
    }

    def __init__(self, image_hash1=None, image_hash2=None):  # noqa: E501
        """ImageSimilarityHashDistanceRequest - a model defined in Swagger"""  # noqa: E501

        self._image_hash1 = None
        self._image_hash2 = None
        self.discriminator = None

        if image_hash1 is not None:
            self.image_hash1 = image_hash1
        if image_hash2 is not None:
            self.image_hash2 = image_hash2

    @property
    def image_hash1(self):
        """Gets the image_hash1 of this ImageSimilarityHashDistanceRequest.  # noqa: E501

        Image hash computed using Cloudmersive Image Hashing API  # noqa: E501

        :return: The image_hash1 of this ImageSimilarityHashDistanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_hash1

    @image_hash1.setter
    def image_hash1(self, image_hash1):
        """Sets the image_hash1 of this ImageSimilarityHashDistanceRequest.

        Image hash computed using Cloudmersive Image Hashing API  # noqa: E501

        :param image_hash1: The image_hash1 of this ImageSimilarityHashDistanceRequest.  # noqa: E501
        :type: str
        """

        self._image_hash1 = image_hash1

    @property
    def image_hash2(self):
        """Gets the image_hash2 of this ImageSimilarityHashDistanceRequest.  # noqa: E501

        Image hash computed using Cloudmersive Image Hashing API  # noqa: E501

        :return: The image_hash2 of this ImageSimilarityHashDistanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_hash2

    @image_hash2.setter
    def image_hash2(self, image_hash2):
        """Sets the image_hash2 of this ImageSimilarityHashDistanceRequest.

        Image hash computed using Cloudmersive Image Hashing API  # noqa: E501

        :param image_hash2: The image_hash2 of this ImageSimilarityHashDistanceRequest.  # noqa: E501
        :type: str
        """

        self._image_hash2 = image_hash2

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImageSimilarityHashDistanceRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageSimilarityHashDistanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
