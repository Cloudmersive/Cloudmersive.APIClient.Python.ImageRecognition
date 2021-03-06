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


class DrawRectangleRequest(object):
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
        'base_image_bytes': 'str',
        'base_image_url': 'str',
        'rectangles_to_draw': 'list[DrawRectangleInstance]'
    }

    attribute_map = {
        'base_image_bytes': 'BaseImageBytes',
        'base_image_url': 'BaseImageUrl',
        'rectangles_to_draw': 'RectanglesToDraw'
    }

    def __init__(self, base_image_bytes=None, base_image_url=None, rectangles_to_draw=None):  # noqa: E501
        """DrawRectangleRequest - a model defined in Swagger"""  # noqa: E501

        self._base_image_bytes = None
        self._base_image_url = None
        self._rectangles_to_draw = None
        self.discriminator = None

        if base_image_bytes is not None:
            self.base_image_bytes = base_image_bytes
        if base_image_url is not None:
            self.base_image_url = base_image_url
        if rectangles_to_draw is not None:
            self.rectangles_to_draw = rectangles_to_draw

    @property
    def base_image_bytes(self):
        """Gets the base_image_bytes of this DrawRectangleRequest.  # noqa: E501

        Image to draw rectangles on, in bytes.  You can also use the BaseImageUrl instead to supply image input as a URL  # noqa: E501

        :return: The base_image_bytes of this DrawRectangleRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_image_bytes

    @base_image_bytes.setter
    def base_image_bytes(self, base_image_bytes):
        """Sets the base_image_bytes of this DrawRectangleRequest.

        Image to draw rectangles on, in bytes.  You can also use the BaseImageUrl instead to supply image input as a URL  # noqa: E501

        :param base_image_bytes: The base_image_bytes of this DrawRectangleRequest.  # noqa: E501
        :type: str
        """
        if base_image_bytes is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', base_image_bytes):  # noqa: E501
            raise ValueError(r"Invalid value for `base_image_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._base_image_bytes = base_image_bytes

    @property
    def base_image_url(self):
        """Gets the base_image_url of this DrawRectangleRequest.  # noqa: E501

        Image to draw rectangles on, as an HTTP or HTTPS fully-qualified URL  # noqa: E501

        :return: The base_image_url of this DrawRectangleRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_image_url

    @base_image_url.setter
    def base_image_url(self, base_image_url):
        """Sets the base_image_url of this DrawRectangleRequest.

        Image to draw rectangles on, as an HTTP or HTTPS fully-qualified URL  # noqa: E501

        :param base_image_url: The base_image_url of this DrawRectangleRequest.  # noqa: E501
        :type: str
        """

        self._base_image_url = base_image_url

    @property
    def rectangles_to_draw(self):
        """Gets the rectangles_to_draw of this DrawRectangleRequest.  # noqa: E501

        Rectangles to draw on the image.  Rectangles are drawn in index order.  # noqa: E501

        :return: The rectangles_to_draw of this DrawRectangleRequest.  # noqa: E501
        :rtype: list[DrawRectangleInstance]
        """
        return self._rectangles_to_draw

    @rectangles_to_draw.setter
    def rectangles_to_draw(self, rectangles_to_draw):
        """Sets the rectangles_to_draw of this DrawRectangleRequest.

        Rectangles to draw on the image.  Rectangles are drawn in index order.  # noqa: E501

        :param rectangles_to_draw: The rectangles_to_draw of this DrawRectangleRequest.  # noqa: E501
        :type: list[DrawRectangleInstance]
        """

        self._rectangles_to_draw = rectangles_to_draw

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
        if issubclass(DrawRectangleRequest, dict):
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
        if not isinstance(other, DrawRectangleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
