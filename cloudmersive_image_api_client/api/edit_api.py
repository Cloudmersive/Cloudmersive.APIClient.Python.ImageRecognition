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


class EditApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def edit_composite_basic(self, location, base_image, layered_image, **kwargs):  # noqa: E501
        """Composite two images together  # noqa: E501

        Composites two input images together; a layered image onto a base image.  The first image you input is the base image.  The second image (the layered image) will be composited on top of this base image.  Supports PNG transparency.  To control padding you can include transparent pixels at the border(s) of your layered images as appropriate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_composite_basic(location, base_image, layered_image, async=True)
        >>> result = thread.get()

        :param async bool
        :param str location: Location to composite the layered images; possible values are: \"center\", \"top-left\", \"top-center\", \"top-right\", \"center-left\", \"center-right\", \"bottom-left\", \"bottom-center\", \"bottom-right\" (required)
        :param file base_image: Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. (required)
        :param file layered_image: Image to layer on top of the base image. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.edit_composite_basic_with_http_info(location, base_image, layered_image, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_composite_basic_with_http_info(location, base_image, layered_image, **kwargs)  # noqa: E501
            return data

    def edit_composite_basic_with_http_info(self, location, base_image, layered_image, **kwargs):  # noqa: E501
        """Composite two images together  # noqa: E501

        Composites two input images together; a layered image onto a base image.  The first image you input is the base image.  The second image (the layered image) will be composited on top of this base image.  Supports PNG transparency.  To control padding you can include transparent pixels at the border(s) of your layered images as appropriate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_composite_basic_with_http_info(location, base_image, layered_image, async=True)
        >>> result = thread.get()

        :param async bool
        :param str location: Location to composite the layered images; possible values are: \"center\", \"top-left\", \"top-center\", \"top-right\", \"center-left\", \"center-right\", \"bottom-left\", \"bottom-center\", \"bottom-right\" (required)
        :param file base_image: Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. (required)
        :param file layered_image: Image to layer on top of the base image. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location', 'base_image', 'layered_image']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_composite_basic" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'location' is set
        if ('location' not in params or
                params['location'] is None):
            raise ValueError("Missing the required parameter `location` when calling `edit_composite_basic`")  # noqa: E501
        # verify the required parameter 'base_image' is set
        if ('base_image' not in params or
                params['base_image'] is None):
            raise ValueError("Missing the required parameter `base_image` when calling `edit_composite_basic`")  # noqa: E501
        # verify the required parameter 'layered_image' is set
        if ('layered_image' not in params or
                params['layered_image'] is None):
            raise ValueError("Missing the required parameter `layered_image` when calling `edit_composite_basic`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'location' in params:
            path_params['location'] = params['location']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'base_image' in params:
            local_var_files['baseImage'] = params['base_image']  # noqa: E501
        if 'layered_image' in params:
            local_var_files['layeredImage'] = params['layered_image']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/png'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/image/edit/composite/{location}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_draw_rectangle(self, request, **kwargs):  # noqa: E501
        """Draw rectangle onto an image  # noqa: E501

        Draw one or more rectangles, with customized visuals, onto an image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_draw_rectangle(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param DrawRectangleRequest request: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.edit_draw_rectangle_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_draw_rectangle_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def edit_draw_rectangle_with_http_info(self, request, **kwargs):  # noqa: E501
        """Draw rectangle onto an image  # noqa: E501

        Draw one or more rectangles, with customized visuals, onto an image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_draw_rectangle_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param DrawRectangleRequest request: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_draw_rectangle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `edit_draw_rectangle`")  # noqa: E501

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
            ['image/png'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/image/edit/draw/rectangle', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_draw_text(self, request, **kwargs):  # noqa: E501
        """Draw text onto an image  # noqa: E501

        Draw one or more pieces of text, with customized visuals, onto an image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_draw_text(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param DrawTextRequest request: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.edit_draw_text_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_draw_text_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def edit_draw_text_with_http_info(self, request, **kwargs):  # noqa: E501
        """Draw text onto an image  # noqa: E501

        Draw one or more pieces of text, with customized visuals, onto an image  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.edit_draw_text_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param DrawTextRequest request: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_draw_text" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `edit_draw_text`")  # noqa: E501

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
            ['image/png'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/image/edit/draw/text', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
