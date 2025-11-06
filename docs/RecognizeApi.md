# cloudmersive_image_api_client.RecognizeApi

All URIs are relative to *http://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recognize_describe**](RecognizeApi.md#recognize_describe) | **POST** /image/recognize/describe | Describe an image in natural language
[**recognize_detect_and_unskew_document**](RecognizeApi.md#recognize_detect_and_unskew_document) | **POST** /image/recognize/detect-document/unskew | Detect and unskew a photo of a document
[**recognize_detect_text_fine**](RecognizeApi.md#recognize_detect_text_fine) | **POST** /image/recognize/detect-text/fine | Detect fine text in a photo of a document
[**recognize_detect_text_large**](RecognizeApi.md#recognize_detect_text_large) | **POST** /image/recognize/detect-text/large | Detect large text in a photo
[**recognize_detect_vehicle_license_plates**](RecognizeApi.md#recognize_detect_vehicle_license_plates) | **POST** /image/recognize/detect-vehicle-license-plates | Detect vehicle license plates in an image
[**recognize_find_symbol**](RecognizeApi.md#recognize_find_symbol) | **POST** /image/recognize/find/symbol | Find the location of a symbol in an image
[**recognize_similarity_compare**](RecognizeApi.md#recognize_similarity_compare) | **POST** /image/recognize/similarity/compare | Compare two images for similarity
[**recognize_similarity_hash**](RecognizeApi.md#recognize_similarity_hash) | **POST** /image/recognize/similarity/hash | Generate a perceptual image hash
[**recognize_similarity_hash_distance**](RecognizeApi.md#recognize_similarity_hash_distance) | **POST** /image/recognize/similarity/hash/distance | Calculates the similarity between two perceptual image hashes


# **recognize_describe**
> ImageDescriptionResponse recognize_describe(image_file)

Describe an image in natural language

Generate an English language text description of the image as a sentence.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Describe an image in natural language
    api_response = api_instance.recognize_describe(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_describe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**ImageDescriptionResponse**](ImageDescriptionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_detect_and_unskew_document**
> str recognize_detect_and_unskew_document(image_file, post_processing_effect=post_processing_effect)

Detect and unskew a photo of a document

Detect and unskew a photo of a document (e.g. taken on a cell phone) into a perfectly square image.  Great for document scanning applications; once unskewed, this image is perfect for converting to PDF using the Convert API or optical character recognition using the OCR API.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
post_processing_effect = 'post_processing_effect_example' # str | Optional, post-processing effects to apply to the email, default is None.  Possible values are None and BlackAndWhite (force the image into a black and white view to aid in OCR operations). (optional)

try:
    # Detect and unskew a photo of a document
    api_response = api_instance.recognize_detect_and_unskew_document(image_file, post_processing_effect=post_processing_effect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_detect_and_unskew_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 
 **post_processing_effect** | **str**| Optional, post-processing effects to apply to the email, default is None.  Possible values are None and BlackAndWhite (force the image into a black and white view to aid in OCR operations). | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_detect_text_fine**
> FineTextDetectionResult recognize_detect_text_fine(image_file)

Detect fine text in a photo of a document

Identify the position, and size of small/fine text within a photograph of a document.  Identify the location of small text in a photo - such as words and other forms of high density text.  Can be used on a scan of a document or a photograph (e.g. smartphone camera) of a document, page or receipt.  For OCR purposes - please see our Deep Learning OCR APIs.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Detect fine text in a photo of a document
    api_response = api_instance.recognize_detect_text_fine(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_detect_text_fine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**FineTextDetectionResult**](FineTextDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_detect_text_large**
> TextDetectionResult recognize_detect_text_large(image_file)

Detect large text in a photo

Identify the position, and size of large text within a photograph.  Identify the location of large text in a photo - such as signs, titles, etc. and other forms of large, low-density text.  Not suitable for high-density text (e.g. scans of documents, receipts, etc.) for OCR purposes - for OCR, please see our Deep Learning OCR APIs.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Detect large text in a photo
    api_response = api_instance.recognize_detect_text_large(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_detect_text_large: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**TextDetectionResult**](TextDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_detect_vehicle_license_plates**
> VehicleLicensePlateDetectionResult recognize_detect_vehicle_license_plates(image_file)

Detect vehicle license plates in an image

Identify the position, and size, and content of vehicle license plates in an image.  License plates should be within 15-20 degrees on-axis to the camera.  Supported image formats are JPG, PNG and BMP.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Detect vehicle license plates in an image
    api_response = api_instance.recognize_detect_vehicle_license_plates(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_detect_vehicle_license_plates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 

### Return type

[**VehicleLicensePlateDetectionResult**](VehicleLicensePlateDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_find_symbol**
> FindSymbolResult recognize_find_symbol(input_image, target_image)

Find the location of a symbol in an image

Determine if an image contains a symbol, and if so, the location of that symbol in the image.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
input_image = '/path/to/file.txt' # file | Image file to search through for the target image.
target_image = '/path/to/file.txt' # file | Image to find in the input image.

try:
    # Find the location of a symbol in an image
    api_response = api_instance.recognize_find_symbol(input_image, target_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_find_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_image** | **file**| Image file to search through for the target image. | 
 **target_image** | **file**| Image to find in the input image. | 

### Return type

[**FindSymbolResult**](FindSymbolResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_similarity_compare**
> str recognize_similarity_compare(base_image, comparison_image, recognition_mode=recognition_mode)

Compare two images for similarity

Generates an image similarity score using Deep Learning between 0.0 and 1.0, values closer to 1.0 indicate greater similarity

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
base_image = '/path/to/file.txt' # file | Image file to compare against.  Common file formats such as PNG, JPEG are supported.
comparison_image = '/path/to/file.txt' # file | Image to compare to the base image.
recognition_mode = 'recognition_mode_example' # str | Optional, specify the recognition mode; possible values are Normal, Basic and Advanced.  Default is Normal. (optional)

try:
    # Compare two images for similarity
    api_response = api_instance.recognize_similarity_compare(base_image, comparison_image, recognition_mode=recognition_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_similarity_compare: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_image** | **file**| Image file to compare against.  Common file formats such as PNG, JPEG are supported. | 
 **comparison_image** | **file**| Image to compare to the base image. | 
 **recognition_mode** | **str**| Optional, specify the recognition mode; possible values are Normal, Basic and Advanced.  Default is Normal. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_similarity_hash**
> ImageSimilarityHashResponse recognize_similarity_hash(image_file, recognition_mode=recognition_mode)

Generate a perceptual image hash

Generates a hash value for the image; hash values that are closer together in terms of Hamming Distance are more similar.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
recognition_mode = 'recognition_mode_example' # str | Optional, specify the recognition mode; possible values are Normal, Basic and Advanced.  Default is Normal. (optional)

try:
    # Generate a perceptual image hash
    api_response = api_instance.recognize_similarity_hash(image_file, recognition_mode=recognition_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_similarity_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file** | **file**| Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported. | 
 **recognition_mode** | **str**| Optional, specify the recognition mode; possible values are Normal, Basic and Advanced.  Default is Normal. | [optional] 

### Return type

[**ImageSimilarityHashResponse**](ImageSimilarityHashResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_similarity_hash_distance**
> ImageSimilarityHashDistanceResponse recognize_similarity_hash_distance(request)

Calculates the similarity between two perceptual image hashes

Calculates the similarity between two perceptual image hashes by computing the Hamming Distance between them.

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
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
request = cloudmersive_image_api_client.ImageSimilarityHashDistanceRequest() # ImageSimilarityHashDistanceRequest | 

try:
    # Calculates the similarity between two perceptual image hashes
    api_response = api_instance.recognize_similarity_hash_distance(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_similarity_hash_distance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ImageSimilarityHashDistanceRequest**](ImageSimilarityHashDistanceRequest.md)|  | 

### Return type

[**ImageSimilarityHashDistanceResponse**](ImageSimilarityHashDistanceResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

