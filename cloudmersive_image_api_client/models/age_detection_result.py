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

from cloudmersive_image_api_client.models.person_with_age import PersonWithAge  # noqa: F401,E501


class AgeDetectionResult(object):
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
        'people_with_age': 'list[PersonWithAge]',
        'people_identified': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'people_with_age': 'PeopleWithAge',
        'people_identified': 'PeopleIdentified'
    }

    def __init__(self, successful=None, people_with_age=None, people_identified=None):  # noqa: E501
        """AgeDetectionResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._people_with_age = None
        self._people_identified = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if people_with_age is not None:
            self.people_with_age = people_with_age
        if people_identified is not None:
            self.people_identified = people_identified

    @property
    def successful(self):
        """Gets the successful of this AgeDetectionResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this AgeDetectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this AgeDetectionResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this AgeDetectionResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def people_with_age(self):
        """Gets the people_with_age of this AgeDetectionResult.  # noqa: E501

        People in the image annotated with age information  # noqa: E501

        :return: The people_with_age of this AgeDetectionResult.  # noqa: E501
        :rtype: list[PersonWithAge]
        """
        return self._people_with_age

    @people_with_age.setter
    def people_with_age(self, people_with_age):
        """Sets the people_with_age of this AgeDetectionResult.

        People in the image annotated with age information  # noqa: E501

        :param people_with_age: The people_with_age of this AgeDetectionResult.  # noqa: E501
        :type: list[PersonWithAge]
        """

        self._people_with_age = people_with_age

    @property
    def people_identified(self):
        """Gets the people_identified of this AgeDetectionResult.  # noqa: E501

        Number of people identified in the image with an age  # noqa: E501

        :return: The people_identified of this AgeDetectionResult.  # noqa: E501
        :rtype: int
        """
        return self._people_identified

    @people_identified.setter
    def people_identified(self, people_identified):
        """Sets the people_identified of this AgeDetectionResult.

        Number of people identified in the image with an age  # noqa: E501

        :param people_identified: The people_identified of this AgeDetectionResult.  # noqa: E501
        :type: int
        """

        self._people_identified = people_identified

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
        if not isinstance(other, AgeDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
