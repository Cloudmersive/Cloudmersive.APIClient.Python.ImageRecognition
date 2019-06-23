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


class RecognitionOutcome(object):
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
        'confidence_score': 'float',
        'description': 'str'
    }

    attribute_map = {
        'confidence_score': 'ConfidenceScore',
        'description': 'Description'
    }

    def __init__(self, confidence_score=None, description=None):  # noqa: E501
        """RecognitionOutcome - a model defined in Swagger"""  # noqa: E501

        self._confidence_score = None
        self._description = None
        self.discriminator = None

        if confidence_score is not None:
            self.confidence_score = confidence_score
        if description is not None:
            self.description = description

    @property
    def confidence_score(self):
        """Gets the confidence_score of this RecognitionOutcome.  # noqa: E501

        Scores closer to 1 are better than scores closer to 0  # noqa: E501

        :return: The confidence_score of this RecognitionOutcome.  # noqa: E501
        :rtype: float
        """
        return self._confidence_score

    @confidence_score.setter
    def confidence_score(self, confidence_score):
        """Sets the confidence_score of this RecognitionOutcome.

        Scores closer to 1 are better than scores closer to 0  # noqa: E501

        :param confidence_score: The confidence_score of this RecognitionOutcome.  # noqa: E501
        :type: float
        """

        self._confidence_score = confidence_score

    @property
    def description(self):
        """Gets the description of this RecognitionOutcome.  # noqa: E501

        English language description of the image  # noqa: E501

        :return: The description of this RecognitionOutcome.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecognitionOutcome.

        English language description of the image  # noqa: E501

        :param description: The description of this RecognitionOutcome.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(RecognitionOutcome, dict):
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
        if not isinstance(other, RecognitionOutcome):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
