# ResponseCreateTrancheBureauReportData

Refer table BureauReportData for attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_of_bureau** | **str** | Cibil / Experian / Himark | [optional] 
**bureau_vintage** | **int** | Vintage in the bureau. Number of years from the first trade line | [optional] 
**bureau_score** | **int** | Bureau Score | [optional] 
**bureau_report_link** | **[str]** | Document of the bureau | [optional] 
**bureau_report_link_password** | **str** | Document of the bureau - Password | [optional] 
**bureau_json_link** | **[str]** | Bureau Json placed in a link | [optional] 
**bureau_json_link_password** | **str** | Bureau Json placed in a link - Password | [optional] 
**bureau_json** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | Refer table BureauJson for attributes | [optional] 
**commercial_bureau_score** | **int** | CRIF score | [optional] 
**commercial_bureau_score_link** | **[str]** | Commercial Bureau Document | [optional] 
**commercial_bureau_score_link_password** | **str** | Commercial Bureau Document Password | [optional] 
**partner_score_on_the_customer** | **int** | Score Captured by the Partner | [optional] 
**total_existing_obligations** | **int** | Total Existing Obligations basis the Bureau Report | [optional] 
**credit_card_limit** | **int** | Total Credit Card Limit basis the Bureau Report | [optional] 
**number_of_credit_cards** | **int** | Total Number of Credit Cards per Bureau Report | [optional] 
**number_of_unsecured_loans** | **int** | Total Number of Unsecured Loans per Bureau Report | [optional] 
**value_of_total_unsecured_loans** | **float** | Total value of unsecured loans | [optional] 
**number_of_loans** | **int** | Total Number of Loans per Bureau Report | [optional] 
**value_of_total_loans** | **float** | Total value of loans | [optional] 
**number_of_enquiries_3months** | **int** | Number of Enquiries in the Last 3 Months per Bureau Report | [optional] 
**number_of_enquiries_6months** | **int** | Number of Enquiries in the Last 6 Months per Bureau Report | [optional] 
**number_of_enquiries_12months** | **int** | Number of Enquiries in the Last 12 Months per Bureau Report | [optional] 
**number_of_writeoff_suitfiled_settled_12months** | **int** | Number of Writeoff Suitfiled Settled in the Last 12 Months | [optional] 
**max_dpd_tradeline_12months** | **int** | Maximum DPD Tradeline in the Last 12 Months | [optional] 
**max_overdue_tradeline** | **int** | Maximum Overdue Tradeline | [optional] 
**total_overdue_amount_12months** | **float** | Total Overdue Amount in the Last 12 Months | [optional] 
**loan_amount_settled_12months** | **float** | Loan Amount Settled in the Last 12 Months | [optional] 
**nature_of_loan_settled1** | **str** | The nature of past loan settlement if any (Loan 1) - Settled/ Closed/ Written-off | [optional] 
**nature_of_loan_settled2** | **str** | The nature of past loan settlement if any (Loan 2) - Settled/ Closed/ Written-off | [optional] 
**total_emi_bounces** | **int** | Total EMI Bounces | [optional] 
**emi_bounces_6months** | **int** | EMI Bounces in the Last 6 Months | [optional] 
**emi_bounces_12months** | **int** | EMI Bounces in the Last 12 Months | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


