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


class FindSymbolResult(object):
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
        'match_score': 'float',
        'x_left': 'int',
        'y_top': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'match_score': 'MatchScore',
        'x_left': 'XLeft',
        'y_top': 'YTop',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, successful=None, match_score=None, x_left=None, y_top=None, width=None, height=None):  # noqa: E501
        """FindSymbolResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._match_score = None
        self._x_left = None
        self._y_top = None
        self._width = None
        self._height = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if match_score is not None:
            self.match_score = match_score
        if x_left is not None:
            self.x_left = x_left
        if y_top is not None:
            self.y_top = y_top
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def successful(self):
        """Gets the successful of this FindSymbolResult.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this FindSymbolResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this FindSymbolResult.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this FindSymbolResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def match_score(self):
        """Gets the match_score of this FindSymbolResult.  # noqa: E501

        Score between 0.0 and 1.0 that measures how closely the symbol matched; scores above 0.2 are good  # noqa: E501

        :return: The match_score of this FindSymbolResult.  # noqa: E501
        :rtype: float
        """
        return self._match_score

    @match_score.setter
    def match_score(self, match_score):
        """Sets the match_score of this FindSymbolResult.

        Score between 0.0 and 1.0 that measures how closely the symbol matched; scores above 0.2 are good  # noqa: E501

        :param match_score: The match_score of this FindSymbolResult.  # noqa: E501
        :type: float
        """

        self._match_score = match_score

    @property
    def x_left(self):
        """Gets the x_left of this FindSymbolResult.  # noqa: E501

        X location of the left edge of the found location in pixels  # noqa: E501

        :return: The x_left of this FindSymbolResult.  # noqa: E501
        :rtype: int
        """
        return self._x_left

    @x_left.setter
    def x_left(self, x_left):
        """Sets the x_left of this FindSymbolResult.

        X location of the left edge of the found location in pixels  # noqa: E501

        :param x_left: The x_left of this FindSymbolResult.  # noqa: E501
        :type: int
        """

        self._x_left = x_left

    @property
    def y_top(self):
        """Gets the y_top of this FindSymbolResult.  # noqa: E501

        Y location of the top edge of the found location in pixels  # noqa: E501

        :return: The y_top of this FindSymbolResult.  # noqa: E501
        :rtype: int
        """
        return self._y_top

    @y_top.setter
    def y_top(self, y_top):
        """Sets the y_top of this FindSymbolResult.

        Y location of the top edge of the found location in pixels  # noqa: E501

        :param y_top: The y_top of this FindSymbolResult.  # noqa: E501
        :type: int
        """

        self._y_top = y_top

    @property
    def width(self):
        """Gets the width of this FindSymbolResult.  # noqa: E501

        Width of the found location in pixels  # noqa: E501

        :return: The width of this FindSymbolResult.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this FindSymbolResult.

        Width of the found location in pixels  # noqa: E501

        :param width: The width of this FindSymbolResult.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this FindSymbolResult.  # noqa: E501

        Height of the found location in pixels  # noqa: E501

        :return: The height of this FindSymbolResult.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this FindSymbolResult.

        Height of the found location in pixels  # noqa: E501

        :param height: The height of this FindSymbolResult.  # noqa: E501
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
        if issubclass(FindSymbolResult, dict):
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
        if not isinstance(other, FindSymbolResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
