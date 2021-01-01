# cloudmersive_image_api_client
Image Recognition and Processing APIs let you use Machine Learning to recognize and process images, and also perform useful image modification operations.

This Python package provides a native API client for [Cloudmersive Image Recognition and Processing](https://www.cloudmersive.com/image-recognition-and-processing-api)

- API version: v1
- Package version: 3.0.3
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_image_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_image_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = cloudmersive_image_api_client.ArtisticApi(cloudmersive_image_api_client.ApiClient(configuration))
style = 'style_example' # str | The style of the painting to apply.  To start, try \"udnie\" a painting style.  Possible values are: \"udnie\", \"wave\", \"la_muse\", \"rain_princess\".
image_file = '/path/to/file.txt' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Transform an image into an artistic painting automatically
    api_response = api_instance.artistic_painting(style, image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtisticApi->artistic_painting: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtisticApi* | [**artistic_painting**](docs/ArtisticApi.md#artistic_painting) | **POST** /image/artistic/painting/{style} | Transform an image into an artistic painting automatically
*ConvertApi* | [**convert_to_bmp**](docs/ConvertApi.md#convert_to_bmp) | **POST** /image/convert/to/bmp | Convert input image to Bitmap BMP format
*ConvertApi* | [**convert_to_gif**](docs/ConvertApi.md#convert_to_gif) | **POST** /image/convert/to/gif | Convert input image to GIF format
*ConvertApi* | [**convert_to_jpg**](docs/ConvertApi.md#convert_to_jpg) | **POST** /image/convert/to/jpg/{quality} | Convert input image to JPG, JPEG format
*ConvertApi* | [**convert_to_photoshop**](docs/ConvertApi.md#convert_to_photoshop) | **POST** /image/convert/to/psd | Convert input image to Photoshop PSD format
*ConvertApi* | [**convert_to_png**](docs/ConvertApi.md#convert_to_png) | **POST** /image/convert/to/png | Convert input image to PNG format
*ConvertApi* | [**convert_to_tiff**](docs/ConvertApi.md#convert_to_tiff) | **POST** /image/convert/to/tiff | Convert input image to TIFF format
*ConvertApi* | [**convert_to_web_p**](docs/ConvertApi.md#convert_to_web_p) | **POST** /image/convert/to/webp | Convert input image to WebP format
*EditApi* | [**edit_auto_orient**](docs/EditApi.md#edit_auto_orient) | **POST** /image/edit/auto-orient/remove-exif | Normalizes image rotation and removes EXIF rotation data
*EditApi* | [**edit_composite_basic**](docs/EditApi.md#edit_composite_basic) | **POST** /image/edit/composite/{location} | Composite two images together
*EditApi* | [**edit_composite_precise**](docs/EditApi.md#edit_composite_precise) | **POST** /image/edit/composite/precise | Composite two images together precisely
*EditApi* | [**edit_contrast_adaptive**](docs/EditApi.md#edit_contrast_adaptive) | **POST** /image/edit/contrast/{gamma}/adaptive | Adaptively adjust the contrast of the image to be more appealing and easy to see
*EditApi* | [**edit_crop_circle**](docs/EditApi.md#edit_crop_circle) | **POST** /image/edit/crop/circle/{left}/{top}/{radius} | Crop an image to an circular area
*EditApi* | [**edit_crop_rectangle**](docs/EditApi.md#edit_crop_rectangle) | **POST** /image/edit/crop/rectangle/{left}/{top}/{width}/{height} | Crop an image to a rectangular area
*EditApi* | [**edit_draw_polygon**](docs/EditApi.md#edit_draw_polygon) | **POST** /image/edit/draw/polygon | Draw a polygon onto an image
*EditApi* | [**edit_draw_rectangle**](docs/EditApi.md#edit_draw_rectangle) | **POST** /image/edit/draw/rectangle | Draw a rectangle onto an image
*EditApi* | [**edit_draw_text**](docs/EditApi.md#edit_draw_text) | **POST** /image/edit/draw/text | Draw text onto an image
*EditApi* | [**edit_drop_shadow**](docs/EditApi.md#edit_drop_shadow) | **POST** /image/edit/drop-shadow/{X}/{Y}/{sigma}/{opacity} | Add a customizeable drop shadow to an image
*EditApi* | [**edit_invert**](docs/EditApi.md#edit_invert) | **POST** /image/edit/invert | Invert, negate the colors in the image
*EditApi* | [**edit_remove_exif_data**](docs/EditApi.md#edit_remove_exif_data) | **POST** /image/edit/remove-exif | Remove EXIF data from the image
*EditApi* | [**edit_remove_transparency**](docs/EditApi.md#edit_remove_transparency) | **POST** /image/edit/remove-transparency | Remove transparency from the image
*EditApi* | [**edit_rotate**](docs/EditApi.md#edit_rotate) | **POST** /image/edit/rotate/{degrees}/angle | Rotate an image any number of degrees
*FaceApi* | [**face_compare**](docs/FaceApi.md#face_compare) | **POST** /image/face/compare-and-match | Compare and match faces
*FaceApi* | [**face_crop_first**](docs/FaceApi.md#face_crop_first) | **POST** /image/face/crop/first | Crop image to face with square crop
*FaceApi* | [**face_crop_first_round**](docs/FaceApi.md#face_crop_first_round) | **POST** /image/face/crop/first/round | Crop image to face with round crop
*FaceApi* | [**face_detect_age**](docs/FaceApi.md#face_detect_age) | **POST** /image/face/detect-age | Detect the age of people in an image
*FaceApi* | [**face_detect_gender**](docs/FaceApi.md#face_detect_gender) | **POST** /image/face/detect-gender | Detect the gender of people in an image
*FaceApi* | [**face_locate**](docs/FaceApi.md#face_locate) | **POST** /image/face/locate | Detect and find faces in an image
*FaceApi* | [**face_locate_with_landmarks**](docs/FaceApi.md#face_locate_with_landmarks) | **POST** /image/face/locate-with-landmarks | Detect and find faces and landmarks eyes and nose and mouth in image
*FilterApi* | [**filter_black_and_white**](docs/FilterApi.md#filter_black_and_white) | **POST** /image/filter/black-and-white | Convert image to black-and-white grayscale
*FilterApi* | [**filter_despeckle**](docs/FilterApi.md#filter_despeckle) | **POST** /image/filter/despeckle | Despeckle to remove point noise from the image
*FilterApi* | [**filter_edge_detect**](docs/FilterApi.md#filter_edge_detect) | **POST** /image/filter/edge-detect/{radius} | Detect and highlight edges in an image
*FilterApi* | [**filter_emboss**](docs/FilterApi.md#filter_emboss) | **POST** /image/filter/emboss/{radius}/{sigma} | Emboss an image
*FilterApi* | [**filter_gaussian_blur**](docs/FilterApi.md#filter_gaussian_blur) | **POST** /image/filter/blur/guassian/{radius}/{sigma} | Perform a guassian blur on the input image
*FilterApi* | [**filter_motion_blur**](docs/FilterApi.md#filter_motion_blur) | **POST** /image/filter/blur/motion/{radius}/{sigma}/{angle} | Perform a motion blur on the input image
*FilterApi* | [**filter_posterize**](docs/FilterApi.md#filter_posterize) | **POST** /image/filter/posterize | Posterize the image by reducing distinct colors
*FilterApi* | [**filter_swirl**](docs/FilterApi.md#filter_swirl) | **POST** /image/filter/swirl | Swirl distort the image
*InfoApi* | [**info_get_dominant_color**](docs/InfoApi.md#info_get_dominant_color) | **POST** /image/get-info/dominant-color | Returns the dominant colors of the image
*InfoApi* | [**info_get_metadata**](docs/InfoApi.md#info_get_metadata) | **POST** /image/get-info/metadata | Returns the image metadata including EXIF and resolution
*NsfwApi* | [**nsfw_classify**](docs/NsfwApi.md#nsfw_classify) | **POST** /image/nsfw/classify | Not safe for work NSFW racy content classification
*RecognizeApi* | [**recognize_describe**](docs/RecognizeApi.md#recognize_describe) | **POST** /image/recognize/describe | Describe an image in natural language
*RecognizeApi* | [**recognize_detect_and_unskew_document**](docs/RecognizeApi.md#recognize_detect_and_unskew_document) | **POST** /image/recognize/detect-document/unskew | Detect and unskew a photo of a document
*RecognizeApi* | [**recognize_detect_objects**](docs/RecognizeApi.md#recognize_detect_objects) | **POST** /image/recognize/detect-objects | Detect objects including types and locations in an image
*RecognizeApi* | [**recognize_detect_people**](docs/RecognizeApi.md#recognize_detect_people) | **POST** /image/recognize/detect-people | Detect people including locations in an image
*RecognizeApi* | [**recognize_detect_text_fine**](docs/RecognizeApi.md#recognize_detect_text_fine) | **POST** /image/recognize/detect-text/fine | Detect fine text in a photo of a document
*RecognizeApi* | [**recognize_detect_text_large**](docs/RecognizeApi.md#recognize_detect_text_large) | **POST** /image/recognize/detect-text/large | Detect large text in a photo
*RecognizeApi* | [**recognize_detect_vehicle_license_plates**](docs/RecognizeApi.md#recognize_detect_vehicle_license_plates) | **POST** /image/recognize/detect-vehicle-license-plates | Detect vehicle license plates in an image
*RecognizeApi* | [**recognize_find_symbol**](docs/RecognizeApi.md#recognize_find_symbol) | **POST** /image/recognize/find/symbol | Find the location of a symbol in an image
*ResizeApi* | [**resize_post**](docs/ResizeApi.md#resize_post) | **POST** /image/resize/preserveAspectRatio/{maxWidth}/{maxHeight} | Resize an image while preserving aspect ratio
*ResizeApi* | [**resize_resize_simple**](docs/ResizeApi.md#resize_resize_simple) | **POST** /image/resize/target/{width}/{height} | Resize an image
*TextGenerationApi* | [**text_generation_create_handwriting_png**](docs/TextGenerationApi.md#text_generation_create_handwriting_png) | **POST** /image/text/create/handwriting/png | Create an image of handwriting in PNG format


## Documentation For Models

 - [AgeDetectionResult](docs/AgeDetectionResult.md)
 - [ColorResult](docs/ColorResult.md)
 - [CreateHandwritingRequest](docs/CreateHandwritingRequest.md)
 - [DetectedLicensePlate](docs/DetectedLicensePlate.md)
 - [DetectedObject](docs/DetectedObject.md)
 - [DominantColorResult](docs/DominantColorResult.md)
 - [DrawPolygonInstance](docs/DrawPolygonInstance.md)
 - [DrawPolygonRequest](docs/DrawPolygonRequest.md)
 - [DrawRectangleInstance](docs/DrawRectangleInstance.md)
 - [DrawRectangleRequest](docs/DrawRectangleRequest.md)
 - [DrawTextInstance](docs/DrawTextInstance.md)
 - [DrawTextRequest](docs/DrawTextRequest.md)
 - [Face](docs/Face.md)
 - [FaceCompareResponse](docs/FaceCompareResponse.md)
 - [FaceLocateResponse](docs/FaceLocateResponse.md)
 - [FaceLocateWithLandmarksResponse](docs/FaceLocateWithLandmarksResponse.md)
 - [FaceMatch](docs/FaceMatch.md)
 - [FacePoint](docs/FacePoint.md)
 - [FaceWithLandmarks](docs/FaceWithLandmarks.md)
 - [FindSymbolResult](docs/FindSymbolResult.md)
 - [FineTextDetectionResult](docs/FineTextDetectionResult.md)
 - [FineTextItem](docs/FineTextItem.md)
 - [GenderDetectionResult](docs/GenderDetectionResult.md)
 - [ImageDescriptionResponse](docs/ImageDescriptionResponse.md)
 - [ImageMetadata](docs/ImageMetadata.md)
 - [ImageMetadataExifValue](docs/ImageMetadataExifValue.md)
 - [NsfwResult](docs/NsfwResult.md)
 - [ObjectDetectionResult](docs/ObjectDetectionResult.md)
 - [PersonWithAge](docs/PersonWithAge.md)
 - [PersonWithGender](docs/PersonWithGender.md)
 - [PolygonPoint](docs/PolygonPoint.md)
 - [RecognitionOutcome](docs/RecognitionOutcome.md)
 - [TextDetectionResult](docs/TextDetectionResult.md)
 - [TextItem](docs/TextItem.md)
 - [VehicleLicensePlateDetectionResult](docs/VehicleLicensePlateDetectionResult.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



