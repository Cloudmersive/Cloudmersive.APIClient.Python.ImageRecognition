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


class ImageSimilarityComparisonResponse(object):
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
        'are_images_similar': 'bool',
        'image_similarity_score': 'float'
    }

    attribute_map = {
        'successful': 'Successful',
        'are_images_similar': 'AreImagesSimilar',
        'image_similarity_score': 'ImageSimilarityScore'
    }

    def __init__(self, successful=None, are_images_similar=None, image_similarity_score=None):  # noqa: E501
        """ImageSimilarityComparisonResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._are_images_similar = None
        self._image_similarity_score = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if are_images_similar is not None:
            self.are_images_similar = are_images_similar
        if image_similarity_score is not None:
            self.image_similarity_score = image_similarity_score

    @property
    def successful(self):
        """Gets the successful of this ImageSimilarityComparisonResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this ImageSimilarityComparisonResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ImageSimilarityComparisonResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this ImageSimilarityComparisonResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def are_images_similar(self):
        """Gets the are_images_similar of this ImageSimilarityComparisonResponse.  # noqa: E501

        True if images are similar, false otherwise  # noqa: E501

        :return: The are_images_similar of this ImageSimilarityComparisonResponse.  # noqa: E501
        :rtype: bool
        """
        return self._are_images_similar

    @are_images_similar.setter
    def are_images_similar(self, are_images_similar):
        """Sets the are_images_similar of this ImageSimilarityComparisonResponse.

        True if images are similar, false otherwise  # noqa: E501

        :param are_images_similar: The are_images_similar of this ImageSimilarityComparisonResponse.  # noqa: E501
        :type: bool
        """

        self._are_images_similar = are_images_similar

    @property
    def image_similarity_score(self):
        """Gets the image_similarity_score of this ImageSimilarityComparisonResponse.  # noqa: E501

        Similarity score between 0.0 and 1.0, with 1.0 meaning highly similar and 0.0 meaning highly dissimilar  # noqa: E501

        :return: The image_similarity_score of this ImageSimilarityComparisonResponse.  # noqa: E501
        :rtype: float
        """
        return self._image_similarity_score

    @image_similarity_score.setter
    def image_similarity_score(self, image_similarity_score):
        """Sets the image_similarity_score of this ImageSimilarityComparisonResponse.

        Similarity score between 0.0 and 1.0, with 1.0 meaning highly similar and 0.0 meaning highly dissimilar  # noqa: E501

        :param image_similarity_score: The image_similarity_score of this ImageSimilarityComparisonResponse.  # noqa: E501
        :type: float
        """

        self._image_similarity_score = image_similarity_score

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
        if issubclass(ImageSimilarityComparisonResponse, dict):
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
        if not isinstance(other, ImageSimilarityComparisonResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other