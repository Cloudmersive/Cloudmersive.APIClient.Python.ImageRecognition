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


class ColorResult(object):
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
        'r': 'int',
        'g': 'int',
        'b': 'int'
    }

    attribute_map = {
        'r': 'R',
        'g': 'G',
        'b': 'B'
    }

    def __init__(self, r=None, g=None, b=None):  # noqa: E501
        """ColorResult - a model defined in Swagger"""  # noqa: E501

        self._r = None
        self._g = None
        self._b = None
        self.discriminator = None

        if r is not None:
            self.r = r
        if g is not None:
            self.g = g
        if b is not None:
            self.b = b

    @property
    def r(self):
        """Gets the r of this ColorResult.  # noqa: E501

        Red (R) channel pixel value of this color  # noqa: E501

        :return: The r of this ColorResult.  # noqa: E501
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this ColorResult.

        Red (R) channel pixel value of this color  # noqa: E501

        :param r: The r of this ColorResult.  # noqa: E501
        :type: int
        """

        self._r = r

    @property
    def g(self):
        """Gets the g of this ColorResult.  # noqa: E501

        Green (G) channel pixel value of this color  # noqa: E501

        :return: The g of this ColorResult.  # noqa: E501
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this ColorResult.

        Green (G) channel pixel value of this color  # noqa: E501

        :param g: The g of this ColorResult.  # noqa: E501
        :type: int
        """

        self._g = g

    @property
    def b(self):
        """Gets the b of this ColorResult.  # noqa: E501

        Blue (B) channel pixel value of this color  # noqa: E501

        :return: The b of this ColorResult.  # noqa: E501
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this ColorResult.

        Blue (B) channel pixel value of this color  # noqa: E501

        :param b: The b of this ColorResult.  # noqa: E501
        :type: int
        """

        self._b = b

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
        if issubclass(ColorResult, dict):
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
        if not isinstance(other, ColorResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
