# BodyUpdateLoan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_amount** | **float** | Total Loan Amount to the Borrower (in Rupees) | [optional] 
**loan_amount** | **float** | Total Loan Amount | [optional] 
**interest_rate** | **float** | Reducing balance interest rate of the customer in %. This is the interest rate to be mentioned in the sanction letter as well | [optional] 
**tenure** | **int** | Tenure of the loan | [optional] 
**tenure_frequency** | **str** | Daily / Weekly / Monthly | [optional] 
**repayment_frequency** | **str** | Daily / Weekly / Monthly / Bullet | [optional] 
**number_of_repayments** | **int** | Number of repayments as per the repayment schedule | [optional] 
**disbursement_accounts** | [**[BodyUpdateLoanDisbursementAccounts]**](BodyUpdateLoanDisbursementAccounts.md) | Refer table DisbursementAccounts for attributes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


