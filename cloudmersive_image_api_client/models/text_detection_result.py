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


class TextDetectionResult(object):
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
        'text_items': 'list[TextItem]',
        'text_items_count': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'text_items': 'TextItems',
        'text_items_count': 'TextItemsCount'
    }

    def __init__(self, successful=None, text_items=None, text_items_count=None):  # noqa: E501
        """TextDetectionResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._text_items = None
        self._text_items_count = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if text_items is not None:
            self.text_items = text_items
        if text_items_count is not None:
            self.text_items_count = text_items_count

    @property
    def successful(self):
        """Gets the successful of this TextDetectionResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this TextDetectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this TextDetectionResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this TextDetectionResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def text_items(self):
        """Gets the text_items of this TextDetectionResult.  # noqa: E501

        Text items found in the input image  # noqa: E501

        :return: The text_items of this TextDetectionResult.  # noqa: E501
        :rtype: list[TextItem]
        """
        return self._text_items

    @text_items.setter
    def text_items(self, text_items):
        """Sets the text_items of this TextDetectionResult.

        Text items found in the input image  # noqa: E501

        :param text_items: The text_items of this TextDetectionResult.  # noqa: E501
        :type: list[TextItem]
        """

        self._text_items = text_items

    @property
    def text_items_count(self):
        """Gets the text_items_count of this TextDetectionResult.  # noqa: E501

        Count of text items found in the input image  # noqa: E501

        :return: The text_items_count of this TextDetectionResult.  # noqa: E501
        :rtype: int
        """
        return self._text_items_count

    @text_items_count.setter
    def text_items_count(self, text_items_count):
        """Sets the text_items_count of this TextDetectionResult.

        Count of text items found in the input image  # noqa: E501

        :param text_items_count: The text_items_count of this TextDetectionResult.  # noqa: E501
        :type: int
        """

        self._text_items_count = text_items_count

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
        if issubclass(TextDetectionResult, dict):
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
        if not isinstance(other, TextDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
