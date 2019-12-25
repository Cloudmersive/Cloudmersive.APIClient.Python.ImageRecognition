# ImageMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation was successful, false otherwise | [optional] 
**is_valid_image** | **bool** | True if the input image is a valid image file, false otherwise | [optional] 
**file_format** | **str** | File format of the image | [optional] 
**width** | **int** | Width of the image in pixels | [optional] 
**height** | **int** | Height of the image in pixels | [optional] 
**bit_depth** | **int** | Bits per pixel | [optional] 
**has_transparency** | **bool** | True if the image has transaprency in the form of an alpha channel, false otherwise | [optional] 
**color_space** | **str** | Color space of the image | [optional] 
**exif_profile_name** | **str** | Name of the EXIF profile used | [optional] 
**exif_values** | [**list[ImageMetadataExifValue]**](ImageMetadataExifValue.md) | EXIF tags and values embedded in the image | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


