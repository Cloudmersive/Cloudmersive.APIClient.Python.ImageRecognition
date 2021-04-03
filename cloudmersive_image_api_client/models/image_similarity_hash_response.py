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


class ImageSimilarityHashResponse(object):
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
        'successful': 'bool',
        'image_hash': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'image_hash': 'ImageHash'
    }

    def __init__(self, successful=None, image_hash=None):  # noqa: E501
        """ImageSimilarityHashResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._image_hash = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if image_hash is not None:
            self.image_hash = image_hash

    @property
    def successful(self):
        """Gets the successful of this ImageSimilarityHashResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this ImageSimilarityHashResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ImageSimilarityHashResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this ImageSimilarityHashResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def image_hash(self):
        """Gets the image_hash of this ImageSimilarityHashResponse.  # noqa: E501

        String representing image perceptual hash value; values with smaller Hamming Distances are more similar than ones with large Hamming Distances  # noqa: E501

        :return: The image_hash of this ImageSimilarityHashResponse.  # noqa: E501
        :rtype: str
        """
        return self._image_hash

    @image_hash.setter
    def image_hash(self, image_hash):
        """Sets the image_hash of this ImageSimilarityHashResponse.

        String representing image perceptual hash value; values with smaller Hamming Distances are more similar than ones with large Hamming Distances  # noqa: E501

        :param image_hash: The image_hash of this ImageSimilarityHashResponse.  # noqa: E501
        :type: str
        """

        self._image_hash = image_hash

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
        if issubclass(ImageSimilarityHashResponse, dict):
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
        if not isinstance(other, ImageSimilarityHashResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
