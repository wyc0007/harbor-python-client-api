# WebhookPolicy

The webhook policy object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The webhook policy ID. | [optional] 
**name** | **str** | The name of webhook policy. | [optional] 
**description** | **str** | The description of webhook policy. | [optional] 
**project_id** | **int** | The project ID of webhook policy. | [optional] 
**targets** | [**[WebhookTargetObject]**](WebhookTargetObject.md) |  | [optional] 
**event_types** | **[str]** |  | [optional] 
**creator** | **str** | The creator of the webhook policy. | [optional] 
**creation_time** | **datetime** | The create time of the webhook policy. | [optional] 
**update_time** | **datetime** | The update time of the webhook policy. | [optional] 
**enabled** | **bool** | Whether the webhook policy is enabled or not. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


