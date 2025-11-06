# cloudmersive_image_api_client.TextGenerationApi

All URIs are relative to *http://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_generation_create_handwriting_png**](TextGenerationApi.md#text_generation_create_handwriting_png) | **POST** /image/text/create/handwriting/png | Create an image of handwriting in PNG format


# **text_generation_create_handwriting_png**
> object text_generation_create_handwriting_png(request)

Create an image of handwriting in PNG format

Uses Deep Learning to generate realistic handwriting and returns the result as a PNG image

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
api_instance = cloudmersive_image_api_client.TextGenerationApi(cloudmersive_image_api_client.ApiClient(configuration))
request = cloudmersive_image_api_client.CreateHandwritingRequest() # CreateHandwritingRequest | Draw text parameters

try:
    # Create an image of handwriting in PNG format
    api_response = api_instance.text_generation_create_handwriting_png(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextGenerationApi->text_generation_create_handwriting_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateHandwritingRequest**](CreateHandwritingRequest.md)| Draw text parameters | 

### Return type

**object**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

