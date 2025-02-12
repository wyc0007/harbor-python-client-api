# CVEAllowlist

The CVE Allowlist for system or project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the allowlist | [optional] 
**project_id** | **int** | ID of the project which the allowlist belongs to.  For system level allowlist this attribute is zero. | [optional] 
**expires_at** | **int, none_type** | the time for expiration of the allowlist, in the form of seconds since epoch.  This is an optional attribute, if it&#39;s not set the CVE allowlist does not expire. | [optional] 
**items** | [**[CVEAllowlistItem]**](CVEAllowlistItem.md) |  | [optional] 
**creation_time** | **datetime** | The creation time of the allowlist. | [optional] 
**update_time** | **datetime** | The update time of the allowlist. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


