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


class ResizeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resize_post(self, max_width, max_height, image_file, **kwargs):  # noqa: E501
        """Resize an image while preserving aspect ratio  # noqa: E501

        Resize an image to a maximum width and maximum height, while preserving the image's original aspect ratio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resize_post(max_width, max_height, image_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int max_width: Maximum width of the output image - final image will be as large as possible while less than or equial to this width (required)
        :param int max_height: Maximum height of the output image - final image will be as large as possible while less than or equial to this height (required)
        :param file image_file: Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resize_post_with_http_info(max_width, max_height, image_file, **kwargs)  # noqa: E501
        else:
            (data) = self.resize_post_with_http_info(max_width, max_height, image_file, **kwargs)  # noqa: E501
            return data

    def resize_post_with_http_info(self, max_width, max_height, image_file, **kwargs):  # noqa: E501
        """Resize an image while preserving aspect ratio  # noqa: E501

        Resize an image to a maximum width and maximum height, while preserving the image's original aspect ratio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resize_post_with_http_info(max_width, max_height, image_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int max_width: Maximum width of the output image - final image will be as large as possible while less than or equial to this width (required)
        :param int max_height: Maximum height of the output image - final image will be as large as possible while less than or equial to this height (required)
        :param file image_file: Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['max_width', 'max_height', 'image_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resize_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'max_width' is set
        if ('max_width' not in params or
                params['max_width'] is None):
            raise ValueError("Missing the required parameter `max_width` when calling `resize_post`")  # noqa: E501
        # verify the required parameter 'max_height' is set
        if ('max_height' not in params or
                params['max_height'] is None):
            raise ValueError("Missing the required parameter `max_height` when calling `resize_post`")  # noqa: E501
        # verify the required parameter 'image_file' is set
        if ('image_file' not in params or
                params['image_file'] is None):
            raise ValueError("Missing the required parameter `image_file` when calling `resize_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'max_width' in params:
            path_params['maxWidth'] = params['max_width']  # noqa: E501
        if 'max_height' in params:
            path_params['maxHeight'] = params['max_height']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'image_file' in params:
            local_var_files['imageFile'] = params['image_file']  # noqa: E501

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
            '/image/resize/preserveAspectRatio/{maxWidth}/{maxHeight}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resize_resize_simple(self, width, height, image_file, **kwargs):  # noqa: E501
        """Resize an image  # noqa: E501

        Resize an image to a specific width and specific height  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resize_resize_simple(width, height, image_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int width: (required)
        :param int height: (required)
        :param file image_file: Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resize_resize_simple_with_http_info(width, height, image_file, **kwargs)  # noqa: E501
        else:
            (data) = self.resize_resize_simple_with_http_info(width, height, image_file, **kwargs)  # noqa: E501
            return data

    def resize_resize_simple_with_http_info(self, width, height, image_file, **kwargs):  # noqa: E501
        """Resize an image  # noqa: E501

        Resize an image to a specific width and specific height  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resize_resize_simple_with_http_info(width, height, image_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int width: (required)
        :param int height: (required)
        :param file image_file: Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['width', 'height', 'image_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resize_resize_simple" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `resize_resize_simple`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `resize_resize_simple`")  # noqa: E501
        # verify the required parameter 'image_file' is set
        if ('image_file' not in params or
                params['image_file'] is None):
            raise ValueError("Missing the required parameter `image_file` when calling `resize_resize_simple`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'width' in params:
            path_params['width'] = params['width']  # noqa: E501
        if 'height' in params:
            path_params['height'] = params['height']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'image_file' in params:
            local_var_files['imageFile'] = params['image_file']  # noqa: E501

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
            '/image/resize/target/{width}/{height}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
