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

from cloudmersive_image_api_client.models.face_point import FacePoint  # noqa: F401,E501


class FaceWithLandmarks(object):
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
        'left_eyebrow': 'list[FacePoint]',
        'right_eyebrow': 'list[FacePoint]',
        'left_eye': 'list[FacePoint]',
        'right_eye': 'list[FacePoint]',
        'bottom_and_sides_of_face': 'list[FacePoint]',
        'nose_bridge': 'list[FacePoint]',
        'nose_bottom': 'list[FacePoint]',
        'lips_inner_outline': 'list[FacePoint]',
        'lips_outer_outline': 'list[FacePoint]',
        'left_x': 'int',
        'top_y': 'int',
        'right_x': 'int',
        'bottom_y': 'int'
    }

    attribute_map = {
        'left_eyebrow': 'LeftEyebrow',
        'right_eyebrow': 'RightEyebrow',
        'left_eye': 'LeftEye',
        'right_eye': 'RightEye',
        'bottom_and_sides_of_face': 'BottomAndSidesOfFace',
        'nose_bridge': 'NoseBridge',
        'nose_bottom': 'NoseBottom',
        'lips_inner_outline': 'LipsInnerOutline',
        'lips_outer_outline': 'LipsOuterOutline',
        'left_x': 'LeftX',
        'top_y': 'TopY',
        'right_x': 'RightX',
        'bottom_y': 'BottomY'
    }

    def __init__(self, left_eyebrow=None, right_eyebrow=None, left_eye=None, right_eye=None, bottom_and_sides_of_face=None, nose_bridge=None, nose_bottom=None, lips_inner_outline=None, lips_outer_outline=None, left_x=None, top_y=None, right_x=None, bottom_y=None):  # noqa: E501
        """FaceWithLandmarks - a model defined in Swagger"""  # noqa: E501

        self._left_eyebrow = None
        self._right_eyebrow = None
        self._left_eye = None
        self._right_eye = None
        self._bottom_and_sides_of_face = None
        self._nose_bridge = None
        self._nose_bottom = None
        self._lips_inner_outline = None
        self._lips_outer_outline = None
        self._left_x = None
        self._top_y = None
        self._right_x = None
        self._bottom_y = None
        self.discriminator = None

        if left_eyebrow is not None:
            self.left_eyebrow = left_eyebrow
        if right_eyebrow is not None:
            self.right_eyebrow = right_eyebrow
        if left_eye is not None:
            self.left_eye = left_eye
        if right_eye is not None:
            self.right_eye = right_eye
        if bottom_and_sides_of_face is not None:
            self.bottom_and_sides_of_face = bottom_and_sides_of_face
        if nose_bridge is not None:
            self.nose_bridge = nose_bridge
        if nose_bottom is not None:
            self.nose_bottom = nose_bottom
        if lips_inner_outline is not None:
            self.lips_inner_outline = lips_inner_outline
        if lips_outer_outline is not None:
            self.lips_outer_outline = lips_outer_outline
        if left_x is not None:
            self.left_x = left_x
        if top_y is not None:
            self.top_y = top_y
        if right_x is not None:
            self.right_x = right_x
        if bottom_y is not None:
            self.bottom_y = bottom_y

    @property
    def left_eyebrow(self):
        """Gets the left_eyebrow of this FaceWithLandmarks.  # noqa: E501


        :return: The left_eyebrow of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._left_eyebrow

    @left_eyebrow.setter
    def left_eyebrow(self, left_eyebrow):
        """Sets the left_eyebrow of this FaceWithLandmarks.


        :param left_eyebrow: The left_eyebrow of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._left_eyebrow = left_eyebrow

    @property
    def right_eyebrow(self):
        """Gets the right_eyebrow of this FaceWithLandmarks.  # noqa: E501


        :return: The right_eyebrow of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._right_eyebrow

    @right_eyebrow.setter
    def right_eyebrow(self, right_eyebrow):
        """Sets the right_eyebrow of this FaceWithLandmarks.


        :param right_eyebrow: The right_eyebrow of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._right_eyebrow = right_eyebrow

    @property
    def left_eye(self):
        """Gets the left_eye of this FaceWithLandmarks.  # noqa: E501


        :return: The left_eye of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._left_eye

    @left_eye.setter
    def left_eye(self, left_eye):
        """Sets the left_eye of this FaceWithLandmarks.


        :param left_eye: The left_eye of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._left_eye = left_eye

    @property
    def right_eye(self):
        """Gets the right_eye of this FaceWithLandmarks.  # noqa: E501


        :return: The right_eye of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._right_eye

    @right_eye.setter
    def right_eye(self, right_eye):
        """Sets the right_eye of this FaceWithLandmarks.


        :param right_eye: The right_eye of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._right_eye = right_eye

    @property
    def bottom_and_sides_of_face(self):
        """Gets the bottom_and_sides_of_face of this FaceWithLandmarks.  # noqa: E501


        :return: The bottom_and_sides_of_face of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._bottom_and_sides_of_face

    @bottom_and_sides_of_face.setter
    def bottom_and_sides_of_face(self, bottom_and_sides_of_face):
        """Sets the bottom_and_sides_of_face of this FaceWithLandmarks.


        :param bottom_and_sides_of_face: The bottom_and_sides_of_face of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._bottom_and_sides_of_face = bottom_and_sides_of_face

    @property
    def nose_bridge(self):
        """Gets the nose_bridge of this FaceWithLandmarks.  # noqa: E501


        :return: The nose_bridge of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._nose_bridge

    @nose_bridge.setter
    def nose_bridge(self, nose_bridge):
        """Sets the nose_bridge of this FaceWithLandmarks.


        :param nose_bridge: The nose_bridge of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._nose_bridge = nose_bridge

    @property
    def nose_bottom(self):
        """Gets the nose_bottom of this FaceWithLandmarks.  # noqa: E501


        :return: The nose_bottom of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._nose_bottom

    @nose_bottom.setter
    def nose_bottom(self, nose_bottom):
        """Sets the nose_bottom of this FaceWithLandmarks.


        :param nose_bottom: The nose_bottom of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._nose_bottom = nose_bottom

    @property
    def lips_inner_outline(self):
        """Gets the lips_inner_outline of this FaceWithLandmarks.  # noqa: E501


        :return: The lips_inner_outline of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._lips_inner_outline

    @lips_inner_outline.setter
    def lips_inner_outline(self, lips_inner_outline):
        """Sets the lips_inner_outline of this FaceWithLandmarks.


        :param lips_inner_outline: The lips_inner_outline of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._lips_inner_outline = lips_inner_outline

    @property
    def lips_outer_outline(self):
        """Gets the lips_outer_outline of this FaceWithLandmarks.  # noqa: E501


        :return: The lips_outer_outline of this FaceWithLandmarks.  # noqa: E501
        :rtype: list[FacePoint]
        """
        return self._lips_outer_outline

    @lips_outer_outline.setter
    def lips_outer_outline(self, lips_outer_outline):
        """Sets the lips_outer_outline of this FaceWithLandmarks.


        :param lips_outer_outline: The lips_outer_outline of this FaceWithLandmarks.  # noqa: E501
        :type: list[FacePoint]
        """

        self._lips_outer_outline = lips_outer_outline

    @property
    def left_x(self):
        """Gets the left_x of this FaceWithLandmarks.  # noqa: E501

        X coordinate of the left side of the face  # noqa: E501

        :return: The left_x of this FaceWithLandmarks.  # noqa: E501
        :rtype: int
        """
        return self._left_x

    @left_x.setter
    def left_x(self, left_x):
        """Sets the left_x of this FaceWithLandmarks.

        X coordinate of the left side of the face  # noqa: E501

        :param left_x: The left_x of this FaceWithLandmarks.  # noqa: E501
        :type: int
        """

        self._left_x = left_x

    @property
    def top_y(self):
        """Gets the top_y of this FaceWithLandmarks.  # noqa: E501

        Y coordinate of the top side of the face  # noqa: E501

        :return: The top_y of this FaceWithLandmarks.  # noqa: E501
        :rtype: int
        """
        return self._top_y

    @top_y.setter
    def top_y(self, top_y):
        """Sets the top_y of this FaceWithLandmarks.

        Y coordinate of the top side of the face  # noqa: E501

        :param top_y: The top_y of this FaceWithLandmarks.  # noqa: E501
        :type: int
        """

        self._top_y = top_y

    @property
    def right_x(self):
        """Gets the right_x of this FaceWithLandmarks.  # noqa: E501

        X coordinate of the right side of the face  # noqa: E501

        :return: The right_x of this FaceWithLandmarks.  # noqa: E501
        :rtype: int
        """
        return self._right_x

    @right_x.setter
    def right_x(self, right_x):
        """Sets the right_x of this FaceWithLandmarks.

        X coordinate of the right side of the face  # noqa: E501

        :param right_x: The right_x of this FaceWithLandmarks.  # noqa: E501
        :type: int
        """

        self._right_x = right_x

    @property
    def bottom_y(self):
        """Gets the bottom_y of this FaceWithLandmarks.  # noqa: E501

        Y coordinate of the bottom side of the face  # noqa: E501

        :return: The bottom_y of this FaceWithLandmarks.  # noqa: E501
        :rtype: int
        """
        return self._bottom_y

    @bottom_y.setter
    def bottom_y(self, bottom_y):
        """Sets the bottom_y of this FaceWithLandmarks.

        Y coordinate of the bottom side of the face  # noqa: E501

        :param bottom_y: The bottom_y of this FaceWithLandmarks.  # noqa: E501
        :type: int
        """

        self._bottom_y = bottom_y

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FaceWithLandmarks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
