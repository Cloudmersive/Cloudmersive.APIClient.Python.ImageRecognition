# cloudmersive_image_api_client.FilterApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_black_and_white**](FilterApi.md#filter_black_and_white) | **POST** /image/filter/black-and-white | Convert image to black-and-white grayscale
[**filter_despeckle**](FilterApi.md#filter_despeckle) | **POST** /image/filter/despeckle | Despeckle to remove point noise from the image
[**filter_edge_detect**](FilterApi.md#filter_edge_detect) | **POST** /image/filter/edge-detect/{radius} | Detect and highlight edges in an image
[**filter_emboss**](FilterApi.md#filter_emboss) | **POST** /image/filter/emboss/{radius}/{sigma} | Emboss an image
[**filter_gaussian_blur**](FilterApi.md#filter_gaussian_blur) | **POST** /image/filter/blur/guassian/{radius}/{sigma} | Perform a guassian blur on the input image
[**filter_motion_blur**](FilterApi.md#filter_motion_blur) | **POST** /image/filter/blur/motion/{radius}/{sigma}/{angle} | Perform a motion blur on the input image
[**filter_posterize**](FilterApi.md#filter_posterize) | **POST** /image/filter/posterize | Posterize the image by reducing distinct colors
[**filter_swirl**](FilterApi.md#filter_swirl) | **POST** /image/filter/swirl | Swirl distort the image


# **filter_black_and_white**
> str filter_black_and_white(image_file)

Convert image to black-and-white grayscale

Remove color from the image by converting to a grayscale, black-and-white image

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Convert image to black-and-white grayscale
    api_response = api_instance.filter_black_and_white(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_black_and_white: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_despeckle**
> str filter_despeckle(image_file)

Despeckle to remove point noise from the image

Remove point noise / despeckle the input image

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Despeckle to remove point noise from the image
    api_response = api_instance.filter_despeckle(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_despeckle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_edge_detect**
> str filter_edge_detect(radius, image_file)

Detect and highlight edges in an image

Perform an edge detection operation on the input image

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
radius = 56 # int | Radius in pixels of the edge detection operation; a larger radius will produce a greater effect
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Detect and highlight edges in an image
    api_response = api_instance.filter_edge_detect(radius, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_edge_detect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius** | **int**| Radius in pixels of the edge detection operation; a larger radius will produce a greater effect | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_emboss**
> str filter_emboss(radius, sigma, image_file)

Emboss an image

Perform an emboss operation on the input image

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
radius = 56 # int | Radius in pixels of the emboss operation; a larger radius will produce a greater effect
sigma = 56 # int | Sigma, or variance, of the emboss operation
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Emboss an image
    api_response = api_instance.filter_emboss(radius, sigma, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_emboss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius** | **int**| Radius in pixels of the emboss operation; a larger radius will produce a greater effect | 
 **sigma** | **int**| Sigma, or variance, of the emboss operation | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_gaussian_blur**
> str filter_gaussian_blur(radius, sigma, image_file)

Perform a guassian blur on the input image

Perform a gaussian blur on the input image

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
radius = 56 # int | Radius in pixels of the blur operation; a larger radius will produce a greater blur effect
sigma = 56 # int | Sigma, or variance, of the gaussian blur operation
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Perform a guassian blur on the input image
    api_response = api_instance.filter_gaussian_blur(radius, sigma, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_gaussian_blur: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius** | **int**| Radius in pixels of the blur operation; a larger radius will produce a greater blur effect | 
 **sigma** | **int**| Sigma, or variance, of the gaussian blur operation | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_motion_blur**
> str filter_motion_blur(radius, sigma, angle, image_file)

Perform a motion blur on the input image

Perform a motion blur on the input image at a specific angle

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
radius = 56 # int | Radius in pixels of the blur operation; a larger radius will produce a greater blur effect
sigma = 56 # int | Sigma, or variance, of the motion blur operation
angle = 56 # int | Angle of the motion blur in degrees
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Perform a motion blur on the input image
    api_response = api_instance.filter_motion_blur(radius, sigma, angle, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_motion_blur: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius** | **int**| Radius in pixels of the blur operation; a larger radius will produce a greater blur effect | 
 **sigma** | **int**| Sigma, or variance, of the motion blur operation | 
 **angle** | **int**| Angle of the motion blur in degrees | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_posterize**
> str filter_posterize(levels, image_file)

Posterize the image by reducing distinct colors

Reduce the unique number of colors in the image to the specified level

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
levels = 56 # int | Number of unique colors to retain in the output image
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Posterize the image by reducing distinct colors
    api_response = api_instance.filter_posterize(levels, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_posterize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **levels** | **int**| Number of unique colors to retain in the output image | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_swirl**
> str filter_swirl(degrees, image_file)

Swirl distort the image

Swirl distort the image by the specified number of degrees

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
api_instance = cloudmersive_image_api_client.FilterApi(cloudmersive_image_api_client.ApiClient(configuration))
degrees = 56 # int | Degrees of swirl
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Swirl distort the image
    api_response = api_instance.filter_swirl(degrees, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilterApi->filter_swirl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degrees** | **int**| Degrees of swirl | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

