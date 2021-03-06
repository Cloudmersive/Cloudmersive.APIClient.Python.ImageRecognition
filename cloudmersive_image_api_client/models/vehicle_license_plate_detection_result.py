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


class VehicleLicensePlateDetectionResult(object):
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
        'detected_license_plates': 'list[DetectedLicensePlate]',
        'detected_license_plate_count': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'detected_license_plates': 'DetectedLicensePlates',
        'detected_license_plate_count': 'DetectedLicensePlateCount'
    }

    def __init__(self, successful=None, detected_license_plates=None, detected_license_plate_count=None):  # noqa: E501
        """VehicleLicensePlateDetectionResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._detected_license_plates = None
        self._detected_license_plate_count = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if detected_license_plates is not None:
            self.detected_license_plates = detected_license_plates
        if detected_license_plate_count is not None:
            self.detected_license_plate_count = detected_license_plate_count

    @property
    def successful(self):
        """Gets the successful of this VehicleLicensePlateDetectionResult.  # noqa: E501

        Was the image processed successfully?  # noqa: E501

        :return: The successful of this VehicleLicensePlateDetectionResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this VehicleLicensePlateDetectionResult.

        Was the image processed successfully?  # noqa: E501

        :param successful: The successful of this VehicleLicensePlateDetectionResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def detected_license_plates(self):
        """Gets the detected_license_plates of this VehicleLicensePlateDetectionResult.  # noqa: E501

        License plates found in the image  # noqa: E501

        :return: The detected_license_plates of this VehicleLicensePlateDetectionResult.  # noqa: E501
        :rtype: list[DetectedLicensePlate]
        """
        return self._detected_license_plates

    @detected_license_plates.setter
    def detected_license_plates(self, detected_license_plates):
        """Sets the detected_license_plates of this VehicleLicensePlateDetectionResult.

        License plates found in the image  # noqa: E501

        :param detected_license_plates: The detected_license_plates of this VehicleLicensePlateDetectionResult.  # noqa: E501
        :type: list[DetectedLicensePlate]
        """

        self._detected_license_plates = detected_license_plates

    @property
    def detected_license_plate_count(self):
        """Gets the detected_license_plate_count of this VehicleLicensePlateDetectionResult.  # noqa: E501

        The number of license plates detected in the image  # noqa: E501

        :return: The detected_license_plate_count of this VehicleLicensePlateDetectionResult.  # noqa: E501
        :rtype: int
        """
        return self._detected_license_plate_count

    @detected_license_plate_count.setter
    def detected_license_plate_count(self, detected_license_plate_count):
        """Sets the detected_license_plate_count of this VehicleLicensePlateDetectionResult.

        The number of license plates detected in the image  # noqa: E501

        :param detected_license_plate_count: The detected_license_plate_count of this VehicleLicensePlateDetectionResult.  # noqa: E501
        :type: int
        """

        self._detected_license_plate_count = detected_license_plate_count

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
        if issubclass(VehicleLicensePlateDetectionResult, dict):
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
        if not isinstance(other, VehicleLicensePlateDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
