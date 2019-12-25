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

from cloudmersive_image_api_client.models.face import Face  # noqa: F401,E501


class FaceLocateResponse(object):
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
        'faces': 'list[Face]',
        'face_count': 'int',
        'error_details': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'faces': 'Faces',
        'face_count': 'FaceCount',
        'error_details': 'ErrorDetails'
    }

    def __init__(self, successful=None, faces=None, face_count=None, error_details=None):  # noqa: E501
        """FaceLocateResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._faces = None
        self._face_count = None
        self._error_details = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if faces is not None:
            self.faces = faces
        if face_count is not None:
            self.face_count = face_count
        if error_details is not None:
            self.error_details = error_details

    @property
    def successful(self):
        """Gets the successful of this FaceLocateResponse.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this FaceLocateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this FaceLocateResponse.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this FaceLocateResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def faces(self):
        """Gets the faces of this FaceLocateResponse.  # noqa: E501

        Array of faces found in the image  # noqa: E501

        :return: The faces of this FaceLocateResponse.  # noqa: E501
        :rtype: list[Face]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this FaceLocateResponse.

        Array of faces found in the image  # noqa: E501

        :param faces: The faces of this FaceLocateResponse.  # noqa: E501
        :type: list[Face]
        """

        self._faces = faces

    @property
    def face_count(self):
        """Gets the face_count of this FaceLocateResponse.  # noqa: E501

        Number of faces found in the image  # noqa: E501

        :return: The face_count of this FaceLocateResponse.  # noqa: E501
        :rtype: int
        """
        return self._face_count

    @face_count.setter
    def face_count(self, face_count):
        """Sets the face_count of this FaceLocateResponse.

        Number of faces found in the image  # noqa: E501

        :param face_count: The face_count of this FaceLocateResponse.  # noqa: E501
        :type: int
        """

        self._face_count = face_count

    @property
    def error_details(self):
        """Gets the error_details of this FaceLocateResponse.  # noqa: E501

        Details of any errors that occurred  # noqa: E501

        :return: The error_details of this FaceLocateResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this FaceLocateResponse.

        Details of any errors that occurred  # noqa: E501

        :param error_details: The error_details of this FaceLocateResponse.  # noqa: E501
        :type: str
        """

        self._error_details = error_details

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
        if issubclass(FaceLocateResponse, dict):
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
        if not isinstance(other, FaceLocateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
