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

from cloudmersive_image_api_client.models.person_with_gender import PersonWithGender  # noqa: F401,E501


class GenderDetectionResult(object):
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
        'person_with_gender': 'list[PersonWithGender]',
        'people_identified': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'person_with_gender': 'PersonWithGender',
        'people_identified': 'PeopleIdentified'
    }

    def __init__(self, successful=None, person_with_gender=None, people_identified=None):  # noqa: E501
        """GenderDetectionResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._person_with_gender = None
        self._people_identified = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if person_with_gender is not None:
            self.person_with_gender = person_with_gender
        if people_identified is not None:
            self.people_identified = people_identified

    @property
    def successful(self):
        """Gets the successful of this GenderDetectionResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this GenderDetectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this GenderDetectionResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this GenderDetectionResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def person_with_gender(self):
        """Gets the person_with_gender of this GenderDetectionResult.  # noqa: E501

        People in the image annotated with gender information  # noqa: E501

        :return: The person_with_gender of this GenderDetectionResult.  # noqa: E501
        :rtype: list[PersonWithGender]
        """
        return self._person_with_gender

    @person_with_gender.setter
    def person_with_gender(self, person_with_gender):
        """Sets the person_with_gender of this GenderDetectionResult.

        People in the image annotated with gender information  # noqa: E501

        :param person_with_gender: The person_with_gender of this GenderDetectionResult.  # noqa: E501
        :type: list[PersonWithGender]
        """

        self._person_with_gender = person_with_gender

    @property
    def people_identified(self):
        """Gets the people_identified of this GenderDetectionResult.  # noqa: E501

        Number of people identified in the image with a gender  # noqa: E501

        :return: The people_identified of this GenderDetectionResult.  # noqa: E501
        :rtype: int
        """
        return self._people_identified

    @people_identified.setter
    def people_identified(self, people_identified):
        """Sets the people_identified of this GenderDetectionResult.

        Number of people identified in the image with a gender  # noqa: E501

        :param people_identified: The people_identified of this GenderDetectionResult.  # noqa: E501
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
        if issubclass(GenderDetectionResult, dict):
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
        if not isinstance(other, GenderDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other