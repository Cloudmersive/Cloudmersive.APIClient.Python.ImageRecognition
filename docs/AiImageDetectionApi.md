# cloudmersive_image_api_client.AiImageDetectionApi

All URIs are relative to *http://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_image_detection_detect_file**](AiImageDetectionApi.md#ai_image_detection_detect_file) | **POST** /image/ai-detection/file | Detect if an input image was generated using AI


# **ai_image_detection_detect_file**
> ImageAiDetectionResult ai_image_detection_detect_file(image_file)

Detect if an input image was generated using AI

Detects if the input image was generated using AI tools.

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
api_instance = cloudmersive_image_api_client.AiImageDetectionApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Detect if an input image was generated using AI
    api_response = api_instance.ai_image_detection_detect_file(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AiImageDetectionApi->ai_image_detection_detect_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**ImageAiDetectionResult**](ImageAiDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

