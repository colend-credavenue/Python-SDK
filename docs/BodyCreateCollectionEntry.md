# BodyCreateCollectionEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_no** | **int** | Installment Number | [optional] 
**due_date** | **date** | Due Date for the Installment (YYYY-MM-DD) | [optional] 
**principal** | **float** | Total principal amount paid for this installment | [optional] 
**interest** | **float** | Total interest amount paid for this installement | [optional] 
**other_charges** | **float** | Other Charges | [optional] 
**overdue_charges** | **float** | Total overdue interest paid | [optional] 
**penalty_charges** | **float** | Penalty Charges Paid | [optional] 
**fee_charges** | **float** | Fee Charges Paid | [optional] 
**bounce_charges** | **float** | Bounce charges paid | [optional] 
**amount** | **float** | Total Collection Amount | [optional] 
**paid_date** | **date** | Date when customer paid the amount (YYYY-MM-DD) | [optional] 
**investor_transfer_date** | **date** | Date when originator transferred the amount to investor (YYYY-MM-DD) | [optional] 
**reference_no** | **str** | Instrument Number of the collection received | [optional] 
**instrument_type** | **str** | Instrument Type of the collection received | [optional] 
**emi_closed** | **str** | Y / N. Input Y if the installment is closed. | [optional] 
**foreclosure** | **str** | Y / N. Input Y if the loan is foreclosed. | [optional] 
**payment_type** | **str** | Normal / Part / Advance | [optional] 
**pos** | **float** | Before the collection record to mention pos for that loan | [optional] 
**updated_rs** | [**[BodyCreateCollectionEntryUpdatedRs]**](BodyCreateCollectionEntryUpdatedRs.md) | Refer table UpdatedRs for attributes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


