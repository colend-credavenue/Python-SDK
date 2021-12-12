# BodyCreateTranche


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tranche_number** | **int** | Tranche Number | [optional] 
**principal_amount** | **int** | Principal amount to be disbursed in the tranche | [optional] 
**differential_interest** | **int** | Broken period interest amount | [optional] 
**interest_start_date** | **date** | Pre Emi interest due date | [optional] 
**processing_fee** | **int** | Processing fee amount (Inckusive of GST) | [optional] 
**stamp_duty** | **int** | Stamp duty amount | [optional] 
**insurance_charges** | **int** | Insurance premium inclusive of GST | [optional] 
**documentation_charges** | **int** | Total documentation charges inclusive of GST | [optional] 
**other_charges** | **int** | Any other charges inclusive of GST | [optional] 
**closing_loan_principal** | **int** | Balance principal amount after this tranche | [optional] 
**tranche_doc_link** | **str** | Link to the corresponding document | [optional] 
**tranche_doc_link_password** | **str** | Link to the corresponding document | [optional] 
**disbursement_accounts** | [**[ResponseCreateTrancheDisbursementAccounts]**](ResponseCreateTrancheDisbursementAccounts.md) | Refer table DisbursementAccounts for attributes | [optional] 
**loan_data** | [**[ResponseCreateTrancheLoanData]**](ResponseCreateTrancheLoanData.md) | Refer table LoanData for attributes | [optional] 
**bureau_report_data** | [**ResponseCreateTrancheBureauReportData**](ResponseCreateTrancheBureauReportData.md) |  | [optional] 
**client_loan_id** | **str** | Loan ID as per Partner&amp;#39;s LMS | [optional] 
**business_data** | [**ResponseCreateTrancheBusinessData**](ResponseCreateTrancheBusinessData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


