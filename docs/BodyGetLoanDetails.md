# BodyGetLoanDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business** | [**BodyCreateLoanBusiness**](BodyCreateLoanBusiness.md) |  | [optional] 
**guarantors** | [**[BodyCreateLoanGuarantors]**](BodyCreateLoanGuarantors.md) | Refer table Guarantors for attributes | [optional] 
**co_applicants** | [**[BodyCreateLoanCoApplicants]**](BodyCreateLoanCoApplicants.md) | Refer table CoApplicants for attributes | [optional] 
**bank_statement** | [**BodyCreateLoanBankStatement**](BodyCreateLoanBankStatement.md) |  | [optional] 
**financial_data** | [**BodyCreateLoanFinancialData**](BodyCreateLoanFinancialData.md) |  | [optional] 
**product_id** | **str** | Product ID created in CA | [optional] 
**client_loan_id** | **str** | Loan ID as per Partner&amp;#39;s LMS | [optional] 
**purpose** | **str** | Free flowing text | [optional] 
**principal_amount** | **float** | Total loan amount in Rs (Overall amount to the borrower) | [optional] 
**interest_rate** | **float** | Reducing balance interest rate of the customer in %. This is the interest rate to be mentioned in the sanction letter as well | [optional] 
**tenure** | **int** | Tenure of the loan | [optional] 
**tenure_frequency** | **str** | Whether the tenure is monthly/yearly/weekly | [optional] 
**repayment_frequency** | **str** | Daily/Weekly/Once in 2 weeks/Monthly/Quarterly/Bullet | [optional] 
**number_of_repayments** | **int** | Number of repayments as per the repayment schedule | [optional] 
**disbursement_accounts** | [**[BodyCreateLoanDisbursementAccounts]**](BodyCreateLoanDisbursementAccounts.md) | Refer table DisbursementAccounts for attributes | [optional] 
**assets** | [**[BodyCreateLoanAssets]**](BodyCreateLoanAssets.md) | Refer table Assets for attributes | [optional] 
**references** | [**[BodyCreateLoanReferences]**](BodyCreateLoanReferences.md) | Refer table References for attributes | [optional] 
**insurance_details** | [**[BodyCreateLoanInsuranceDetails]**](BodyCreateLoanInsuranceDetails.md) | Refer table InsuranceDetails for attributes | [optional] 
**tranches** | [**[BodyCreateLoanTranches]**](BodyCreateLoanTranches.md) | Refer table Tranches for attributes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


