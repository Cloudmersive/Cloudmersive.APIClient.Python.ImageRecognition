# coding: utf-8

"""
    imageapi

    Image Recognition and Processing APIs let you use Machine Learning to recognize and process images, and also perform useful image modification operations.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_image_api_client.api_client import ApiClient


class TextGenerationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def text_generation_create_handwriting_png(self, request, **kwargs):  # noqa: E501
        """Create an image of handwriting in PNG format  # noqa: E501

        Uses Deep Learning to generate realistic handwriting and returns the result as a PNG image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.text_generation_create_handwriting_png(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateHandwritingRequest request: Draw text parameters (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.text_generation_create_handwriting_png_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.text_generation_create_handwriting_png_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def text_generation_create_handwriting_png_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create an image of handwriting in PNG format  # noqa: E501

        Uses Deep Learning to generate realistic handwriting and returns the result as a PNG image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.text_generation_create_handwriting_png_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateHandwritingRequest request: Draw text parameters (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method text_generation_create_handwriting_png" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `text_generation_create_handwriting_png`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/image/text/create/handwriting/png', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
