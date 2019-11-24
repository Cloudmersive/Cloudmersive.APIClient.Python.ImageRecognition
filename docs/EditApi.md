# cloudmersive_image_api_client.EditApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_auto_orient**](EditApi.md#edit_auto_orient) | **POST** /image/edit/auto-orient/remove-exif | Normalizes image rotation and removes EXIF rotation data
[**edit_composite_basic**](EditApi.md#edit_composite_basic) | **POST** /image/edit/composite/{location} | Composite two images together
[**edit_contrast_adaptive**](EditApi.md#edit_contrast_adaptive) | **POST** /image/edit/contrast/{gamma}/adaptive | Adaptively adjust the contrast of the image to be more appealing and easy to see
[**edit_crop_rectangle**](EditApi.md#edit_crop_rectangle) | **POST** /image/edit/crop/rectangle/{left}/{top}/{width}/{height} | Crop an image to a rectangular area
[**edit_draw_polygon**](EditApi.md#edit_draw_polygon) | **POST** /image/edit/draw/polygon | Draw a polygon onto an image
[**edit_draw_rectangle**](EditApi.md#edit_draw_rectangle) | **POST** /image/edit/draw/rectangle | Draw a rectangle onto an image
[**edit_draw_text**](EditApi.md#edit_draw_text) | **POST** /image/edit/draw/text | Draw text onto an image
[**edit_drop_shadow**](EditApi.md#edit_drop_shadow) | **POST** /image/edit/drop-shadow/{X}/{Y}/{sigma}/{opacity} | Add a customizeable drop shadow to an image
[**edit_rotate**](EditApi.md#edit_rotate) | **POST** /image/edit/rotate/{degrees}/angle | Rotate an image any number of degrees


# **edit_auto_orient**
> str edit_auto_orient(image_file)

Normalizes image rotation and removes EXIF rotation data

Automatically orients the input image based on EXIF information and then removes the EXIF information.  EXIF is an additional set of information stored in some images taken with cell phone cameras based on the orientation of the camera.  By normalizing rotation and removing EXIF data these images become much easier to process.

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Normalizes image rotation and removes EXIF rotation data
    api_response = api_instance.edit_auto_orient(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_auto_orient: %s\n" % e)
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

# **edit_composite_basic**
> str edit_composite_basic(location, base_image, layered_image)

Composite two images together

Composites two input images together; a layered image onto a base image.  The first image you input is the base image.  The second image (the layered image) will be composited on top of this base image.  Supports PNG transparency.  To control padding you can include transparent pixels at the border(s) of your layered images as appropriate.

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
location = 'location_example' # str | Location to composite the layered images; possible values are: \"center\", \"top-left\", \"top-center\", \"top-right\", \"center-left\", \"center-right\", \"bottom-left\", \"bottom-center\", \"bottom-right\"
base_image = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
layered_image = '/path/to/file.txt' # file | Image to layer on top of the base image.

try:
    # Composite two images together
    api_response = api_instance.edit_composite_basic(location, base_image, layered_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_composite_basic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| Location to composite the layered images; possible values are: \&quot;center\&quot;, \&quot;top-left\&quot;, \&quot;top-center\&quot;, \&quot;top-right\&quot;, \&quot;center-left\&quot;, \&quot;center-right\&quot;, \&quot;bottom-left\&quot;, \&quot;bottom-center\&quot;, \&quot;bottom-right\&quot; | 
 **base_image** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 
 **layered_image** | **file**| Image to layer on top of the base image. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_contrast_adaptive**
> str edit_contrast_adaptive(gamma, image_file)

Adaptively adjust the contrast of the image to be more appealing and easy to see

Uses Gamma to adjust the contrast adaptively the way the human eye sees the world.  Results significantly improve the viewability and visual appeal of the image.

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
gamma = 1.2 # float | Gamma value to adjust the contrast in the image.  Recommended value is 2.0.  Values between 0.0 and 1.0 will reduce contrast, while values above 1.0 will increase contrast.
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Adaptively adjust the contrast of the image to be more appealing and easy to see
    api_response = api_instance.edit_contrast_adaptive(gamma, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_contrast_adaptive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gamma** | **float**| Gamma value to adjust the contrast in the image.  Recommended value is 2.0.  Values between 0.0 and 1.0 will reduce contrast, while values above 1.0 will increase contrast. | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_crop_rectangle**
> str edit_crop_rectangle(left, top, width, height, image_file)

Crop an image to a rectangular area

Crop an image to a target rectangular area

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
left = 56 # int | The left edge of the rectangular crop area in pixels (X).
top = 56 # int | The top edge of the rectangular crop area in pixels (Y).
width = 56 # int | The width of the rectangular crop area in pixels.
height = 56 # int | The height of the rectangular crop area in pixels.
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Crop an image to a rectangular area
    api_response = api_instance.edit_crop_rectangle(left, top, width, height, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_crop_rectangle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **left** | **int**| The left edge of the rectangular crop area in pixels (X). | 
 **top** | **int**| The top edge of the rectangular crop area in pixels (Y). | 
 **width** | **int**| The width of the rectangular crop area in pixels. | 
 **height** | **int**| The height of the rectangular crop area in pixels. | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_draw_polygon**
> str edit_draw_polygon(request)

Draw a polygon onto an image

Draw one or more polygons, with customized visuals, onto an image

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
request = cloudmersive_image_api_client.DrawPolygonRequest() # DrawPolygonRequest | 

try:
    # Draw a polygon onto an image
    api_response = api_instance.edit_draw_polygon(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_draw_polygon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DrawPolygonRequest**](DrawPolygonRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_draw_rectangle**
> str edit_draw_rectangle(request)

Draw a rectangle onto an image

Draw one or more rectangles, with customized visuals, onto an image

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
request = cloudmersive_image_api_client.DrawRectangleRequest() # DrawRectangleRequest | 

try:
    # Draw a rectangle onto an image
    api_response = api_instance.edit_draw_rectangle(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_draw_rectangle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DrawRectangleRequest**](DrawRectangleRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_draw_text**
> str edit_draw_text(request)

Draw text onto an image

Draw one or more pieces of text, with customized visuals, onto an image

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
request = cloudmersive_image_api_client.DrawTextRequest() # DrawTextRequest | 

try:
    # Draw text onto an image
    api_response = api_instance.edit_draw_text(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_draw_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DrawTextRequest**](DrawTextRequest.md)|  | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_drop_shadow**
> str edit_drop_shadow(x, y, sigma, opacity, image_file)

Add a customizeable drop shadow to an image

Add a customizeable drop shadow to the image

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
x = 56 # int | 
y = 56 # int | 
sigma = 56 # int | Sigma (blur distance) of the drop shadow
opacity = 56 # int | Opacity of the drop shadow; 0 is 0% and 100 is 100%
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Add a customizeable drop shadow to an image
    api_response = api_instance.edit_drop_shadow(x, y, sigma, opacity, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_drop_shadow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **int**|  | 
 **y** | **int**|  | 
 **sigma** | **int**| Sigma (blur distance) of the drop shadow | 
 **opacity** | **int**| Opacity of the drop shadow; 0 is 0% and 100 is 100% | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_rotate**
> str edit_rotate(degrees, image_file)

Rotate an image any number of degrees

Rotates an image by an arbitrary number of degrees

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
api_instance = cloudmersive_image_api_client.EditApi(cloudmersive_image_api_client.ApiClient(configuration))
degrees = 1.2 # float | Degrees to rotate the image; values range from 0.0 to 360.0.
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Rotate an image any number of degrees
    api_response = api_instance.edit_rotate(degrees, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditApi->edit_rotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degrees** | **float**| Degrees to rotate the image; values range from 0.0 to 360.0. | 
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

