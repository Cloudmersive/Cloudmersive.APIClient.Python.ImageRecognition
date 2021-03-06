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


class TextItem(object):
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
        'left_x': 'int',
        'top_y': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'left_x': 'LeftX',
        'top_y': 'TopY',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, left_x=None, top_y=None, width=None, height=None):  # noqa: E501
        """TextItem - a model defined in Swagger"""  # noqa: E501

        self._left_x = None
        self._top_y = None
        self._width = None
        self._height = None
        self.discriminator = None

        if left_x is not None:
            self.left_x = left_x
        if top_y is not None:
            self.top_y = top_y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def left_x(self):
        """Gets the left_x of this TextItem.  # noqa: E501

        Left X coordinate of the text location; 0 represents the left edge of the input image  # noqa: E501

        :return: The left_x of this TextItem.  # noqa: E501
        :rtype: int
        """
        return self._left_x

    @left_x.setter
    def left_x(self, left_x):
        """Sets the left_x of this TextItem.

        Left X coordinate of the text location; 0 represents the left edge of the input image  # noqa: E501

        :param left_x: The left_x of this TextItem.  # noqa: E501
        :type: int
        """

        self._left_x = left_x

    @property
    def top_y(self):
        """Gets the top_y of this TextItem.  # noqa: E501

        Top Y coordinate of the text location; 0 represents the top edge of the input image  # noqa: E501

        :return: The top_y of this TextItem.  # noqa: E501
        :rtype: int
        """
        return self._top_y

    @top_y.setter
    def top_y(self, top_y):
        """Sets the top_y of this TextItem.

        Top Y coordinate of the text location; 0 represents the top edge of the input image  # noqa: E501

        :param top_y: The top_y of this TextItem.  # noqa: E501
        :type: int
        """

        self._top_y = top_y

    @property
    def width(self):
        """Gets the width of this TextItem.  # noqa: E501

        Width in pixels of the text item  # noqa: E501

        :return: The width of this TextItem.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TextItem.

        Width in pixels of the text item  # noqa: E501

        :param width: The width of this TextItem.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this TextItem.  # noqa: E501

        Height in pixels of the text item  # noqa: E501

        :return: The height of this TextItem.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TextItem.

        Height in pixels of the text item  # noqa: E501

        :param height: The height of this TextItem.  # noqa: E501
        :type: int
        """

        self._height = height

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
        if issubclass(TextItem, dict):
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
        if not isinstance(other, TextItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
