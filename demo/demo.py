from __future__ import print_function
import time
import cloudmersive_image_api_client 
from cloudmersive_image_api_client .rest import ApiException
from pprint import pprint

api_instance = cloudmersive_image_api_client.FaceApi()
image_file = 'C:\\temp\\woman-car.jpg' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = 'f0c513bc-8c00-4491-830e-3e83b015feb6'

try:
    # Crop image to face (square)
    api_response = api_instance.face_crop_first(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaceApi->face_crop_first: %s\n" % e)