#Remove-Item –path ./ –recurse
& java -jar swagger-codegen-cli-2.4.5.jar generate -i https://api.cloudmersive.com/swagger/api/image -l python -c packageconfig.json
#(Get-Content ./client/package.json).replace('v1', '1.0.1') | Set-Content ./client/package.json

# Bug fix

$newcontent = (Get-Content ./core/replace.py -Raw)
Write-Host $newcontent
(Get-Content ./cloudmersive_image_api_client/api_client.py).replace('if response_type:', $newcontent) | Set-Content ./cloudmersive_image_api_client/api_client.py
(Get-Content ./cloudmersive_image_api_client/rest.py).replace((Get-Content ./core/rest_match.py -Raw), (Get-Content ./core/rest_replace.py -Raw)) | Set-Content ./cloudmersive_image_api_client/rest.py