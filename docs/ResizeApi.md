# cloudmersive_image_api_client.ResizeApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resize_post**](ResizeApi.md#resize_post) | **POST** /image/resize/preserveAspectRatio/{maxWidth}/{maxHeight} | Resize an image while preserving aspect ratio
[**resize_resize_simple**](ResizeApi.md#resize_resize_simple) | **POST** /image/resize/target/{width}/{height} | Resize an image


# **resize_post**
> str resize_post(max_width, max_height, image_file)

Resize an image while preserving aspect ratio

Resize an image to a maximum width and maximum height, while preserving the image's original aspect ratio.  Resize is EXIF-aware.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_image_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_image_api_client.ResizeApi(cloudmersive_image_api_client.ApiClient(configuration))
max_width = 56 # int | Maximum width of the output image - final image will be as large as possible while less than or equial to this width
max_height = 56 # int | Maximum height of the output image - final image will be as large as possible while less than or equial to this height
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Resize an image while preserving aspect ratio
    api_response = api_instance.resize_post(max_width, max_height, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResizeApi->resize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_width** | **int**| Maximum width of the output image - final image will be as large as possible while less than or equial to this width | 
 **max_height** | **int**| Maximum height of the output image - final image will be as large as possible while less than or equial to this height | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_resize_simple**
> str resize_resize_simple(width, height, image_file)

Resize an image

Resize an image to a specific width and specific height.  Resize is EXIF-aware.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_image_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_image_api_client.ResizeApi(cloudmersive_image_api_client.ApiClient(configuration))
width = 56 # int | Width of the output image - final image will be exactly this width
height = 56 # int | Height of the output image - final image will be exactly this height
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Resize an image
    api_response = api_instance.resize_resize_simple(width, height, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResizeApi->resize_resize_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**| Width of the output image - final image will be exactly this width | 
 **height** | **int**| Height of the output image - final image will be exactly this height | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

