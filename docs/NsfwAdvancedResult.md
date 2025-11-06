# NsfwAdvancedResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the classification was successfully run, false otherwise | [optional] 
**clean_result** | **bool** | True if the result was clean, false otherwise | [optional] 
**contains_nudity** | **bool** | True if the image contains nudity or sex, false otherwise | [optional] 
**contains_graphic_violence** | **bool** | True if the image contains graphic violence and/or gore, false otherwise | [optional] 
**contains_non_graphic_violence** | **bool** | True if the image contains non-graphic violence, e.g. weapons, false otherwise | [optional] 
**contains_self_harm** | **bool** | True if the image contains self-harm or suicide imagery, false otherwise | [optional] 
**contains_hate** | **bool** | True if the image contains hate, false otherwise | [optional] 
**contains_potential_illegal_activity** | **bool** | True if the image contains potentially illegal activity such as drugs, false otherwise | [optional] 
**contains_medical_imagery** | **bool** | True if the image contains medical imagery, false otherwise | [optional] 
**contains_profanity** | **bool** | True if the image contains profanity or obscenities, false otherwise | [optional] 
**score** | **float** | Score between 0.0 and 1.0.  Scores of 0.0-0.2 represent high probability safe content, while scores 0.8-1.0 represent high probability unsafe content.  Content between 0.2 and 0.8 is of increasing raciness. | [optional] 
**classification_outcome** | **str** | Classification result into four categories: SafeContent_HighProbability, UnsafeContent_HighProbability, RacyContent, SafeContent_ModerateProbability | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


