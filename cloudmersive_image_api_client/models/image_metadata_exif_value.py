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


class ImageMetadataExifValue(object):
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
        'tag': 'str',
        'data_type': 'str',
        'data_value': 'str'
    }

    attribute_map = {
        'tag': 'Tag',
        'data_type': 'DataType',
        'data_value': 'DataValue'
    }

    def __init__(self, tag=None, data_type=None, data_value=None):  # noqa: E501
        """ImageMetadataExifValue - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._data_type = None
        self._data_value = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if data_type is not None:
            self.data_type = data_type
        if data_value is not None:
            self.data_value = data_value

    @property
    def tag(self):
        """Gets the tag of this ImageMetadataExifValue.  # noqa: E501

        Tag name for the EXIF value  # noqa: E501

        :return: The tag of this ImageMetadataExifValue.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ImageMetadataExifValue.

        Tag name for the EXIF value  # noqa: E501

        :param tag: The tag of this ImageMetadataExifValue.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def data_type(self):
        """Gets the data_type of this ImageMetadataExifValue.  # noqa: E501

        Date type of the EXIF value  # noqa: E501

        :return: The data_type of this ImageMetadataExifValue.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ImageMetadataExifValue.

        Date type of the EXIF value  # noqa: E501

        :param data_type: The data_type of this ImageMetadataExifValue.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def data_value(self):
        """Gets the data_value of this ImageMetadataExifValue.  # noqa: E501

        Value, formatted as a string of the EXIF value  # noqa: E501

        :return: The data_value of this ImageMetadataExifValue.  # noqa: E501
        :rtype: str
        """
        return self._data_value

    @data_value.setter
    def data_value(self, data_value):
        """Sets the data_value of this ImageMetadataExifValue.

        Value, formatted as a string of the EXIF value  # noqa: E501

        :param data_value: The data_value of this ImageMetadataExifValue.  # noqa: E501
        :type: str
        """

        self._data_value = data_value

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
        if issubclass(ImageMetadataExifValue, dict):
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
        if not isinstance(other, ImageMetadataExifValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
