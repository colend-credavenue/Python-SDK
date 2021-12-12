# credavenue_colending.ColendingApi

All URIs are relative to *https://colend-uat-01-api.credavenue.in/colending*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loan**](ColendingApi.md#create_loan) | **POST** /clients/{client_name}/api/v2/loans | #Create Loan
[**get_loan_details**](ColendingApi.md#get_loan_details) | **GET** /clients/{client_name}/api/v2/loans/{loan_id} | #Get Loan Details
[**update_loan**](ColendingApi.md#update_loan) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id} | #Update Loan
[**agreement_signed**](ColendingApi.md#agreement_signed) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/agreement_signed | #Agreement Signed
[**property_review**](ColendingApi.md#property_review) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/property_review | #Property Review
[**disburse_loan**](ColendingApi.md#disburse_loan) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/disburse | #Disburse Loan
[**update_post_disbursement**](ColendingApi.md#update_post_disbursement) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/update_post_disbursement | #Update Post Disbursement
[**get_collection_details**](ColendingApi.md#get_collection_details) | **GET** /clients/{client_name}/api/v2/loans/{loan_id}/payments | Get Collection Details
[**create_collection_entry**](ColendingApi.md#create_collection_entry) | **POST** /clients/{client_name}/api/v2/loans/{loan_id}/payments/record_payment | #Create Collection Entry
[**update_collection_entry**](ColendingApi.md#update_collection_entry) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/payments/{payment_id} | #Update Collection Entry
[**get_repayment_schedule_details**](ColendingApi.md#get_repayment_schedule_details) | **GET** /clients/{client_name}/api/v2/loans/{loan_id}/rs | #Get Repayment Schedule Details
[**create_repayment_schedule**](ColendingApi.md#create_repayment_schedule) | **POST** /clients/{client_name}/api/v2/loans/{loan_id}/rs | #Create Repayment Schedule
[**update_repayment_schedule**](ColendingApi.md#update_repayment_schedule) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/rs | #Update Repayment Schedule
[**create_advance_collection**](ColendingApi.md#create_advance_collection) | **POST** /clients/{client_name}/api/v2/loans/{loan_id}/advance_payments | #Create Advance Collection
[**update_advance_collection**](ColendingApi.md#update_advance_collection) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/advance_payments/{advance_payment_id} | #Update Advance Collection
[**upload_interest_accruals**](ColendingApi.md#upload_interest_accruals) | **POST** /clients/{client_name}/api/v2/interest_accruals | #Upload Interest Accruals
[**approve_fund_transfer**](ColendingApi.md#approve_fund_transfer) | **PUT** /clients/{client_name}/api/v2/loans/{loan_id}/approve_fund_transfer | #Approve Fund Transfer
[**get_interest_accrual**](ColendingApi.md#get_interest_accrual) | **GET** /clients/{client_name}/api/v2/interest_accruals/{file_id} | #Get Interest Accrual
[**create_tranche**](ColendingApi.md#create_tranche) | **POST** /clients/{client_name}/api/v2/loans/{loan_id}/tranches | #Create Tranche
[**get_tranche_details**](ColendingApi.md#get_tranche_details) | **GET** /clients/{client_name}/api/v2/loans/{loan_id}/tranches/{id} | #Get Tranche Details



# **agreement_signed**
> AgreementSignedSuccess agreement_signed(product_id, client_name, loan_id, body_agreement_signed)

#Agreement Signed

Agreement Signed API - This endpoint can be used to update the loan status to agreement signed.  **Expected Loan Status: "approved"**

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>sanction_letter_link</td>     <td>array</td>     <td></td>          <td>Sanction letter issued to the customer in joint/lenders letter head</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>sanction_letter_link_password</td>     <td>string</td>     <td></td>          <td>Sanction letter issued to the customer in joint/lenders letter head - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>self_declaration_form_link</td>     <td>array</td>     <td></td>          <td>Self declaration form link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>self_declaration_form_link_password</td>     <td>string</td>     <td></td>          <td>Self declaration form link password</td>       <td>12345678</td>  </tr>        <tr>     <td>fatca_declaration_link</td>     <td>array</td>     <td></td>          <td>FATCA declaration</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>fatca_declaration_link_password</td>     <td>string</td>     <td></td>          <td>FATCA declaration link password</td>       <td>12345678</td>  </tr>        <tr>     <td>entire_set_of_loan_agreements_link</td>     <td>array</td>     <td></td>          <td>Entire loan agreement kit</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>entire_set_of_loan_agreements_link_password</td>     <td>string</td>     <td></td>          <td>Entire loan agreement kit password</td>       <td>12345678</td>  </tr>        <tr>     <td>dpn_link</td>     <td>array</td>     <td></td>          <td>DPN Image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>dpn_link_password</td>     <td>string</td>     <td></td>          <td>DPN Image password</td>       <td>12345678</td>  </tr>        <tr>     <td>drf_link</td>     <td>array</td>     <td></td>          <td>DRF Image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>drf_link_password</td>     <td>string</td>     <td></td>          <td>DRF Image password</td>       <td>12345678</td>  </tr>        <tr>     <td>nach_enach_mandate_link</td>     <td>array</td>     <td></td>          <td>Nach Enach Mandate Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>nach_enach_mandate_link_password</td>     <td>string</td>     <td></td>          <td>Nach Enach Mandate Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>credit_discussion_mail_link</td>     <td>array</td>     <td></td>          <td>Credit Discussion Mail Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>credit_discussion_mail_link_password</td>     <td>string</td>     <td></td>          <td>Credit Discussion Mail Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>field_verification_report_link</td>     <td>array</td>     <td></td>          <td>Field Verification Report Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>field_verification_report_link_password</td>     <td>string</td>     <td></td>          <td>Field Verification Report Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>tele_verification_report_link</td>     <td>array</td>     <td></td>          <td>Tele Verification Report Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>tele_verification_report_link_password</td>     <td>string</td>     <td></td>          <td>Tele Verification Report Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>vehicle_inspection_report_link</td>     <td>array</td>     <td></td>          <td>Vehicle Inspection Report Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>vehicle_inspection_report_link_password</td>     <td>string</td>     <td></td>          <td>Vehicle Inspection Report Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>insurance_application_form_link</td>     <td>array</td>     <td></td>          <td>Insurance Application Form Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>insurance_application_form_link_password</td>     <td>string</td>     <td></td>          <td>Insurance Application Form Link Password</td>       <td>12345678</td>  </tr>    </tbody>       </table>    #   > <h4>Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>422</td>     <td>Unprocessable Entity</td>     <td>Client Loan Already Taken /  Product Not Found /  Document not found/accessible</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.agreement_signed_success import AgreementSignedSuccess
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.body_agreement_signed import BodyAgreementSigned
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_agreement_signed = BodyAgreementSigned(
        sanction_letter_link=[
            "sanction_letter_link_example",
        ],
        sanction_letter_link_password="sanction_letter_link_password_example",
        self_declaration_form_link=[
            "self_declaration_form_link_example",
        ],
        self_declaration_form_link_password="self_declaration_form_link_password_example",
        fatca_declaration_link=[
            "fatca_declaration_link_example",
        ],
        fatca_declaration_link_password="fatca_declaration_link_password_example",
        entire_set_of_loan_agreements_link=[
            "entire_set_of_loan_agreements_link_example",
        ],
        entire_set_of_loan_agreements_link_password="entire_set_of_loan_agreements_link_password_example",
        dpn_link=[
            "dpn_link_example",
        ],
        dpn_link_password="dpn_link_password_example",
        drf_link=[
            "drf_link_example",
        ],
        drf_link_password="drf_link_password_example",
        nach_enach_mandate_link=[
            "nach_enach_mandate_link_example",
        ],
        nach_enach_mandate_link_password="nach_enach_mandate_link_password_example",
        credit_discussion_mail_link=[
            "credit_discussion_mail_link_example",
        ],
        credit_discussion_mail_link_password="credit_discussion_mail_link_password_example",
        field_verification_report_link=[
            "field_verification_report_link_example",
        ],
        field_verification_report_link_password="field_verification_report_link_password_example",
        tele_verification_report_link=[
            "tele_verification_report_link_example",
        ],
        tele_verification_report_link_password="tele_verification_report_link_password_example",
        vehicle_inspection_report_link=[
            "vehicle_inspection_report_link_example",
        ],
        vehicle_inspection_report_link_password="vehicle_inspection_report_link_password_example",
        insurance_application_form_link=[
            "insurance_application_form_link_example",
        ],
        insurance_application_form_link_password="insurance_application_form_link_password_example",
    ) # BodyAgreementSigned | 

    # example passing only required values which don't have defaults set
    try:
        # #Agreement Signed
        api_response = api_instance.agreement_signed(product_id, client_name, loan_id, body_agreement_signed)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->agreement_signed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_agreement_signed** | [**BodyAgreementSigned**](BodyAgreementSigned.md)|  |

### Return type

[**AgreementSignedSuccess**](AgreementSignedSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_fund_transfer**
> RequestSuccess approve_fund_transfer(product_id, client_name, loan_id, body)

#Approve Fund Transfer

Approve Fund Transfer API

Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.request_success import RequestSuccess
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # #Approve Fund Transfer
        api_response = api_instance.approve_fund_transfer(product_id, client_name, loan_id, body)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->approve_fund_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**RequestSuccess**](RequestSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_advance_collection**
> AgreementSignedSuccess create_advance_collection(product_id, client_name, loan_id, body_create_advance_collection)

#Create Advance Collection

Advance Collection API - This endpoint can be used to create an advance transaction for a loan that can be utilized in future payments later

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Advance Amount</td>       <td>10000.0</td>  </tr>        <tr>     <td>transaction_date</td>     <td>string</td>     <td>date</td>          <td>Date when customer paid the amount (YYYY-MM-DD)</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>investor_transfer_date</td>     <td>string</td>     <td>date</td>          <td>Date when originator transferred the amount to investor (YYYY-MM-DD)</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>instrument_number</td>     <td>string</td>     <td></td>          <td>UTR / Cheque Number</td>       <td>UTR12345</td>  </tr>        <tr>     <td>instrument_type</td>     <td>string</td>     <td></td>          <td>RTGS / NEFT / UPI / Cheque</td>       <td>NEFT</td>  </tr>        <tr>     <td>advance_outstanding</td>     <td>number</td>     <td>float</td>          <td>Before this collection record to mention advance outstanding for that loan</td>       <td>5000.0</td>  </tr>        <tr>     <td>transaction_type</td>     <td>string</td>     <td></td>          <td>Credit / Refund</td>       <td>Credit</td>  </tr>        <tr>     <td>comment</td>     <td>string</td>     <td></td>          <td>comment</td>       <td>Advance payment</td>  </tr>    </tbody>       </table>    Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.body_create_advance_collection import BodyCreateAdvanceCollection
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.agreement_signed_success import AgreementSignedSuccess
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_create_advance_collection = BodyCreateAdvanceCollection(
        amount=3.14,
        transaction_date=dateutil_parser('1970-01-01').date(),
        investor_transfer_date=dateutil_parser('1970-01-01').date(),
        instrument_number="instrument_number_example",
        instrument_type="instrument_type_example",
        advance_outstanding=3.14,
        transaction_type="transaction_type_example",
        comment="comment_example",
    ) # BodyCreateAdvanceCollection | 

    # example passing only required values which don't have defaults set
    try:
        # #Create Advance Collection
        api_response = api_instance.create_advance_collection(product_id, client_name, loan_id, body_create_advance_collection)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->create_advance_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_create_advance_collection** | [**BodyCreateAdvanceCollection**](BodyCreateAdvanceCollection.md)|  |

### Return type

[**AgreementSignedSuccess**](AgreementSignedSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection_entry**
> CreateCollectionSuccess create_collection_entry(product_id, client_name, loan_id, body_create_collection_entry)

#Create Collection Entry

Create Collection API - This API endpoint can be used to create a collection entry.  You will get a 201 HTTP response if the collection entry gets created successfully.  You can even cross verify it by checking the principal outstanding in Loan Details Response.

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>installment_no</td>     <td>integer</td>     <td></td>          <td>Installment Number</td>       <td>1</td>  </tr>        <tr>     <td>due_date</td>     <td>string</td>     <td>date</td>          <td>Due Date for the Installment (YYYY-MM-DD)</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>principal</td>     <td>number</td>     <td>float</td>          <td>Total principal amount paid for this installment</td>       <td>10000.0</td>  </tr>        <tr>     <td>interest</td>     <td>number</td>     <td>float</td>          <td>Total interest amount paid for this installement</td>       <td>100.0</td>  </tr>        <tr>     <td>other_charges</td>     <td>number</td>     <td>float</td>          <td>Other Charges</td>       <td>100.0</td>  </tr>        <tr>     <td>overdue_charges</td>     <td>number</td>     <td>float</td>          <td>Total overdue interest paid</td>       <td>100.0</td>  </tr>        <tr>     <td>penalty_charges</td>     <td>number</td>     <td>float</td>          <td>Penalty Charges Paid</td>       <td>100.0</td>  </tr>        <tr>     <td>fee_charges</td>     <td>number</td>     <td>float</td>          <td>Fee Charges Paid</td>       <td>100.0</td>  </tr>        <tr>     <td>bounce_charges</td>     <td>number</td>     <td>float</td>          <td>Bounce charges paid</td>       <td>100.0</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Total Collection Amount</td>       <td>10600.0</td>  </tr>        <tr>     <td>paid_date</td>     <td>string</td>     <td>date</td>          <td>Date when customer paid the amount (YYYY-MM-DD)</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>investor_transfer_date</td>     <td>string</td>     <td>date</td>          <td>Date when originator transferred the amount to investor (YYYY-MM-DD)</td>       <td>2022-01-02</td>  </tr>        <tr>     <td>reference_no</td>     <td>string</td>     <td></td>          <td>Instrument Number of the collection received</td>       <td>UTR123456</td>  </tr>        <tr>     <td>instrument_type</td>     <td>string</td>     <td></td>          <td>Instrument Type of the collection received</td>       <td>NEFT</td>  </tr>        <tr>     <td>emi_closed</td>     <td>string</td>     <td></td>          <td>Y / N. Input Y if the installment is closed.</td>       <td>Y</td>  </tr>        <tr>     <td>foreclosure</td>     <td>string</td>     <td></td>          <td>Y / N. Input Y if the loan is foreclosed.</td>       <td>Y</td>  </tr>        <tr>     <td>payment_type</td>     <td>string</td>     <td></td>          <td>Normal / Part / Advance</td>       <td>Normal</td>  </tr>        <tr>     <td>pos</td>     <td>number</td>     <td>float</td>          <td>Before the collection record to mention pos for that loan</td>       <td>100000.0</td>  </tr>        <tr>     <td>updated_rs</td>     <td>array</td>     <td></td>          <td>Refer table UpdatedRs for attributes</td>       <td>[{&quot;installment_no&quot;:1,&quot;due_date&quot;:&quot;2021-01-02&quot;,&quot;principal&quot;:10000.0,&quot;interest&quot;:100.0,&quot;amount&quot;:10100.0,&quot;pos&quot;:10000.0,&quot;comment&quot;:&quot;Payment&quot;},{&quot;installment_no&quot;:1,&quot;due_date&quot;:&quot;2021-01-02&quot;,&quot;principal&quot;:10000.0,&quot;interest&quot;:100.0,&quot;amount&quot;:10100.0,&quot;pos&quot;:10000.0,&quot;comment&quot;:&quot;Payment&quot;}]</td>  </tr>    </tbody>       </table>   <h4>UpdatedRs</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>installment_no</td>     <td>integer</td>     <td></td>          <td>Installment Number</td>       <td>1</td>  </tr>        <tr>     <td>due_date</td>     <td>string</td>     <td>date</td>          <td>Due Date for Installment (YYYY-MM-DD)</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>principal</td>     <td>number</td>     <td>float</td>          <td>Total Principal Amount</td>       <td>10000.0</td>  </tr>        <tr>     <td>interest</td>     <td>number</td>     <td>float</td>          <td>Interest</td>       <td>100.0</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Installment amount</td>       <td>10100.0</td>  </tr>        <tr>     <td>pos</td>     <td>number</td>     <td>float</td>          <td>Closing Principal Outstanding</td>       <td>10000.0</td>  </tr>        <tr>     <td>comment</td>     <td>string</td>     <td></td>          <td>comment</td>       <td>Payment</td>  </tr>    </tbody>       </table>          # Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>201</td>     <td>Created</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters/   Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>  <tbody>      <tr>     <td>422</td>     <td>Unprocessable Entity</td>     <td>Sum of collection payments principal for the installment should be equal to repayment schedule's principal / Sum of collection payments interest for the installment should be equal to repayment schedule's interest/ Amount is not equal to sum of Principal, Interest, Overdue Charges, Other Charges, Fee Charges, Bounce Charges/ The installment is already paid / Investor Transfer Date cannot be in the future/ Investor Transfer Date cannot be a Sunday/ Investor transfer date cannot be less than customer transfer date/ Paid date can't be in the future/ Paid date can't be before loan disbursement/ Payment's due date does not match repayment schedule's due date/ Previous cycle is unpaid/ Invalid Loan Status: Loan is not disbursed</td>   </tr>    </tbody>  </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.body_create_collection_entry import BodyCreateCollectionEntry
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.create_collection_success import CreateCollectionSuccess
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_create_collection_entry = BodyCreateCollectionEntry(
        installment_no=1,
        due_date=dateutil_parser('1970-01-01').date(),
        principal=3.14,
        interest=3.14,
        other_charges=3.14,
        overdue_charges=3.14,
        penalty_charges=3.14,
        fee_charges=3.14,
        bounce_charges=3.14,
        amount=3.14,
        paid_date=dateutil_parser('1970-01-01').date(),
        investor_transfer_date=dateutil_parser('1970-01-01').date(),
        reference_no="reference_no_example",
        instrument_type="instrument_type_example",
        emi_closed="emi_closed_example",
        foreclosure="foreclosure_example",
        payment_type="payment_type_example",
        pos=3.14,
        updated_rs=[
            BodyCreateCollectionEntryUpdatedRs(
                installment_no=1,
                due_date=dateutil_parser('1970-01-01').date(),
                principal=3.14,
                interest=3.14,
                amount=3.14,
                pos=3.14,
                comment="comment_example",
            ),
        ],
    ) # BodyCreateCollectionEntry | 

    # example passing only required values which don't have defaults set
    try:
        # #Create Collection Entry
        api_response = api_instance.create_collection_entry(product_id, client_name, loan_id, body_create_collection_entry)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->create_collection_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_create_collection_entry** | [**BodyCreateCollectionEntry**](BodyCreateCollectionEntry.md)|  |

### Return type

[**CreateCollectionSuccess**](CreateCollectionSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 201 Created |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan**
> CreateLoanSuccess create_loan(product_id, client_name, body_create_loan)

#Create Loan

#Create Loan

Create Loan   This API endpoint can be used to create a loan.  interest_rate: Rate of interest percent per annum  All link fields should have a valid accessible URL or "NA".  States should be in INDIAN_STATES array (refer at the end of the table).

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>customer_type</td>     <td>string</td>     <td></td>          <td>Individual / Corporate</td>       <td>individual</td>  </tr>        <tr>     <td>customer_category</td>     <td>string</td>     <td></td>          <td>Salaried, Self-Empolyed</td>       <td>salaried</td>  </tr>        <tr>     <td>client_customer_id</td>     <td>string</td>     <td></td>          <td>Customer id as per partners CRM/LOS</td>       <td>CA_1234</td>  </tr>        <tr>     <td>title</td>     <td>string</td>     <td></td>          <td>Mr / Ms</td>       <td>Mr</td>  </tr>        <tr>     <td>first_name</td>     <td>string</td>     <td></td>          <td>First Name of the Customer</td>       <td>Neeraj</td>  </tr>        <tr>     <td>middle_name</td>     <td>string</td>     <td></td>          <td>Middle Name of the Customer</td>       <td>Kumar</td>  </tr>        <tr>     <td>last_name</td>     <td>string</td>     <td></td>          <td>Last Name of the Customer</td>       <td>Chopra</td>  </tr>        <tr>     <td>gender</td>     <td>string</td>     <td></td>          <td>M / F / O</td>       <td>M</td>  </tr>        <tr>     <td>date_of_birth</td>     <td>string</td>     <td>date</td>          <td>Date of birth in YYYY-MM-DD</td>       <td>1995-12-05</td>  </tr>        <tr>     <td>age</td>     <td>integer</td>     <td></td>          <td>Age in years</td>       <td>26</td>  </tr>        <tr>     <td>mobile_number</td>     <td>integer</td>     <td></td>          <td>Mobile Number of the Customer (10 digits)</td>       <td>9876543210</td>  </tr>        <tr>     <td>phone_number</td>     <td>integer</td>     <td></td>          <td>Contact Number of the Customer</td>       <td>4412345678</td>  </tr>        <tr>     <td>email</td>     <td>string</td>     <td></td>          <td>Permanent Email id of the Customer</td>       <td>minato@gmail.com</td>  </tr>        <tr>     <td>official_email_id</td>     <td>string</td>     <td></td>          <td>Official Email ID of the Customer</td>       <td>minato_namikaze@credavenue.com</td>  </tr>        <tr>     <td>place_of_birth</td>     <td>string</td>     <td></td>          <td>Place of birth of the Customer</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_address</td>     <td>string</td>     <td></td>          <td>Current address of the applicant. Free flowing text</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>current_village</td>     <td>string</td>     <td></td>          <td>Village in which applicant is currently residing. Free flowing for now</td>       <td>Vedaranyam</td>  </tr>        <tr>     <td>current_city_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for the current city</td>       <td>tier_1</td>  </tr>        <tr>     <td>current_city</td>     <td>string</td>     <td></td>          <td>City in which applicant is currently residing. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_district</td>     <td>string</td>     <td></td>          <td>District in which applicant is currently residing. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_state</td>     <td>string</td>     <td></td>          <td>State in which applicant is currently residing. Free flowing for now</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>current_country</td>     <td>string</td>     <td></td>          <td>Country in which applicant is currently residing. Free flowing for now</td>       <td>India</td>  </tr>        <tr>     <td>current_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_current_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>rented</td>  </tr>        <tr>     <td>years_of_stay_in_current_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the current address</td>       <td>5</td>  </tr>        <tr>     <td>permanent_address</td>     <td>string</td>     <td></td>          <td>Permanent address of the customer. Free flowing for now</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>permanent_city</td>     <td>string</td>     <td></td>          <td>Permanent city of the customer. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_city_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for the permanent city</td>       <td>tier_1</td>  </tr>        <tr>     <td>permanent_district</td>     <td>string</td>     <td></td>          <td>Permanent district of the customer. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_state</td>     <td>string</td>     <td></td>          <td>Permanent state of the customer. Free flowing for now</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>permanent_pincode</td>     <td>integer</td>     <td></td>          <td>Permanent pincode of the customer. Free flowing for now</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_permanent_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>owned</td>  </tr>        <tr>     <td>years_of_stay_in_permanent_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the permanent address</td>       <td>5</td>  </tr>        <tr>     <td>mailing_address</td>     <td>string</td>     <td></td>          <td>Mailing address of the customer. Free flowing text</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>marital_status</td>     <td>string</td>     <td></td>          <td>married / unmarried</td>       <td>unmarried</td>  </tr>        <tr>     <td>religion</td>     <td>string</td>     <td></td>          <td>Religion of customer. Free flow text</td>       <td>Hindu</td>  </tr>        <tr>     <td>nationality</td>     <td>string</td>     <td></td>          <td>Nationality of customer. Free flow text</td>       <td>indian</td>  </tr>        <tr>     <td>father_name</td>     <td>string</td>     <td></td>          <td>Father name of customer. Free flow text</td>       <td>Dan Kato</td>  </tr>        <tr>     <td>mother_name</td>     <td>string</td>     <td></td>          <td>Mother name of customer; Free flow text</td>       <td>Tsunade Senju</td>  </tr>        <tr>     <td>spouse_name</td>     <td>string</td>     <td></td>          <td>Spouse name of customer; Free flow text</td>       <td>Kushina Uzumaki</td>  </tr>        <tr>     <td>education_qualification</td>     <td>string</td>     <td></td>          <td>Educational Qualifications</td>       <td>MBA</td>  </tr>        <tr>     <td>net_monthly_income</td>     <td>number</td>     <td>float</td>          <td>Monthly Income of the Customer (in Rupees)</td>       <td>10000.0</td>  </tr>        <tr>     <td>annual_income</td>     <td>number</td>     <td>float</td>          <td>Annual income of the customer in number (don’t convert into thousand/lacs etc)</td>       <td>120000.0</td>  </tr>        <tr>     <td>no_of_dependants</td>     <td>integer</td>     <td></td>          <td>Number of dependants</td>       <td>3</td>  </tr>        <tr>     <td>occupation</td>     <td>string</td>     <td></td>          <td>salaried / business / retired / self_employed and others</td>       <td>salaried</td>  </tr>        <tr>     <td>partner_score_on_the_customer</td>     <td>number</td>     <td>float</td>          <td>Partner score</td>       <td>3.0</td>  </tr>        <tr>     <td>politically_exposed</td>     <td>string</td>     <td></td>          <td>Political Exposure of the Customer</td>       <td>f</td>  </tr>        <tr>     <td>income_source</td>     <td>string</td>     <td></td>          <td>Cash / Cheque / Fund transfer</td>       <td>Cash</td>  </tr>        <tr>     <td>applicant_profession</td>     <td>string</td>     <td></td>          <td>Profession of the Customer</td>       <td>IT Consultant</td>  </tr>        <tr>     <td>caution_negative_profile</td>     <td>string</td>     <td></td>          <td>Is the customer categories as a negative profile?</td>       <td>t</td>  </tr>        <tr>     <td>udyam_number</td>     <td>string</td>     <td></td>          <td>Udyam Number of the Customer</td>       <td>UDYAM-UP-00-0123456</td>  </tr>        <tr>     <td>pan_check</td>     <td>string</td>     <td></td>          <td>Result of the pan check</td>       <td>Success</td>  </tr>        <tr>     <td>dedupe_status</td>     <td>string</td>     <td></td>          <td>Result of the dedupe</td>       <td>Failed</td>  </tr>        <tr>     <td>pan_number</td>     <td>string</td>     <td></td>          <td>PAN number of customer</td>       <td>BMMPH9018G</td>  </tr>        <tr>     <td>pan_number_link</td>     <td>array</td>     <td></td>          <td>PAN image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>pan_number_link_password</td>     <td>string</td>     <td></td>          <td>PAN image password</td>       <td>12345678</td>  </tr>        <tr>     <td>form_60_link</td>     <td>array</td>     <td></td>          <td>Form 60 If applicable</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>form_60_link_password</td>     <td>string</td>     <td></td>          <td>Form 60 password If applicable</td>       <td>12345678</td>  </tr>        <tr>     <td>aadhar_number</td>     <td>string</td>     <td></td>          <td>Aadhar number of customer</td>       <td>794065231234</td>  </tr>        <tr>     <td>aadhar_number_link</td>     <td>array</td>     <td></td>          <td>Aadhar image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aadhar_number_link_password</td>     <td>string</td>     <td></td>          <td>Aadhar image password</td>       <td>12345678</td>  </tr>        <tr>     <td>voter_id_number</td>     <td>string</td>     <td></td>          <td>Voter ID Number of customer</td>       <td>RTG2291234</td>  </tr>        <tr>     <td>voting_id_link</td>     <td>array</td>     <td></td>          <td>Voter ID image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>voting_id_link_password</td>     <td>string</td>     <td></td>          <td>Voter ID image password</td>       <td>12345678</td>  </tr>        <tr>     <td>driving_license_number</td>     <td>string</td>     <td></td>          <td>Driving license number of customer</td>       <td>TN0112345</td>  </tr>        <tr>     <td>driving_license_number_link</td>     <td>array</td>     <td></td>          <td>Driving License image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>driving_license_number_link_password</td>     <td>string</td>     <td></td>          <td>Driving license image password</td>       <td>12345678</td>  </tr>        <tr>     <td>driving_license_expiry_date</td>     <td>string</td>     <td>date</td>          <td>Expiry date of driving license</td>       <td>2000-10-01</td>  </tr>        <tr>     <td>passport_number</td>     <td>string</td>     <td></td>          <td>Passport number of customer</td>       <td>L4018345</td>  </tr>        <tr>     <td>passport_number_link</td>     <td>array</td>     <td></td>          <td>Passport image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>passport_number_link_password</td>     <td>string</td>     <td></td>          <td>Passport image password</td>       <td>12345678</td>  </tr>        <tr>     <td>video_image_link</td>     <td>array</td>     <td></td>          <td>Video KYC of the Applicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_image_link_password</td>     <td>string</td>     <td></td>          <td>Video KYC link password</td>       <td>12345678</td>  </tr>        <tr>     <td>video_kyc_detail</td>     <td>object</td>     <td></td>     <td>Refer table VideoKycDetail for attributes</td>       <td>{&quot;profile_id&quot;:&quot;AB12345&quot;,&quot;account_id&quot;:&quot;AB12345&quot;,&quot;key&quot;:&quot;abc@123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}</td>  </tr>        <tr>     <td>other_kyc_number</td>     <td>string</td>     <td></td>          <td>KYC Number of the Customer</td>       <td>ABC1234</td>  </tr>        <tr>     <td>other_kyc_link</td>     <td>array</td>     <td></td>          <td>KYC Image of the Customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_kyc_link_password</td>     <td>string</td>     <td></td>          <td>KYC Image link password</td>       <td>12345678</td>  </tr>        <tr>     <td>rent_agreement_link</td>     <td>array</td>     <td></td>          <td>KYC number of customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>rent_agreement_link_password</td>     <td>string</td>     <td></td>          <td>Rent agreement link password</td>       <td>12345678</td>  </tr>        <tr>     <td>utility_bills_link</td>     <td>array</td>     <td></td>          <td>Utility bills link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>utility_bills_link_password</td>     <td>string</td>     <td></td>          <td>Utility bills link password</td>       <td>12345678</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo Image of the Customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link_password</td>     <td>string</td>     <td></td>          <td>Photo Image password</td>       <td>12345678</td>  </tr>        <tr>     <td>employer_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for  the employer</td>       <td>tier_1</td>  </tr>        <tr>     <td>employer_category</td>     <td>string</td>     <td></td>          <td>Category of the employer</td>       <td>Private</td>  </tr>        <tr>     <td>employment_type</td>     <td>string</td>     <td></td>          <td>salaried / self_employed</td>       <td>self_employed</td>  </tr>        <tr>     <td>employment_details_name</td>     <td>string</td>     <td></td>          <td>Employer name. Free flowing text</td>       <td>Credavenue</td>  </tr>        <tr>     <td>employment_details_address</td>     <td>string</td>     <td></td>          <td>Office address. Free flowing text</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>employment_details_years_of_experience</td>     <td>number</td>     <td>float</td>          <td>Applicant Number of years in the current organization</td>       <td>5.0</td>  </tr>        <tr>     <td>employment_details_designation</td>     <td>string</td>     <td></td>          <td>Designation in current role, free flowing text</td>       <td>Manager</td>  </tr>        <tr>     <td>employement_vintage_current_organisation</td>     <td>integer</td>     <td></td>          <td>No of Years in the same Organisation</td>       <td>3</td>  </tr>        <tr>     <td>total_work_experience</td>     <td>number</td>     <td>float</td>          <td>Total years of experience</td>       <td>5.0</td>  </tr>        <tr>     <td>payslip_link</td>     <td>array</td>     <td></td>          <td>Last three month pay slip</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>payslip_link_password</td>     <td>string</td>     <td></td>          <td>Last three month pay slip link password</td>       <td>12345678</td>  </tr>        <tr>     <td>tds_certificate_link</td>     <td>array</td>     <td></td>          <td>Last Three Year TDS Certificate Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>tds_certificate_link_password</td>     <td>string</td>     <td></td>          <td>Last Three Year TDS Certificate Link</td>       <td>12345678</td>  </tr>        <tr>     <td>business</td>     <td>object</td>     <td></td>    <td>Refer table Business for attributes</td>       <td>{&quot;name_of_business&quot;:&quot;Credavenue&quot;,&quot;nature_of_business&quot;:&quot;Electronics&quot;,&quot;type_of_constitution&quot;:&quot;partnership&quot;,&quot;type_of_ownership&quot;:&quot;type_of_ownership_35&quot;,&quot;registration_date&quot;:&quot;1995-01-01&quot;,&quot;incorporation_date&quot;:&quot;1995-01-01&quot;,&quot;industry_type&quot;:&quot;trading&quot;,&quot;sector_type&quot;:&quot;Financial services&quot;,&quot;sub_sector_type&quot;:&quot;Banking&quot;,&quot;business_vintage&quot;:4,&quot;business_registered_office_address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;business_registered_office_district&quot;:&quot;Chennai&quot;,&quot;business_registered_office_city&quot;:&quot;Chennai&quot;,&quot;business_registered_office_state&quot;:&quot;tamil_nadu&quot;,&quot;business_registered_office_pincode&quot;:600025,&quot;business_mailing_office_address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;business_mailing_office_city&quot;:&quot;Chennai&quot;,&quot;business_mailing_office_state&quot;:&quot;Chennai&quot;,&quot;business_mailing_office_pincode&quot;:600025,&quot;business_registered_office_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_registered_office_link_password&quot;:&quot;12345678&quot;,&quot;business_mailing_office_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_mailing_office_link_password&quot;:&quot;12345678&quot;,&quot;business_phone_number&quot;:[9876543210,9876543210],&quot;business_email_id&quot;:[&quot;holmes@credavenue.com&quot;,&quot;holmes@credavenue.com&quot;],&quot;business_partner_score&quot;:3.0,&quot;business_pan_number&quot;:&quot;BMMPG9018G&quot;,&quot;business_pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_pan_link_password&quot;:&quot;12345678&quot;,&quot;business_rc_number&quot;:&quot;U72200MH2009PLC123456&quot;,&quot;business_rc_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_rc_link_password&quot;:&quot;12345678&quot;,&quot;business_gst_number&quot;:&quot;29ABCDE1234F2Z5&quot;,&quot;business_gst_copy_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_gst_copy_link_password&quot;:&quot;12345678&quot;,&quot;business_udyog_aadhar_number&quot;:&quot;794065346725&quot;,&quot;business_udyog_aadhar_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_udyog_aadhar_link_password&quot;:&quot;12345678&quot;,&quot;business_ssi_number&quot;:&quot;7589297314&quot;,&quot;business_ssi_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_ssi_link_password&quot;:&quot;12345678&quot;,&quot;business_shops_est_number&quot;:&quot;2017086025&quot;,&quot;business_shops_est_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_shops_est_link_password&quot;:&quot;12345678&quot;,&quot;business_factory_regn_number&quot;:&quot;TVEIQ0615232&quot;,&quot;business_factory_regn_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_factory_regn_link_password&quot;:&quot;12345678&quot;,&quot;business_trade_license_number&quot;:&quot;EA131102014709112&quot;,&quot;business_trade_license_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_trade_license_link_password&quot;:&quot;12345678&quot;,&quot;business_place_photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_place_photo_link_password&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_continuity_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;business_continuity_proof_link_password&quot;:&quot;12345678&quot;,&quot;other_business_address_proof_number&quot;:&quot;ABC12345&quot;,&quot;other_business_address_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_business_address_proof_link_password&quot;:&quot;12345678&quot;,&quot;no_of_business_authorised_persons&quot;:3,&quot;partnerships&quot;:[&quot;{&quot;partnership_type&quot;:&quot;director&quot;,&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;poi_number&quot;:&quot;794065346728&quot;,&quot;poi_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poi_link_password&quot;:&quot;12345678&quot;,&quot;poa_number&quot;:&quot;L4018348&quot;,&quot;poa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poa_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;}&quot;,&quot;{&quot;partnership_type&quot;:&quot;director&quot;,&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;poi_number&quot;:&quot;794065346728&quot;,&quot;poi_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poi_link_password&quot;:&quot;12345678&quot;,&quot;poa_number&quot;:&quot;L4018348&quot;,&quot;poa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poa_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;}&quot;],&quot;partnership_detail&quot;:&quot;{&quot;partnership_firm_pan&quot;:&quot;BMMPG9018G&quot;,&quot;partnership_pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;partnership_pan_link_password&quot;:&quot;12345678&quot;,&quot;partnership_deed_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;partnership_deed_link_password&quot;:&quot;12345678&quot;,&quot;beneficiary_owner_details_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;beneficiary_owner_details_link_password&quot;:&quot;12345678&quot;}&quot;,&quot;private_entity_detail&quot;:&quot;{&quot;cin_number&quot;:&quot;L21091KA2019OPC141331&quot;,&quot;cin_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;cin_link_password&quot;:&quot;12345678&quot;,&quot;moa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;moa_link_password&quot;:&quot;12345678&quot;,&quot;aoa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aoa_link_password&quot;:&quot;12345678&quot;,&quot;board_resoultion_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;board_resoultion_link_password&quot;:&quot;12345678&quot;,&quot;share_holding_pattern_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;share_holding_pattern_link_password&quot;:&quot;12345678&quot;,&quot;other_company_proof&quot;:&quot;ABC12345&quot;,&quot;other_company_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_company_proof_link_password&quot;:&quot;12345678&quot;}&quot;}</td>  </tr>        <tr>     <td>guarantors</td>     <td>array</td>     <td></td>          <td>Refer table Guarantors for attributes</td>       <td>[{&quot;relationship_with_applicant&quot;:&quot;father&quot;,&quot;first_name&quot;:&quot;Minato&quot;,&quot;middle_name&quot;:&quot;Kumar&quot;,&quot;last_name&quot;:&quot;Namikaze&quot;,&quot;date_of_birth&quot;:&quot;1995-12-05&quot;,&quot;age&quot;:26,&quot;gender&quot;:&quot;M&quot;,&quot;current_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;current_district&quot;:&quot;Chennai&quot;,&quot;current_city&quot;:&quot;Chennai&quot;,&quot;current_city_tier&quot;:&quot;tier_1&quot;,&quot;current_state&quot;:&quot;tamil_nadu&quot;,&quot;current_pincode&quot;:600089,&quot;years_of_stay_in_current_address&quot;:5,&quot;residence_type_current_address&quot;:&quot;rented&quot;,&quot;permanent_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;permanent_district&quot;:&quot;Chennai&quot;,&quot;permanent_city&quot;:&quot;Chennai&quot;,&quot;permanent_city_tier&quot;:&quot;tier_1&quot;,&quot;permanent_state&quot;:&quot;tamil_nadu&quot;,&quot;permanent_pincode&quot;:600089,&quot;years_of_stay_in_permanent_address&quot;:5,&quot;residence_type_permanent_address&quot;:&quot;owned&quot;,&quot;mobile_number&quot;:9876543210,&quot;email&quot;:&quot;minato@gmail.com&quot;,&quot;pan_number&quot;:&quot;BMMPG9018Y&quot;,&quot;pan_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_number_link_password&quot;:&quot;12345678&quot;,&quot;aadhar_number&quot;:&quot;794065346725&quot;,&quot;aadhar_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number_link_password&quot;:&quot;12345678&quot;,&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voting_id_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voting_id_number_link_password&quot;:&quot;12345678&quot;,&quot;driving_license_number&quot;:&quot;TN01123345&quot;,&quot;driving_licence_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_licence_number_link_password&quot;:&quot;12345678&quot;,&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_number_link_password&quot;:&quot;12345678&quot;,&quot;video_image_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_image_link_password&quot;:&quot;12345678&quot;,&quot;video_kyc_detail&quot;:&quot;{&quot;profile_id&quot;:&quot;abc12345&quot;,&quot;account_id&quot;:&quot;abc12345&quot;,&quot;key&quot;:&quot;abc@123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}&quot;,&quot;other_kyc_number&quot;:&quot;other_kyc_number_40&quot;,&quot;other_kyc_number_link&quot;:[&quot;abc12345&quot;,&quot;abc12345&quot;],&quot;other_kyc_number_link_password&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link_password&quot;:&quot;12345678&quot;,&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;,&quot;marital_status&quot;:&quot;unmarried&quot;,&quot;religion&quot;:&quot;Hindu&quot;,&quot;nationality&quot;:&quot;indian&quot;,&quot;bureau_score&quot;:700,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_report_link_password&quot;:&quot;12345678&quot;,&quot;partner_score&quot;:3.0},{&quot;relationship_with_applicant&quot;:&quot;father&quot;,&quot;first_name&quot;:&quot;Minato&quot;,&quot;middle_name&quot;:&quot;Kumar&quot;,&quot;last_name&quot;:&quot;Namikaze&quot;,&quot;date_of_birth&quot;:&quot;1995-12-05&quot;,&quot;age&quot;:26,&quot;gender&quot;:&quot;M&quot;,&quot;current_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;current_district&quot;:&quot;Chennai&quot;,&quot;current_city&quot;:&quot;Chennai&quot;,&quot;current_city_tier&quot;:&quot;tier_1&quot;,&quot;current_state&quot;:&quot;tamil_nadu&quot;,&quot;current_pincode&quot;:600089,&quot;years_of_stay_in_current_address&quot;:5,&quot;residence_type_current_address&quot;:&quot;rented&quot;,&quot;permanent_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;permanent_district&quot;:&quot;Chennai&quot;,&quot;permanent_city&quot;:&quot;Chennai&quot;,&quot;permanent_city_tier&quot;:&quot;tier_1&quot;,&quot;permanent_state&quot;:&quot;tamil_nadu&quot;,&quot;permanent_pincode&quot;:600089,&quot;years_of_stay_in_permanent_address&quot;:5,&quot;residence_type_permanent_address&quot;:&quot;owned&quot;,&quot;mobile_number&quot;:9876543210,&quot;email&quot;:&quot;minato@gmail.com&quot;,&quot;pan_number&quot;:&quot;BMMPG9018Y&quot;,&quot;pan_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_number_link_password&quot;:&quot;12345678&quot;,&quot;aadhar_number&quot;:&quot;794065346725&quot;,&quot;aadhar_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number_link_password&quot;:&quot;12345678&quot;,&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voting_id_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voting_id_number_link_password&quot;:&quot;12345678&quot;,&quot;driving_license_number&quot;:&quot;TN01123345&quot;,&quot;driving_licence_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_licence_number_link_password&quot;:&quot;12345678&quot;,&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_number_link_password&quot;:&quot;12345678&quot;,&quot;video_image_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_image_link_password&quot;:&quot;12345678&quot;,&quot;video_kyc_detail&quot;:&quot;{&quot;profile_id&quot;:&quot;abc12345&quot;,&quot;account_id&quot;:&quot;abc12345&quot;,&quot;key&quot;:&quot;abc@123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}&quot;,&quot;other_kyc_number&quot;:&quot;other_kyc_number_15&quot;,&quot;other_kyc_number_link&quot;:[&quot;abc12345&quot;,&quot;abc12345&quot;],&quot;other_kyc_number_link_password&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link_password&quot;:&quot;12345678&quot;,&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;,&quot;marital_status&quot;:&quot;unmarried&quot;,&quot;religion&quot;:&quot;Hindu&quot;,&quot;nationality&quot;:&quot;indian&quot;,&quot;bureau_score&quot;:700,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_report_link_password&quot;:&quot;12345678&quot;,&quot;partner_score&quot;:3.0}]</td>  </tr>        <tr>     <td>co_applicants</td>     <td>array</td>     <td></td>          <td>Refer table CoApplicants for attributes</td>       <td>[{&quot;relationship_with_applicant&quot;:&quot;father&quot;,&quot;first_name&quot;:&quot;Minato&quot;,&quot;middle_name&quot;:&quot;Kumar&quot;,&quot;last_name&quot;:&quot;Namikaze&quot;,&quot;gender&quot;:&quot;M&quot;,&quot;date_of_birth&quot;:&quot;1995-12-05&quot;,&quot;age&quot;:26,&quot;mobile_number&quot;:9876543210,&quot;email&quot;:&quot;minato@gmail.com&quot;,&quot;current_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;current_city&quot;:&quot;Chennai&quot;,&quot;current_city_tier&quot;:&quot;tier_1&quot;,&quot;current_district&quot;:&quot;Chennai&quot;,&quot;current_state&quot;:&quot;tamil_nadu&quot;,&quot;current_pincode&quot;:600089,&quot;residence_type_current_address&quot;:&quot;rented&quot;,&quot;years_of_stay_in_current_address&quot;:5,&quot;permanent_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;permanent_city&quot;:&quot;Chennai&quot;,&quot;permanent_city_tier&quot;:&quot;tier_1&quot;,&quot;permanent_district&quot;:&quot;Chennai&quot;,&quot;permanent_state&quot;:&quot;tamil_nadu&quot;,&quot;permanent_pincode&quot;:600089,&quot;residence_type_permanent_address&quot;:&quot;owned&quot;,&quot;years_of_stay_in_permanent_address&quot;:5,&quot;marital_status&quot;:&quot;unmarried&quot;,&quot;religion&quot;:&quot;buddhist&quot;,&quot;nationality&quot;:&quot;indian&quot;,&quot;father_name&quot;:&quot;Dan Kato&quot;,&quot;mother_name&quot;:&quot;Tsunade Senju&quot;,&quot;spouse_name&quot;:&quot;Kushina Uzumaki&quot;,&quot;education&quot;:&quot;Hokage&quot;,&quot;annual_income&quot;:120000.0,&quot;income_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;income_proof_link_password&quot;:&quot;12345678&quot;,&quot;bank_statement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_link_password&quot;:&quot;12345678&quot;,&quot;pan_number&quot;:&quot;BMMPG9018Y&quot;,&quot;pan_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_number_link_password&quot;:&quot;12345678&quot;,&quot;aadhar_number&quot;:&quot;794065346725&quot;,&quot;aadhar_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number_link_password&quot;:&quot;12345678&quot;,&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voting_id_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voting_id_number_link_password&quot;:&quot;12345678&quot;,&quot;driving_license_number&quot;:&quot;TN01123345&quot;,&quot;driving_licence_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_licence_number_link_password&quot;:&quot;12345678&quot;,&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_number_link_password&quot;:&quot;12345678&quot;,&quot;video_image_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_image_link_password&quot;:&quot;12345678&quot;,&quot;video_kyc_detail&quot;:&quot;{&quot;profile_id&quot;:&quot;ABC12345&quot;,&quot;account_id&quot;:&quot;ABC12345&quot;,&quot;key&quot;:&quot;abc_123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}&quot;,&quot;other_kyc_number&quot;:&quot;ABC12456&quot;,&quot;other_kyc_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_kyc_number_link_password&quot;:&quot;12345678&quot;,&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link_password&quot;:&quot;12345678&quot;,&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;,&quot;bureau_score&quot;:700,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_report_link_password&quot;:&quot;12345678&quot;,&quot;employment_details_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;employment_details_link_password&quot;:&quot;12345678&quot;,&quot;partner_score&quot;:3.0},{&quot;relationship_with_applicant&quot;:&quot;father&quot;,&quot;first_name&quot;:&quot;Minato&quot;,&quot;middle_name&quot;:&quot;Kumar&quot;,&quot;last_name&quot;:&quot;Namikaze&quot;,&quot;gender&quot;:&quot;M&quot;,&quot;date_of_birth&quot;:&quot;1995-12-05&quot;,&quot;age&quot;:26,&quot;mobile_number&quot;:9876543210,&quot;email&quot;:&quot;minato@gmail.com&quot;,&quot;current_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;current_city&quot;:&quot;Chennai&quot;,&quot;current_city_tier&quot;:&quot;tier_1&quot;,&quot;current_district&quot;:&quot;Chennai&quot;,&quot;current_state&quot;:&quot;tamil_nadu&quot;,&quot;current_pincode&quot;:600089,&quot;residence_type_current_address&quot;:&quot;rented&quot;,&quot;years_of_stay_in_current_address&quot;:5,&quot;permanent_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;permanent_city&quot;:&quot;Chennai&quot;,&quot;permanent_city_tier&quot;:&quot;tier_1&quot;,&quot;permanent_district&quot;:&quot;Chennai&quot;,&quot;permanent_state&quot;:&quot;tamil_nadu&quot;,&quot;permanent_pincode&quot;:600089,&quot;residence_type_permanent_address&quot;:&quot;owned&quot;,&quot;years_of_stay_in_permanent_address&quot;:5,&quot;marital_status&quot;:&quot;unmarried&quot;,&quot;religion&quot;:&quot;buddhist&quot;,&quot;nationality&quot;:&quot;indian&quot;,&quot;father_name&quot;:&quot;Dan Kato&quot;,&quot;mother_name&quot;:&quot;Tsunade Senju&quot;,&quot;spouse_name&quot;:&quot;Kushina Uzumaki&quot;,&quot;education&quot;:&quot;Hokage&quot;,&quot;annual_income&quot;:120000.0,&quot;income_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;income_proof_link_password&quot;:&quot;12345678&quot;,&quot;bank_statement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_link_password&quot;:&quot;12345678&quot;,&quot;pan_number&quot;:&quot;BMMPG9018Y&quot;,&quot;pan_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_number_link_password&quot;:&quot;12345678&quot;,&quot;aadhar_number&quot;:&quot;794065346725&quot;,&quot;aadhar_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number_link_password&quot;:&quot;12345678&quot;,&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voting_id_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voting_id_number_link_password&quot;:&quot;12345678&quot;,&quot;driving_license_number&quot;:&quot;TN01123345&quot;,&quot;driving_licence_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_licence_number_link_password&quot;:&quot;12345678&quot;,&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_number_link_password&quot;:&quot;12345678&quot;,&quot;video_image_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_image_link_password&quot;:&quot;12345678&quot;,&quot;video_kyc_detail&quot;:&quot;{&quot;profile_id&quot;:&quot;ABC12345&quot;,&quot;account_id&quot;:&quot;ABC12345&quot;,&quot;key&quot;:&quot;abc_123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}&quot;,&quot;other_kyc_number&quot;:&quot;ABC12456&quot;,&quot;other_kyc_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_kyc_number_link_password&quot;:&quot;12345678&quot;,&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link_password&quot;:&quot;12345678&quot;,&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;,&quot;bureau_score&quot;:700,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_report_link_password&quot;:&quot;12345678&quot;,&quot;employment_details_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;employment_details_link_password&quot;:&quot;12345678&quot;,&quot;partner_score&quot;:3.0}]</td>  </tr>        <tr>     <td>bank_statement</td>     <td>object</td>     <td></td>    <td>Refer table BankStatement for attributes</td>       <td>{&quot;bank_statement_savings_account_12_months_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_savings_account_12_months_link_password&quot;:&quot;12345678&quot;,&quot;bank_statement_current_account_12_months_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_current_account_12_months_link_password&quot;:&quot;12345678&quot;,&quot;no_of_inward_chq_returns_savings_account&quot;:3,&quot;no_of_outward_chq_returns_savings_account&quot;:4,&quot;no_of_inward_chq_returns_current_account&quot;:5,&quot;no_of_outward_chq_returns_current_account&quot;:6,&quot;bank_account_type_for_assessment&quot;:&quot;savings&quot;,&quot;perfios_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;perfios_link_password&quot;:&quot;12345678&quot;,&quot;perfios_json_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;perfios_json_link_password&quot;:&quot;12345678&quot;,&quot;perfios_json&quot;:[&quot;NA&quot;,&quot;NA&quot;],&quot;finbit_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;finbit_link_password&quot;:&quot;12345678&quot;,&quot;finbit_json_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;finbit_json_link_password&quot;:&quot;12345678&quot;,&quot;finbit_json&quot;:[&quot;NA&quot;,&quot;NA&quot;],&quot;abb&quot;:25000.0,&quot;abd&quot;:10000.0,&quot;credit_summation&quot;:&quot;50000&quot;}</td>  </tr>        <tr>     <td>name_of_bureau</td>     <td>string</td>     <td></td>          <td>Cibil / Experian / Himark</td>       <td>cibil</td>  </tr>        <tr>     <td>bureau_vintage</td>     <td>integer</td>     <td></td>          <td>Vintage in the bureau. Number of years from the first trade line</td>       <td>3</td>  </tr>        <tr>     <td>bureau_score</td>     <td>integer</td>     <td></td>          <td>Bureau Score</td>       <td>650</td>  </tr>        <tr>     <td>bureau_report_json_link</td>     <td>array</td>     <td></td>          <td>Document of the bureau</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_report_json_link_password</td>     <td>string</td>     <td></td>          <td>Document of the bureau - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>bureau_json_link</td>     <td>array</td>     <td></td>          <td>Bureau Json placed in a link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_json_link_password</td>     <td>string</td>     <td></td>          <td>Bureau Json placed in a link - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>bureau_json</td>     <td>array</td>     <td></td>          <td>Bureau Json response</td>       <td>[&quot;NA&quot;, &quot;NA&quot;]</td>  </tr>        <tr>     <td>commercial_bureau_score</td>     <td>integer</td>     <td></td>          <td>CRIF score</td>       <td>330</td>  </tr>        <tr>     <td>commercial_bureau_score_link</td>     <td>array</td>     <td></td>          <td>Commercial Bureau Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>commercial_bureau_score_link_password</td>     <td>string</td>     <td></td>          <td>Commercial Bureau Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>partner_score_on_the_customer_including_bureau_report</td>     <td>number</td>     <td>float</td>          <td>Score Captured by the Partner</td>       <td>800.0</td>  </tr>        <tr>     <td>total_existing_obligations</td>     <td>integer</td>     <td></td>          <td>Total Existing Obligations basis the Bureau Report</td>       <td>25000</td>  </tr>        <tr>     <td>credit_card_limit</td>     <td>integer</td>     <td></td>          <td>Total Credit Card Limit basis the Bureau Report</td>       <td>30000</td>  </tr>        <tr>     <td>no_of_credit_cards</td>     <td>integer</td>     <td></td>          <td>Total Number of Credit Cards per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>total_number_of_unsecured_loans</td>     <td>integer</td>     <td></td>          <td>Total Number of Unsecured Loans per Bureau Report</td>       <td>2</td>  </tr>        <tr>     <td>value_of_total_unsecured_loans</td>     <td>number</td>     <td>float</td>          <td>Total value of unsecured loans</td>       <td>20000.0</td>  </tr>        <tr>     <td>total_number_of_loans</td>     <td>integer</td>     <td></td>          <td>Total Number of Loans per Bureau Report</td>       <td>2</td>  </tr>        <tr>     <td>value_of_total_loans</td>     <td>number</td>     <td>float</td>          <td>Total value of loans</td>       <td>20000.0</td>  </tr>        <tr>     <td>number_of_enquiries_3months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 3 Months per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_enquiries_6months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 6 Months per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_enquiries_12months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 12 Months per Bureau Report</td>       <td>4</td>  </tr>        <tr>     <td>number_of_writeoff_suitfiled_settled_in_the_last_12_months</td>     <td>integer</td>     <td></td>          <td>Number of Writeoff Suitfiled Settled in the Last 12 Months</td>       <td>4</td>  </tr>        <tr>     <td>max_dpd_tradeline_last_12months</td>     <td>integer</td>     <td></td>          <td>Maximum DPD Tradeline in the Last 12 Months</td>       <td>6</td>  </tr>        <tr>     <td>max_overdue_tradeline</td>     <td>integer</td>     <td></td>          <td>Maximum Overdue Tradeline</td>       <td>6</td>  </tr>        <tr>     <td>total_overdue_amount_in_last_12m</td>     <td>number</td>     <td>float</td>          <td>Total Overdue Amount in the Last 12 Months</td>       <td>10000.0</td>  </tr>        <tr>     <td>amount_of_loan_settled_in_last_12m</td>     <td>number</td>     <td>float</td>          <td>Loan Amount Settled in the Last 12 Months</td>       <td>25000.0</td>  </tr>        <tr>     <td>nature_of_loan_settled1</td>     <td>string</td>     <td></td>          <td>The nature of past loan settlement if any (Loan 1) - Settled/ Closed/ Written-off</td>       <td>settled</td>  </tr>        <tr>     <td>nature_of_loan_settled2</td>     <td>string</td>     <td></td>          <td>The nature of past loan settlement if any (Loan 2) - Settled/ Closed/ Written-off</td>       <td>closed</td>  </tr>        <tr>     <td>total_emi_bounces</td>     <td>integer</td>     <td></td>          <td>Total EMI Bounces</td>       <td>3</td>  </tr>        <tr>     <td>bounces_in_last_6m</td>     <td>integer</td>     <td></td>          <td>EMI Bounces in the Last 6 Months</td>       <td>3</td>  </tr>        <tr>     <td>bounces_in_last_12m</td>     <td>integer</td>     <td></td>          <td>EMI Bounces in the Last 12 Months</td>       <td>3</td>  </tr>        <tr>     <td>bureau_validity_date</td>     <td>string</td>     <td>date</td>          <td>Validity of bureau report</td>       <td>1996-01-01</td>  </tr>        <tr>     <td>financial_data</td>     <td>object</td>     <td></td>     <td>Refer table FinancialData for attributes</td>       <td>{&quot;annual_business_turnover&quot;:1000000.0,&quot;annual_gross_profit&quot;:8000000.0,&quot;annual_business_ebitda&quot;:5000000.0,&quot;monthly_net_profit&quot;:14000.0,&quot;annual_net_income&quot;:4000000,&quot;annual_net_profit&quot;:30000000.0,&quot;gst_annual_turnover&quot;:20000,&quot;gst_return_year_1_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;gst_return_year_1_link_password&quot;:&quot;12345678&quot;,&quot;gst_return_year_2_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;gst_return_year_2_link_password&quot;:&quot;12345678&quot;,&quot;gst_return_year_3_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;gst_return_year_3_link_password&quot;:&quot;12345678&quot;,&quot;it_return_year_1_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;it_return_year_1_link_password&quot;:&quot;12345678&quot;,&quot;it_return_year_2_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;it_return_year_2_link_password&quot;:&quot;12345678&quot;,&quot;it_return_year_3_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;it_return_year_3_link_password&quot;:&quot;12345678&quot;,&quot;other_income_assesment_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_income_assesment_proof_link_password&quot;:&quot;12345678&quot;,&quot;cam_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;cam_link_password&quot;:&quot;12345678&quot;,&quot;cfa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;cfa_link_password&quot;:&quot;12345678&quot;}</td>  </tr>        <tr>     <td>abb_emi_ratio</td>     <td>number</td>     <td>float</td>          <td>Average Bank balance to EMI</td>       <td>2.0</td>  </tr>        <tr>     <td>dscr</td>     <td>number</td>     <td>float</td>          <td>Debt Service Coverage Ratio</td>       <td>3.0</td>  </tr>        <tr>     <td>foir</td>     <td>number</td>     <td>float</td>          <td>Fixed Obligations to Income Ratio</td>       <td>4.0</td>  </tr>        <tr>     <td>ltr</td>     <td>number</td>     <td>float</td>          <td>Loan Transfer Ratio</td>       <td>5.0</td>  </tr>        <tr>     <td>insr</td>     <td>number</td>     <td>float</td>          <td>INSR</td>       <td>6.0</td>  </tr>        <tr>     <td>eligibility_as_per_insr</td>     <td>number</td>     <td>float</td>          <td>Eligibility as per INSR</td>       <td>10000.0</td>  </tr>        <tr>     <td>eligibility_as_per_foir</td>     <td>number</td>     <td>float</td>          <td>Eligibility as per FOIR</td>       <td>20000.0</td>  </tr>        <tr>     <td>eligibility_as_per_ltv</td>     <td>number</td>     <td>float</td>          <td>Eligibility as per LTV</td>       <td>30000.0</td>  </tr>        <tr>     <td>eligibility_loan_amount</td>     <td>number</td>     <td>float</td>          <td>Eligibility Loan amount</td>       <td>40000.0</td>  </tr>        <tr>     <td>fcf</td>     <td>integer</td>     <td></td>          <td>Free Cash Flows</td>       <td>24000</td>  </tr>        <tr>     <td>emi_obligations</td>     <td>integer</td>     <td></td>          <td>Existing EMI obligations</td>       <td>20000</td>  </tr>        <tr>     <td>viability_ratio</td>     <td>number</td>     <td>float</td>          <td>Net Assets/ Debt</td>       <td>2.0</td>  </tr>        <tr>     <td>product_id</td>     <td>string</td>     <td></td>          <td>Product ID created in CA</td>       <td>CONSUMER_001</td>  </tr>        <tr>     <td>client_loan_id</td>     <td>string</td>     <td></td>          <td>Loan ID as per Partner&#39;s LMS</td>       <td>LOAN00001</td>  </tr>        <tr>     <td>application_id</td>     <td>string</td>     <td></td>          <td>Application ID as per Partner&#39;s CRM/LOS</td>       <td>LOAN00001</td>  </tr>        <tr>     <td>loan_cycle</td>     <td>integer</td>     <td></td>          <td>Denotes the Cycle number of the loan given to the borrower</td>       <td>0</td>  </tr>        <tr>     <td>partner_branch_code</td>     <td>string</td>     <td></td>          <td>Branch Code as per Partner&#39;s LOS</td>       <td>ABC123</td>  </tr>        <tr>     <td>partner_branch_name</td>     <td>string</td>     <td></td>          <td>Branch Name as per Partner&#39;s LOS</td>       <td>ABC123</td>  </tr>        <tr>     <td>product_type</td>     <td>string</td>     <td></td>          <td></td>       <td>Consumer</td>  </tr>        <tr>     <td>partner_product_code</td>     <td>string</td>     <td></td>          <td>Product code as per partners LOS/LMS</td>       <td>CONSUMER_001</td>  </tr>        <tr>     <td>partner_scheme_code</td>     <td>string</td>     <td></td>          <td></td>       <td>partner_scheme_code_54</td>  </tr>        <tr>     <td>category</td>     <td>string</td>     <td></td>          <td>secured / unsecured</td>       <td>secured</td>  </tr>        <tr>     <td>sub_category</td>     <td>string</td>     <td></td>          <td>bt / top_up / fresh</td>       <td>fresh</td>  </tr>        <tr>     <td>purpose</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>Personal Loan</td>  </tr>        <tr>     <td>disbursement_type</td>     <td>string</td>     <td></td>          <td>Tranche / Single Disbursement</td>       <td>single</td>  </tr>        <tr>     <td>number_of_tranches</td>     <td>integer</td>     <td></td>          <td>Total number of Tranches</td>       <td>2</td>  </tr>        <tr>     <td>end_borrower_amount</td>     <td>number</td>     <td>float</td>          <td>End borrower amount in case of multiple disbursals</td>       <td>40000.0</td>  </tr>        <tr>     <td>existing_lender_amount</td>     <td>number</td>     <td>float</td>          <td>Existing Lender Amount in case of multiple disbursals</td>       <td>10000.0</td>  </tr>        <tr>     <td>principal_amount</td>     <td>number</td>     <td>float</td>          <td>Total loan amount in Rs (Overall amount to the borrower)</td>       <td>100000.0</td>  </tr>        <tr>     <td>interest_rate</td>     <td>number</td>     <td>float</td>          <td>Reducing balance interest rate of the customer in %. This is the interest rate to be mentioned in the sanction letter as well</td>       <td>20.2</td>  </tr>        <tr>     <td>interest_type</td>     <td>string</td>     <td></td>          <td>Interest Type of the Loan</td>       <td>floating</td>  </tr>        <tr>     <td>tenure</td>     <td>integer</td>     <td></td>          <td>Tenure of the loan</td>       <td>12</td>  </tr>        <tr>     <td>tenure_frequency</td>     <td>string</td>     <td></td>          <td>Whether the tenure is monthly/yearly/weekly</td>       <td>monthly</td>  </tr>        <tr>     <td>repayment_frequency</td>     <td>string</td>     <td></td>          <td>Daily/Weekly/Once in 2 weeks/Monthly/Quarterly/Bullet</td>       <td>monthly</td>  </tr>        <tr>     <td>number_of_repayments</td>     <td>integer</td>     <td></td>          <td>Number of repayments as per the repayment schedule</td>       <td>12</td>  </tr>        <tr>     <td>first_repayment_date</td>     <td>string</td>     <td>date</td>          <td>First repayment date as per the repayment schedule (YYYY-MM-DD)</td>       <td>2021-08-30</td>  </tr>        <tr>     <td>repayment_mode</td>     <td>string</td>     <td></td>          <td>Cash / NACH</td>       <td>nach</td>  </tr>        <tr>     <td>advance_emi</td>     <td>number</td>     <td>float</td>          <td>Advance EMI Amount (If collected any)</td>       <td>1000.0</td>  </tr>        <tr>     <td>umrn</td>     <td>string</td>     <td></td>          <td>To update if UMRN generated at this stage, else in PDD stage</td>       <td>umrn_12345</td>  </tr>        <tr>     <td>interest_start_date</td>     <td>string</td>     <td>date</td>          <td>Pre Emi interest due date</td>       <td>1995-10-10</td>  </tr>        <tr>     <td>differential_interest</td>     <td>number</td>     <td>float</td>          <td>Broken Period Interest Amount (in Rupees)</td>       <td>100.0</td>  </tr>        <tr>     <td>processing_fee</td>     <td>number</td>     <td>float</td>          <td>Processing Fee (Inclusive of GST)</td>       <td>100.0</td>  </tr>        <tr>     <td>stamp_duty</td>     <td>number</td>     <td>float</td>          <td>Stamp duty amount</td>       <td>100.0</td>  </tr>        <tr>     <td>insurance_charges</td>     <td>number</td>     <td>float</td>          <td>Insurance premium inclusive of GST</td>       <td>100.0</td>  </tr>        <tr>     <td>documentation_charges</td>     <td>number</td>     <td>float</td>          <td>Total documentation charges inclusive of GST</td>       <td>100.0</td>  </tr>        <tr>     <td>other_charges</td>     <td>number</td>     <td>float</td>          <td>Any Other Charges Inclusive of GST</td>       <td>100.0</td>  </tr>        <tr>     <td>loan_plr_type</td>     <td>string</td>     <td></td>          <td></td>       <td>loan_plr_type_61</td>  </tr>        <tr>     <td>loan_plr_rate</td>     <td>number</td>     <td>float</td>          <td>Prime Lending Rate of the loan</td>       <td>20.2</td>  </tr>        <tr>     <td>spread_id</td>     <td>string</td>     <td></td>          <td></td>       <td>spread_id_18</td>  </tr>        <tr>     <td>loan_emi</td>     <td>number</td>     <td>float</td>          <td>EMI of the loan</td>       <td>1000.0</td>  </tr>        <tr>     <td>rcu_status</td>     <td>string</td>     <td></td>          <td>Document Verification Status (Y/N)</td>       <td>t</td>  </tr>        <tr>     <td>surrogate</td>     <td>string</td>     <td></td>          <td>Surrogate</td>       <td>surrogate_89</td>  </tr>        <tr>     <td>sub_class</td>     <td>string</td>     <td></td>          <td>Sub Class</td>       <td>sub_class_80</td>  </tr>        <tr>     <td>weaker_section</td>     <td>string</td>     <td></td>          <td>Whether the borrower belongs to the weaker section as defined under RBI norms</td>       <td>small marginal farmers</td>  </tr>        <tr>     <td>disbursement_accounts</td>     <td>array</td>     <td></td>          <td>Refer table DisbursementAccounts for attributes</td>       <td>[{&quot;account_type&quot;:&quot;dealer&quot;,&quot;bank_name&quot;:&quot;HDFC&quot;,&quot;bank_account_type&quot;:&quot;savings&quot;,&quot;account_name&quot;:&quot;Neeraj Chopra&quot;,&quot;date_of_bank_account_opening&quot;:&quot;1995-01-01&quot;,&quot;bank_branch_name&quot;:&quot;Rajaji Salai&quot;,&quot;ifsc_code&quot;:&quot;HDFC000123&quot;,&quot;entity_type&quot;:&quot;dealer&quot;,&quot;account_no&quot;:&quot;1234567890&quot;,&quot;amount&quot;:10000.0},{&quot;account_type&quot;:&quot;dealer&quot;,&quot;bank_name&quot;:&quot;HDFC&quot;,&quot;bank_account_type&quot;:&quot;savings&quot;,&quot;account_name&quot;:&quot;Neeraj Chopra&quot;,&quot;date_of_bank_account_opening&quot;:&quot;1995-01-01&quot;,&quot;bank_branch_name&quot;:&quot;Rajaji Salai&quot;,&quot;ifsc_code&quot;:&quot;HDFC000123&quot;,&quot;entity_type&quot;:&quot;dealer&quot;,&quot;account_no&quot;:&quot;1234567890&quot;,&quot;amount&quot;:10000.0}]</td>  </tr>        <tr>     <td>assets</td>     <td>array</td>     <td></td>          <td>Refer table Assets for attributes</td>       <td>[{&quot;asset_category&quot;:&quot;residential&quot;,&quot;asset_owned_by&quot;:&quot;Polygon&quot;,&quot;relationship_to_the_business&quot;:&quot;Promoter&quot;,&quot;asset_value_self_declared&quot;:&quot;100000&quot;,&quot;asset_market_value&quot;:&quot;80000&quot;,&quot;ltv_asset_market_value&quot;:&quot;50000&quot;,&quot;area_type&quot;:&quot;Urban&quot;,&quot;ltv_asset_value_self_declared&quot;:100000.0,&quot;age_of_the_collateral&quot;:4,&quot;mortgage_in_favour_of&quot;:&quot;PNB Housing&quot;,&quot;machinery_type&quot;:&quot;Heavy machinery&quot;,&quot;hypothecation_value&quot;:2000.0,&quot;hypothecation_percentage&quot;:35.0,&quot;new_machinery_value&quot;:30000.0,&quot;old_machinery_value&quot;:10000.0,&quot;new_machinery_ltv&quot;:20000.0,&quot;old_machinery_ltv&quot;:10000.0,&quot;total_number_of_machines&quot;:4,&quot;total_value_of_machines&quot;:500000.0,&quot;manufacturer_name&quot;:&quot;BMW&quot;,&quot;machinery_hypothecated_to&quot;:&quot;Neeraj&quot;,&quot;property_address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;property_city&quot;:&quot;Chennai&quot;,&quot;property_district&quot;:&quot;Chennai&quot;,&quot;property_state&quot;:&quot;tamil_nadu&quot;,&quot;property_pincode&quot;:600025},{&quot;asset_category&quot;:&quot;residential&quot;,&quot;asset_owned_by&quot;:&quot;Polygon&quot;,&quot;relationship_to_the_business&quot;:&quot;Promoter&quot;,&quot;asset_value_self_declared&quot;:&quot;100000&quot;,&quot;asset_market_value&quot;:&quot;80000&quot;,&quot;ltv_asset_market_value&quot;:&quot;50000&quot;,&quot;area_type&quot;:&quot;Urban&quot;,&quot;ltv_asset_value_self_declared&quot;:100000.0,&quot;age_of_the_collateral&quot;:4,&quot;mortgage_in_favour_of&quot;:&quot;PNB Housing&quot;,&quot;machinery_type&quot;:&quot;Heavy machinery&quot;,&quot;hypothecation_value&quot;:2000.0,&quot;hypothecation_percentage&quot;:35.0,&quot;new_machinery_value&quot;:30000.0,&quot;old_machinery_value&quot;:10000.0,&quot;new_machinery_ltv&quot;:20000.0,&quot;old_machinery_ltv&quot;:10000.0,&quot;total_number_of_machines&quot;:4,&quot;total_value_of_machines&quot;:500000.0,&quot;manufacturer_name&quot;:&quot;BMW&quot;,&quot;machinery_hypothecated_to&quot;:&quot;Neeraj&quot;,&quot;property_address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;property_city&quot;:&quot;Chennai&quot;,&quot;property_district&quot;:&quot;Chennai&quot;,&quot;property_state&quot;:&quot;tamil_nadu&quot;,&quot;property_pincode&quot;:600025}]</td>  </tr>        <tr>     <td>references</td>     <td>array</td>     <td></td>          <td>Refer table References for attributes</td>       <td>[{&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;pincode&quot;:&quot;600001&quot;,&quot;phone&quot;:&quot;9876543210&quot;},{&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;pincode&quot;:&quot;600001&quot;,&quot;phone&quot;:&quot;9876543210&quot;}]</td>  </tr>        <tr>     <td>insurance_details</td>     <td>array</td>     <td></td>          <td>Refer table InsuranceDetails for attributes</td>       <td>[{&quot;insurance_type&quot;:&quot;credit&quot;,&quot;insurer_name&quot;:&quot;Tata AIG&quot;,&quot;nominee_details&quot;:&quot;Neeraj&quot;,&quot;nominee_date_of_birth&quot;:&quot;1990-01-01&quot;,&quot;relationship&quot;:&quot;friend&quot;,&quot;premium&quot;:100000.0,&quot;insurance_amount&quot;:300000.0,&quot;policy_number&quot;:0},{&quot;insurance_type&quot;:&quot;credit&quot;,&quot;insurer_name&quot;:&quot;Tata AIG&quot;,&quot;nominee_details&quot;:&quot;Neeraj&quot;,&quot;nominee_date_of_birth&quot;:&quot;1990-01-01&quot;,&quot;relationship&quot;:&quot;friend&quot;,&quot;premium&quot;:100000.0,&quot;insurance_amount&quot;:300000.0,&quot;policy_number&quot;:0}]</td>  </tr>        <tr>     <td>psl_flag</td>     <td>string</td>     <td></td>          <td>Does this loan belong to Priority Sector Lending?</td>       <td>t</td>  </tr>        <tr>     <td>psl_description</td>     <td>string</td>     <td></td>          <td>Description on Priority Sector Lending</td>       <td>psl_description_38</td>  </tr>        <tr>     <td>psl_code</td>     <td>string</td>     <td></td>          <td>Priority Sector Lending code</td>       <td>psl_code_78</td>  </tr>        <tr>     <td>psl_proof_link</td>     <td>array</td>     <td></td>          <td>Any documents as proof for PSL</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>psl_proof_link_password</td>     <td>string</td>     <td></td>          <td>Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>tranches</td>     <td>array</td>     <td></td>          <td>Refer table Tranches for attributes</td>       <td>[{&quot;tranche_number&quot;:1,&quot;principal_amount&quot;:10000,&quot;differential_interest&quot;:100,&quot;processing_fee&quot;:50,&quot;stamp_duty&quot;:100,&quot;insurance_charges&quot;:100,&quot;documentation_charges&quot;:100,&quot;other_charges&quot;:100,&quot;closing_loan_principal&quot;:5000},{&quot;tranche_number&quot;:1,&quot;principal_amount&quot;:10000,&quot;differential_interest&quot;:100,&quot;processing_fee&quot;:50,&quot;stamp_duty&quot;:100,&quot;insurance_charges&quot;:100,&quot;documentation_charges&quot;:100,&quot;other_charges&quot;:100,&quot;closing_loan_principal&quot;:5000}]</td>  </tr>        <tr>     <td>linked_loan_infos</td>     <td>array</td>     <td></td>          <td>Refer table LinkedLoanInfos for attributes</td>       <td>[{&quot;linked_loan_id&quot;:&quot;CA_123&quot;,&quot;foreclosure&quot;:&quot;t&quot;,&quot;principal&quot;:1000.0,&quot;interest&quot;:100.0,&quot;other_charges&quot;:50.0,&quot;overdue_charges&quot;:100.0,&quot;penalty_charges&quot;:100.0,&quot;fee_charges&quot;:100.0,&quot;bounce_charges&quot;:100.0,&quot;amount&quot;:100.0},{&quot;linked_loan_id&quot;:&quot;CA_123&quot;,&quot;foreclosure&quot;:&quot;t&quot;,&quot;principal&quot;:1000.0,&quot;interest&quot;:100.0,&quot;other_charges&quot;:50.0,&quot;overdue_charges&quot;:100.0,&quot;penalty_charges&quot;:100.0,&quot;fee_charges&quot;:100.0,&quot;bounce_charges&quot;:100.0,&quot;amount&quot;:100.0}]</td>  </tr>        <tr>     <td>sourcing_detail</td>     <td>object</td>     <td></td>      <td>Refer table SourcingDetail for attributes</td>       <td>{&quot;source_code&quot;:&quot;PNB&quot;,&quot;referrer_code&quot;:&quot;referrer_code_80&quot;,&quot;referrer_group&quot;:&quot;referrer_group_14&quot;,&quot;referrer_name&quot;:&quot;Albus&quot;,&quot;channel_code&quot;:&quot;DSA sourcing&quot;,&quot;dst_code&quot;:&quot;dst_code_87&quot;,&quot;dsa&quot;:&quot;John Pvt Ltd.&quot;,&quot;dse&quot;:&quot;John&quot;,&quot;relationship_manager&quot;:&quot;Harry&quot;}</td>  </tr>        <tr>     <td>deviation_details</td>     <td>array</td>     <td></td>          <td>Refer table DeviationDetails for attributes</td>       <td>[{&quot;summary&quot;:&quot;This deviation refers to the nature of the segment itself where the corporate on onboarding high debt can continue to keep capex funding at optimum levels, thus TD/NCA is typically high in these funding cases&quot;,&quot;desc&quot;:&quot;High TD/NCA&quot;,&quot;mitigant&quot;:&quot;Even though interest liabilities are higher on account of all current facilities, the company has shown substantial asset growth and cash flow has remained robust over the past 3 FY&quot;,&quot;level&quot;:&quot;high&quot;},{&quot;summary&quot;:&quot;This deviation refers to the nature of the segment itself where the corporate on onboarding high debt can continue to keep capex funding at optimum levels, thus TD/NCA is typically high in these funding cases&quot;,&quot;desc&quot;:&quot;High TD/NCA&quot;,&quot;mitigant&quot;:&quot;Even though interest liabilities are higher on account of all current facilities, the company has shown substantial asset growth and cash flow has remained robust over the past 3 FY&quot;,&quot;level&quot;:&quot;high&quot;}]</td>  </tr>    </tbody>       </table>   <h4>VideoKycDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>profile_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Profile ID of the case as per the video KYC vendor</td>       <td>AB12345</td>  </tr>        <tr>     <td>account_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Account ID of the case as per the video KYC vendor</td>       <td>AB12345</td>  </tr>        <tr>     <td>key</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Key as per the video KYC vendor</td>       <td>abc@123</td>  </tr>        <tr>     <td>auditor</td>     <td>string</td>     <td></td>          <td>Name of the Video KYC Auditor</td>       <td>Neeraj Chopra</td>  </tr>        <tr>     <td>officer</td>     <td>string</td>     <td></td>          <td>Name of the Video KYC Officer</td>       <td>Neeraj Chopra</td>  </tr>    </tbody>       </table>   <h4>Partnerships</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>partnership_type</td>     <td>string</td>     <td></td>          <td>director / signatory / person / partner</td>       <td>director</td>  </tr>        <tr>     <td>name</td>     <td>string</td>     <td></td>          <td>Name of 1st authorized person</td>       <td>Neeraj Chopra</td>  </tr>        <tr>     <td>poi_number</td>     <td>string</td>     <td></td>          <td>KYC number of the authorised person/director</td>       <td>794065346728</td>  </tr>        <tr>     <td>poi_link</td>     <td>array</td>     <td></td>          <td>Proof of Identity for 1st authorized person</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>poi_link_password</td>     <td>string</td>     <td></td>          <td>Proof of Identity for 1st authorized person</td>       <td>12345678</td>  </tr>        <tr>     <td>poa_number</td>     <td>string</td>     <td></td>          <td>KYC number of the authorised person/director</td>       <td>L4018348</td>  </tr>        <tr>     <td>poa_link</td>     <td>array</td>     <td></td>          <td>Proof of address for 1st authorized person/director</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>poa_link_password</td>     <td>string</td>     <td></td>          <td>Proof of address for 1st authorized person/director</td>       <td>12345678</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo of the 1st authorised person/director</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link_password</td>     <td>string</td>     <td></td>          <td>Photo of the 1st authorised person/director</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>PartnershipDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>partnership_firm_pan</td>     <td>string</td>     <td></td>          <td>PAN number of partnership</td>       <td>BMMPG9018G</td>  </tr>        <tr>     <td>partnership_pan_link</td>     <td>array</td>     <td></td>          <td>PAN image of partnership</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>partnership_pan_link_password</td>     <td>string</td>     <td></td>          <td>PAN image password of partnership</td>       <td>12345678</td>  </tr>        <tr>     <td>partnership_deed_link</td>     <td>array</td>     <td></td>          <td>Partnership deed image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>partnership_deed_link_password</td>     <td>string</td>     <td></td>          <td>Partnership deed image password</td>       <td>12345678</td>  </tr>        <tr>     <td>beneficiary_owner_details_link</td>     <td>array</td>     <td></td>          <td>Shareholding pattern of the firm</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>beneficiary_owner_details_link_password</td>     <td>string</td>     <td></td>          <td>Shareholding pattern of the firm - password</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>PrivateEntityDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>cin_number</td>     <td>string</td>     <td></td>          <td>CIN number in case of a company</td>       <td>L21091KA2019OPC141331</td>  </tr>        <tr>     <td>cin_link</td>     <td>array</td>     <td></td>          <td>CIN image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>cin_link_password</td>     <td>string</td>     <td></td>          <td>CIN image password</td>       <td>12345678</td>  </tr>        <tr>     <td>moa_link</td>     <td>array</td>     <td></td>          <td>MOA image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>moa_link_password</td>     <td>string</td>     <td></td>          <td>MOA image password</td>       <td>12345678</td>  </tr>        <tr>     <td>aoa_link</td>     <td>array</td>     <td></td>          <td>AOA image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aoa_link_password</td>     <td>string</td>     <td></td>          <td>AOA image password</td>       <td>12345678</td>  </tr>        <tr>     <td>board_resoultion_link</td>     <td>array</td>     <td></td>          <td>Board resolution image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>board_resoultion_link_password</td>     <td>string</td>     <td></td>          <td>Board resolution image password</td>       <td>12345678</td>  </tr>        <tr>     <td>share_holding_pattern_link</td>     <td>array</td>     <td></td>          <td>Shareholding pattern image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>share_holding_pattern_link_password</td>     <td>string</td>     <td></td>          <td>Shareholding pattern image password</td>       <td>12345678</td>  </tr>        <tr>     <td>other_company_proof</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>ABC12345</td>  </tr>        <tr>     <td>other_company_proof_link</td>     <td>array</td>     <td></td>          <td>Image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_company_proof_link_password</td>     <td>string</td>     <td></td>          <td>Image password</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>Business</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>name_of_business</td>     <td>string</td>     <td></td>          <td>Business name</td>       <td>Credavenue</td>  </tr>        <tr>     <td>nature_of_business</td>     <td>string</td>     <td></td>          <td>The sector this business belongs to</td>       <td>Electronics</td>  </tr>        <tr>     <td>type_of_constitution</td>     <td>string</td>     <td></td>          <td>Partnership/Propertorship/Private Ltd</td>       <td>partnership</td>  </tr>        <tr>     <td>type_of_ownership</td>     <td>string</td>     <td></td>          <td>Type of Ownership</td>       <td>type_of_ownership_15</td>  </tr>        <tr>     <td>registration_date</td>     <td>string</td>     <td>date</td>          <td>Registration date of the business</td>       <td>1995-01-01</td>  </tr>        <tr>     <td>incorporation_date</td>     <td>string</td>     <td>date</td>          <td>Incorporation date of the business</td>       <td>1995-01-01</td>  </tr>        <tr>     <td>industry_type</td>     <td>string</td>     <td></td>          <td>trading/ manufacturing/ services</td>       <td>trading</td>  </tr>        <tr>     <td>sector_type</td>     <td>string</td>     <td></td>          <td>Name of the sector</td>       <td>Financial services</td>  </tr>        <tr>     <td>sub_sector_type</td>     <td>string</td>     <td></td>          <td>Name of the Sub sector</td>       <td>Banking</td>  </tr>        <tr>     <td>business_vintage</td>     <td>integer</td>     <td></td>          <td>Number of years of business existence</td>       <td>4</td>  </tr>        <tr>     <td>business_registered_office_address</td>     <td>string</td>     <td></td>          <td>Address of the business location</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>business_registered_office_district</td>     <td>string</td>     <td></td>          <td>Address of the business location</td>       <td>Chennai</td>  </tr>        <tr>     <td>business_registered_office_city</td>     <td>string</td>     <td></td>          <td>City of business address</td>       <td>Chennai</td>  </tr>        <tr>     <td>business_registered_office_state</td>     <td>string</td>     <td></td>          <td>State of business address</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>business_registered_office_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of business address</td>       <td>600025</td>  </tr>        <tr>     <td>business_mailing_office_address</td>     <td>string</td>     <td></td>          <td>Address of business location</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>business_mailing_office_city</td>     <td>string</td>     <td></td>          <td>City of business address</td>       <td>Chennai</td>  </tr>        <tr>     <td>business_mailing_office_state</td>     <td>string</td>     <td></td>          <td>State of business location</td>       <td>Chennai</td>  </tr>        <tr>     <td>business_mailing_office_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of business location</td>       <td>600025</td>  </tr>        <tr>     <td>business_registered_office_link</td>     <td>array</td>     <td></td>          <td>Registered office document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_registered_office_link_password</td>     <td>string</td>     <td></td>          <td>Registered office document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_mailing_office_link</td>     <td>array</td>     <td></td>          <td>Mailing office document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_mailing_office_link_password</td>     <td>string</td>     <td></td>          <td>Mailing office document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_phone_number</td>     <td>array</td>     <td></td>          <td>Phone number of business address</td>       <td>[9876543210, 9876543210]</td>  </tr>        <tr>     <td>business_email_id</td>     <td>array</td>     <td></td>          <td>Email id of the business</td>       <td>[&quot;holmes@credavenue.com&quot;, &quot;holmes@credavenue.com&quot;]</td>  </tr>        <tr>     <td>business_partner_score</td>     <td>number</td>     <td>float</td>          <td>Partner score for the business</td>       <td>3.0</td>  </tr>        <tr>     <td>business_pan_number</td>     <td>string</td>     <td></td>          <td>PAN number of business</td>       <td>BMMPG9018G</td>  </tr>        <tr>     <td>business_pan_link</td>     <td>array</td>     <td></td>          <td>PAN image of business</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_pan_link_password</td>     <td>string</td>     <td></td>          <td>PAN image password of business</td>       <td>12345678</td>  </tr>        <tr>     <td>business_rc_number</td>     <td>string</td>     <td></td>          <td>Registration number of the business</td>       <td>U72200MH2009PLC123456</td>  </tr>        <tr>     <td>business_rc_link</td>     <td>array</td>     <td></td>          <td>Image of the RC</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_rc_link_password</td>     <td>string</td>     <td></td>          <td>Image password of the RC</td>       <td>12345678</td>  </tr>        <tr>     <td>business_gst_number</td>     <td>string</td>     <td></td>          <td>Business GST number</td>       <td>29ABCDE1234F2Z5</td>  </tr>        <tr>     <td>business_gst_copy_link</td>     <td>array</td>     <td></td>          <td>Business GST image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_gst_copy_link_password</td>     <td>string</td>     <td></td>          <td>Business GST image password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_udyog_aadhar_number</td>     <td>string</td>     <td></td>          <td>Business Udyog Aadhar Number</td>       <td>794065346725</td>  </tr>        <tr>     <td>business_udyog_aadhar_link</td>     <td>array</td>     <td></td>          <td>Business Udyog Aadhar Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_udyog_aadhar_link_password</td>     <td>string</td>     <td></td>          <td>Business Udyog Aadhar Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_ssi_number</td>     <td>string</td>     <td></td>          <td>Small scall industries registration number</td>       <td>7589297314</td>  </tr>        <tr>     <td>business_ssi_link</td>     <td>array</td>     <td></td>          <td>Small scall industries registration document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_ssi_link_password</td>     <td>string</td>     <td></td>          <td>Small scall industries registration document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_shops_est_number</td>     <td>string</td>     <td></td>          <td>Shop establishment number</td>       <td>2017086025</td>  </tr>        <tr>     <td>business_shops_est_link</td>     <td>array</td>     <td></td>          <td>Shop establishment document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_shops_est_link_password</td>     <td>string</td>     <td></td>          <td>Shop establishment document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_factory_regn_number</td>     <td>string</td>     <td></td>          <td>Factory riegistration number</td>       <td>TVEIQ0615232</td>  </tr>        <tr>     <td>business_factory_regn_link</td>     <td>array</td>     <td></td>          <td>Factory riegistration document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_factory_regn_link_password</td>     <td>string</td>     <td></td>          <td>Factory riegistration document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_trade_license_number</td>     <td>string</td>     <td></td>          <td>Trade license number</td>       <td>EA131102014709112</td>  </tr>        <tr>     <td>business_trade_license_link</td>     <td>array</td>     <td></td>          <td>Trade license document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_trade_license_link_password</td>     <td>string</td>     <td></td>          <td>Trade license document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_place_photo_link</td>     <td>array</td>     <td></td>          <td>Business place photo image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_place_photo_link_password</td>     <td>string</td>     <td></td>          <td>Business place photo image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_continuity_proof_link</td>     <td>array</td>     <td></td>          <td>Business continuity proof document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>business_continuity_proof_link_password</td>     <td>string</td>     <td></td>          <td>Business continuity proof document password</td>       <td>12345678</td>  </tr>        <tr>     <td>other_business_address_proof_number</td>     <td>string</td>     <td></td>          <td>any other adddress proof number</td>       <td>ABC12345</td>  </tr>        <tr>     <td>other_business_address_proof_link</td>     <td>array</td>     <td></td>          <td>any other adddress proof image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_business_address_proof_link_password</td>     <td>string</td>     <td></td>          <td>any other adddress proof image password</td>       <td>12345678</td>  </tr>        <tr>     <td>no_of_business_authorised_persons</td>     <td>integer</td>     <td></td>          <td>Number of authorized person for business</td>       <td>3</td>  </tr>        <tr>     <td>partnerships</td>     <td>array</td>     <td></td>          <td>Refer table Partnerships for attributes</td>       <td>[{&quot;partnership_type&quot;:&quot;director&quot;,&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;poi_number&quot;:&quot;794065346728&quot;,&quot;poi_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poi_link_password&quot;:&quot;12345678&quot;,&quot;poa_number&quot;:&quot;L4018348&quot;,&quot;poa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poa_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;},{&quot;partnership_type&quot;:&quot;director&quot;,&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;poi_number&quot;:&quot;794065346728&quot;,&quot;poi_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poi_link_password&quot;:&quot;12345678&quot;,&quot;poa_number&quot;:&quot;L4018348&quot;,&quot;poa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;poa_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;}]</td>  </tr>        <tr>     <td>partnership_detail</td>     <td>object</td>      <td></td>     <td>Refer table PartnershipDetail for attributes</td>       <td>{&quot;partnership_firm_pan&quot;:&quot;BMMPG9018G&quot;,&quot;partnership_pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;partnership_pan_link_password&quot;:&quot;12345678&quot;,&quot;partnership_deed_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;partnership_deed_link_password&quot;:&quot;12345678&quot;,&quot;beneficiary_owner_details_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;beneficiary_owner_details_link_password&quot;:&quot;12345678&quot;}</td>  </tr>        <tr>     <td>private_entity_detail</td>     <td>object</td>     <td></td>     <td>Refer table PrivateEntityDetail for attributes</td>       <td>{&quot;cin_number&quot;:&quot;L21091KA2019OPC141331&quot;,&quot;cin_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;cin_link_password&quot;:&quot;12345678&quot;,&quot;moa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;moa_link_password&quot;:&quot;12345678&quot;,&quot;aoa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aoa_link_password&quot;:&quot;12345678&quot;,&quot;board_resoultion_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;board_resoultion_link_password&quot;:&quot;12345678&quot;,&quot;share_holding_pattern_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;share_holding_pattern_link_password&quot;:&quot;12345678&quot;,&quot;other_company_proof&quot;:&quot;ABC12345&quot;,&quot;other_company_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_company_proof_link_password&quot;:&quot;12345678&quot;}</td>  </tr>    </tbody>       </table>   <h4>Guarantors</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>relationship_with_applicant</td>     <td>string</td>     <td></td>          <td>Father/Mother/Brother/Son/Daughter/Friend/Other relative</td>       <td>father</td>  </tr>        <tr>     <td>first_name</td>     <td>string</td>     <td></td>          <td>First Name of the Guarantor</td>       <td>Minato</td>  </tr>        <tr>     <td>middle_name</td>     <td>string</td>     <td></td>          <td>Middle Name of the Guarantor</td>       <td>Kumar</td>  </tr>        <tr>     <td>last_name</td>     <td>string</td>     <td></td>          <td>Last Name of the Guarantor</td>       <td>Namikaze</td>  </tr>        <tr>     <td>date_of_birth</td>     <td>string</td>     <td>date</td>          <td>Date of Birth (YYYY-MM-DD)</td>       <td>1995-12-05</td>  </tr>        <tr>     <td>age</td>     <td>integer</td>     <td></td>          <td>Age in years</td>       <td>26</td>  </tr>        <tr>     <td>gender</td>     <td>string</td>     <td></td>          <td>M / F / O</td>       <td>M</td>  </tr>        <tr>     <td>current_address</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>2, Mount Road, Teynampet</td>  </tr>        <tr>     <td>current_district</td>     <td>string</td>     <td></td>          <td>District in which Guarantor is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_city</td>     <td>string</td>     <td></td>          <td>City in which Guarantor is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_city_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for the current city</td>       <td>tier_1</td>  </tr>        <tr>     <td>current_state</td>     <td>string</td>     <td></td>          <td>State in which Guarantor is currently residing</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>current_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>years_of_stay_in_current_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the current address</td>       <td>5</td>  </tr>        <tr>     <td>residence_type_current_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>rented</td>  </tr>        <tr>     <td>permanent_address</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>2, Mount Road, Teynampet</td>  </tr>        <tr>     <td>permanent_district</td>     <td>string</td>     <td></td>          <td>District in which Guarantor is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_city</td>     <td>string</td>     <td></td>          <td>City in which Guarantor is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_city_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for the permanent city</td>       <td>tier_1</td>  </tr>        <tr>     <td>permanent_state</td>     <td>string</td>     <td></td>          <td>State in which Guarantor is currently residing</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>permanent_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>years_of_stay_in_permanent_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the permanent address</td>       <td>5</td>  </tr>        <tr>     <td>residence_type_permanent_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>owned</td>  </tr>        <tr>     <td>mobile_number</td>     <td>integer</td>     <td></td>          <td>Mobile Number of the Guarantor (10 digits)</td>       <td>9876543210</td>  </tr>        <tr>     <td>email</td>     <td>string</td>     <td></td>          <td>Personal Email ID of the Guarantor</td>       <td>minato@gmail.com</td>  </tr>        <tr>     <td>pan_number</td>     <td>string</td>     <td></td>          <td>PAN Number of the Guarantor (10 digit Alphanumeric)</td>       <td>BMMPG9018Y</td>  </tr>        <tr>     <td>pan_number_link</td>     <td>array</td>     <td></td>          <td>PAN Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>pan_number_link_password</td>     <td>string</td>     <td></td>          <td>PAN Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>aadhar_number</td>     <td>string</td>     <td></td>          <td>Aadhar Number of the Guarantor (12 digits)</td>       <td>794065346725</td>  </tr>        <tr>     <td>aadhar_number_link</td>     <td>array</td>     <td></td>          <td>Aadhar Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aadhar_number_link_password</td>     <td>string</td>     <td></td>          <td>Aadhar Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>voter_id_number</td>     <td>string</td>     <td></td>          <td>Voter ID Number of the Guarantor</td>       <td>RTG2291234</td>  </tr>        <tr>     <td>voting_id_number_link</td>     <td>array</td>     <td></td>          <td>Voter Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>voting_id_number_link_password</td>     <td>string</td>     <td></td>          <td>Voter Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>driving_license_number</td>     <td>string</td>     <td></td>          <td>Driving License Number of the Guarantor</td>       <td>TN01123345</td>  </tr>        <tr>     <td>driving_licence_number_link</td>     <td>array</td>     <td></td>          <td>Driving License Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>driving_licence_number_link_password</td>     <td>string</td>     <td></td>          <td>Driving License Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>passport_number</td>     <td>string</td>     <td></td>          <td>Passport Number of the Guarantor</td>       <td>L4018345</td>  </tr>        <tr>     <td>passport_number_link</td>     <td>array</td>     <td></td>          <td>Passport Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>passport_number_link_password</td>     <td>string</td>     <td></td>          <td>Passport Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>video_image_link</td>     <td>array</td>     <td></td>          <td>Video KYC of the Guarantor</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_image_link_password</td>     <td>string</td>     <td></td>          <td>Video KYC Image link Password of the Guarantor</td>       <td>12345678</td>  </tr>        <tr>     <td>video_kyc_detail</td>     <td>object</td>     <td></td>     <td>Refer table VideoKycDetail for attributes</td>       <td>{&quot;profile_id&quot;:&quot;abc12345&quot;,&quot;account_id&quot;:&quot;abc12345&quot;,&quot;key&quot;:&quot;abc@123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}</td>  </tr>        <tr>     <td>other_kyc_number</td>     <td>string</td>     <td></td>          <td>KYC Number of the Guarantor</td>       <td>other_kyc_number_21</td>  </tr>        <tr>     <td>other_kyc_number_link</td>     <td>array</td>     <td></td>          <td>KYC Image of the Guarantor</td>       <td>[&quot;abc12345&quot;, &quot;abc12345&quot;]</td>  </tr>        <tr>     <td>other_kyc_number_link_password</td>     <td>string</td>     <td></td>          <td>KYC Image Link Password of the Guarantor</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>rent_agreement_link</td>     <td>array</td>     <td></td>          <td>Rent Agreement Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>rent_agreement_link_password</td>     <td>string</td>     <td></td>          <td>Rent Agreement Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>utility_bills_link</td>     <td>array</td>     <td></td>          <td>Utility Bills Copies (If any)</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>utility_bills_link_password</td>     <td>string</td>     <td></td>          <td>Utility Bills Copies Password (If any)</td>       <td>12345678</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo Image of the Guarantor</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link_password</td>     <td>string</td>     <td></td>          <td>Photo Image Password of the Guarantor</td>       <td>12345678</td>  </tr>        <tr>     <td>marital_status</td>     <td>string</td>     <td></td>          <td>married / unmarried</td>       <td>unmarried</td>  </tr>        <tr>     <td>religion</td>     <td>string</td>     <td></td>          <td>Religion of the Guarantor</td>       <td>Hindu</td>  </tr>        <tr>     <td>nationality</td>     <td>string</td>     <td></td>          <td>Nationality of the Guarantor</td>       <td>indian</td>  </tr>        <tr>     <td>bureau_score</td>     <td>integer</td>     <td></td>          <td>Bureau Score of the Guarantor</td>       <td>700</td>  </tr>        <tr>     <td>bureau_report_link</td>     <td>array</td>     <td></td>          <td>Guarantor&#39;s Bureau Report PDF</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_report_link_password</td>     <td>string</td>     <td></td>          <td>Guarantor&#39;s Bureau Report Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>partner_score</td>     <td>number</td>     <td>float</td>          <td>Score Captured by the Partner</td>       <td>3.0</td>  </tr>    </tbody>       </table>   <h4>CoApplicants</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>relationship_with_applicant</td>     <td>string</td>     <td></td>          <td>Father/Mother/Brother/Son/Daughter/Friend/Other relative</td>       <td>father</td>  </tr>        <tr>     <td>first_name</td>     <td>string</td>     <td></td>          <td>First Name of the CoApplicant</td>       <td>Minato</td>  </tr>        <tr>     <td>middle_name</td>     <td>string</td>     <td></td>          <td>Middle Name of the CoApplicant</td>       <td>Kumar</td>  </tr>        <tr>     <td>last_name</td>     <td>string</td>     <td></td>          <td>Last Name of the CoApplicant</td>       <td>Namikaze</td>  </tr>        <tr>     <td>gender</td>     <td>string</td>     <td></td>          <td>M / F / O</td>       <td>M</td>  </tr>        <tr>     <td>date_of_birth</td>     <td>string</td>     <td>date</td>          <td>Date of Birth (YYYY-MM-DD)</td>       <td>1995-12-05</td>  </tr>        <tr>     <td>age</td>     <td>integer</td>     <td></td>          <td>Age in years</td>       <td>26</td>  </tr>        <tr>     <td>mobile_number</td>     <td>integer</td>     <td></td>          <td>Mobile Number of the CoApplicant (10 digits)</td>       <td>9876543210</td>  </tr>        <tr>     <td>email</td>     <td>string</td>     <td></td>          <td>Personal Email ID of the CoApplicant</td>       <td>minato@gmail.com</td>  </tr>        <tr>     <td>current_address</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>2, Mount Road, Teynampet</td>  </tr>        <tr>     <td>current_city</td>     <td>string</td>     <td></td>          <td>City in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_city_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for the current city</td>       <td>tier_1</td>  </tr>        <tr>     <td>current_district</td>     <td>string</td>     <td></td>          <td>District in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_state</td>     <td>string</td>     <td></td>          <td>State in which CoApplicant is currently residing</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>current_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_current_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>rented</td>  </tr>        <tr>     <td>years_of_stay_in_current_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the current address</td>       <td>5</td>  </tr>        <tr>     <td>permanent_address</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>2, Mount Road, Teynampet</td>  </tr>        <tr>     <td>permanent_city</td>     <td>string</td>     <td></td>          <td>City in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_city_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for the permanent city</td>       <td>tier_1</td>  </tr>        <tr>     <td>permanent_district</td>     <td>string</td>     <td></td>          <td>District in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_state</td>     <td>string</td>     <td></td>          <td>State in which CoApplicant is currently residing</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>permanent_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_permanent_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>owned</td>  </tr>        <tr>     <td>years_of_stay_in_permanent_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the permanent address</td>       <td>5</td>  </tr>        <tr>     <td>marital_status</td>     <td>string</td>     <td></td>          <td>Married / Unmarried</td>       <td>unmarried</td>  </tr>        <tr>     <td>religion</td>     <td>string</td>     <td></td>          <td>Religion of the CoApplicant</td>       <td>buddhist</td>  </tr>        <tr>     <td>nationality</td>     <td>string</td>     <td></td>          <td>Nationality of the CoApplicant</td>       <td>indian</td>  </tr>        <tr>     <td>father_name</td>     <td>string</td>     <td></td>          <td>Father Name of the CoApplicant</td>       <td>Dan Kato</td>  </tr>        <tr>     <td>mother_name</td>     <td>string</td>     <td></td>          <td>Mother Name of the CoApplicant</td>       <td>Tsunade Senju</td>  </tr>        <tr>     <td>spouse_name</td>     <td>string</td>     <td></td>          <td>Spouse Name of the CoApplicant</td>       <td>Kushina Uzumaki</td>  </tr>        <tr>     <td>education</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>Hokage</td>  </tr>        <tr>     <td>annual_income</td>     <td>number</td>     <td>float</td>          <td>Annual Income of the CoApplicant (in Rupees)</td>       <td>120000.0</td>  </tr>        <tr>     <td>income_proof_link</td>     <td>array</td>     <td></td>          <td>CoApplicant Income Proof Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>income_proof_link_password</td>     <td>string</td>     <td></td>          <td>CoApplicant Income Proof Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>bank_statement_link</td>     <td>array</td>     <td></td>          <td>CoApplicant Bank Statement Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bank_statement_link_password</td>     <td>string</td>     <td></td>          <td>CoApplicant Bank Statement Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>pan_number</td>     <td>string</td>     <td></td>          <td>PAN Number of the CoApplicant (10 digit Alphanumeric)</td>       <td>BMMPG9018Y</td>  </tr>        <tr>     <td>pan_number_link</td>     <td>array</td>     <td></td>          <td>PAN Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>pan_number_link_password</td>     <td>string</td>     <td></td>          <td>PAN Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>aadhar_number</td>     <td>string</td>     <td></td>          <td>Aadhar Number of the CoApplicant (12 digits)</td>       <td>794065346725</td>  </tr>        <tr>     <td>aadhar_number_link</td>     <td>array</td>     <td></td>          <td>Aadhar Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aadhar_number_link_password</td>     <td>string</td>     <td></td>          <td>Aadhar Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>voter_id_number</td>     <td>string</td>     <td></td>          <td>Voter ID Number of the CoApplicant</td>       <td>RTG2291234</td>  </tr>        <tr>     <td>voting_id_number_link</td>     <td>array</td>     <td></td>          <td>Voter Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>voting_id_number_link_password</td>     <td>string</td>     <td></td>          <td>Voter Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>driving_license_number</td>     <td>string</td>     <td></td>          <td>Driving License Number of the CoApplicant</td>       <td>TN01123345</td>  </tr>        <tr>     <td>driving_licence_number_link</td>     <td>array</td>     <td></td>          <td>Driving License Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>driving_licence_number_link_password</td>     <td>string</td>     <td></td>          <td>Driving License Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>passport_number</td>     <td>string</td>     <td></td>          <td>Passport Number of the CoApplicant</td>       <td>L4018345</td>  </tr>        <tr>     <td>passport_number_link</td>     <td>array</td>     <td></td>          <td>Passport Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>passport_number_link_password</td>     <td>string</td>     <td></td>          <td>Passport Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>video_image_link</td>     <td>array</td>     <td></td>          <td>Video KYC of the CoApplicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_image_link_password</td>     <td>string</td>     <td></td>          <td>Video KYC Password of the CoApplicant</td>       <td>12345678</td>  </tr>        <tr>     <td>video_kyc_detail</td>     <td>object</td>     <td></td>     <td>Refer table VideoKycDetail for attributes</td>       <td>{&quot;profile_id&quot;:&quot;ABC12345&quot;,&quot;account_id&quot;:&quot;ABC12345&quot;,&quot;key&quot;:&quot;abc_123&quot;,&quot;auditor&quot;:&quot;Neeraj Chopra&quot;,&quot;officer&quot;:&quot;Neeraj Chopra&quot;}</td>  </tr>        <tr>     <td>other_kyc_number</td>     <td>string</td>     <td></td>          <td>KYC Number of the CoApplicant</td>       <td>ABC12456</td>  </tr>        <tr>     <td>other_kyc_number_link</td>     <td>array</td>     <td></td>          <td>KYC Image of the CoApplicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_kyc_number_link_password</td>     <td>string</td>     <td></td>          <td>KYC Image Password of the CoApplicant</td>       <td>12345678</td>  </tr>        <tr>     <td>rent_agreement_link</td>     <td>array</td>     <td></td>          <td>CoApplicant Rent Agreement Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>rent_agreement_link_password</td>     <td>string</td>     <td></td>          <td>CoApplicant Rent Agreement Document Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>utility_bills_link</td>     <td>array</td>     <td></td>          <td>Utility Bills Copies (If any)</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>utility_bills_link_password</td>     <td>string</td>     <td></td>          <td>Utility Bills Copies Password (If any)</td>       <td>12345678</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo Image of the CoApplicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link_password</td>     <td>string</td>     <td></td>          <td>Photo Image Password of the CoApplicant</td>       <td>12345678</td>  </tr>        <tr>     <td>bureau_score</td>     <td>integer</td>     <td></td>          <td>Bureau Score of the CoApplicant</td>       <td>700</td>  </tr>        <tr>     <td>bureau_report_link</td>     <td>array</td>     <td></td>          <td>CoApplicant&#39;s Bureau Report Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_report_link_password</td>     <td>string</td>     <td></td>          <td>CoApplicant&#39;s Bureau Report Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>employment_details_link</td>     <td>array</td>     <td></td>          <td>CoApplicant&#39;s Employment Details Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>employment_details_link_password</td>     <td>string</td>     <td></td>          <td>CoApplicant&#39;s Employment Details Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>partner_score</td>     <td>number</td>     <td>float</td>          <td>Score Captured by the Partner</td>       <td>3.0</td>  </tr>    </tbody>       </table>   <h4>BankStatement</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>bank_statement_savings_account_12_months_link</td>     <td>array</td>     <td></td>          <td>Savings bank account statement for last 12 months</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bank_statement_savings_account_12_months_link_password</td>     <td>string</td>     <td></td>          <td>Savings bank account statement for last 12 months Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>bank_statement_current_account_12_months_link</td>     <td>array</td>     <td></td>          <td>Current account bank details for last 12 months</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bank_statement_current_account_12_months_link_password</td>     <td>string</td>     <td></td>          <td>Current account bank details for last 12 months Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>no_of_inward_chq_returns_savings_account</td>     <td>integer</td>     <td></td>          <td>Number of inward cheque returns in savings account</td>       <td>3</td>  </tr>        <tr>     <td>no_of_outward_chq_returns_savings_account</td>     <td>integer</td>     <td></td>          <td>Number of outward cheque returns in savings account</td>       <td>4</td>  </tr>        <tr>     <td>no_of_inward_chq_returns_current_account</td>     <td>integer</td>     <td></td>          <td>Number of inward cheque returns in current account</td>       <td>5</td>  </tr>        <tr>     <td>no_of_outward_chq_returns_current_account</td>     <td>integer</td>     <td></td>          <td>Number of outward cheque returns in current account</td>       <td>6</td>  </tr>        <tr>     <td>bank_account_type_for_assessment</td>     <td>string</td>     <td></td>          <td>Savings / Current / Overdraft / CC</td>       <td>savings</td>  </tr>        <tr>     <td>perfios_link</td>     <td>array</td>     <td></td>          <td>Perfios report in form of document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>perfios_link_password</td>     <td>string</td>     <td></td>          <td>Perfios report in form of document - password</td>       <td>12345678</td>  </tr>        <tr>     <td>perfios_json_link</td>     <td>array</td>     <td></td>          <td>Perfios Json placed in a link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>perfios_json_link_password</td>     <td>string</td>     <td></td>          <td>Perfios Json placed in a link - password</td>       <td>12345678</td>  </tr>        <tr>     <td>perfios_json</td>     <td>array</td>     <td></td>          <td>Perfios Json response</td>       <td>[&quot;NA&quot;, &quot;NA&quot;]</td>  </tr>        <tr>     <td>finbit_link</td>     <td>array</td>     <td></td>          <td>Finbit report in form of document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>finbit_link_password</td>     <td>string</td>     <td></td>          <td>Finbit report in form of document - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>finbit_json_link</td>     <td>array</td>     <td></td>          <td>Finbit Json placed in a link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>finbit_json_link_password</td>     <td>string</td>     <td></td>          <td>FINBIT Json placed in a link - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>finbit_json</td>     <td>array</td>     <td></td>          <td>FINBIT Json response</td>       <td>[&quot;NA&quot;, &quot;NA&quot;]</td>  </tr>        <tr>     <td>abb</td>     <td>number</td>     <td>float</td>          <td>Average Bank Balance maintaiend on the EMI dates (Calculated by the Originator for the Last 12 Months)</td>       <td>25000.0</td>  </tr>        <tr>     <td>abd</td>     <td>number</td>     <td>float</td>          <td>Average Monthly Bank Deposits for the Last 12 Months</td>       <td>10000.0</td>  </tr>        <tr>     <td>credit_summation</td>     <td>string</td>     <td></td>          <td>Sum of all the credits in the bank statement</td>       <td>50000</td>  </tr>    </tbody>       </table>   <h4>FinancialData</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>annual_business_turnover</td>     <td>number</td>     <td>float</td>          <td>Annual Business Turnover (in Rupees)</td>       <td>1000000.0</td>  </tr>        <tr>     <td>annual_gross_profit</td>     <td>number</td>     <td>float</td>          <td>Annual Gross Profit (in Rupees)</td>       <td>8000000.0</td>  </tr>        <tr>     <td>annual_business_ebitda</td>     <td>number</td>     <td>float</td>          <td>Annual Business EBITDA (in Rupees)</td>       <td>5000000.0</td>  </tr>        <tr>     <td>monthly_net_profit</td>     <td>number</td>     <td>float</td>          <td>Monthly Net Profit (in Rupees)</td>       <td>14000.0</td>  </tr>        <tr>     <td>annual_net_income</td>     <td>integer</td>     <td></td>          <td>Annual Net Income</td>       <td>4000000</td>  </tr>        <tr>     <td>annual_net_profit</td>     <td>number</td>     <td>float</td>          <td>Net Profit After Tax (in Rupees)</td>       <td>30000000.0</td>  </tr>        <tr>     <td>gst_annual_turnover</td>     <td>integer</td>     <td></td>          <td>GST Annual Turnover</td>       <td>20000</td>  </tr>        <tr>     <td>gst_return_year_1_link</td>     <td>array</td>     <td></td>          <td>GST return image for last year</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>gst_return_year_1_link_password</td>     <td>string</td>     <td></td>          <td>GST return image password for last year</td>       <td>12345678</td>  </tr>        <tr>     <td>gst_return_year_2_link</td>     <td>array</td>     <td></td>          <td>GST return image for last year -1</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>gst_return_year_2_link_password</td>     <td>string</td>     <td></td>          <td>GST return image password for last year -1</td>       <td>12345678</td>  </tr>        <tr>     <td>gst_return_year_3_link</td>     <td>array</td>     <td></td>          <td>GST return image for last year -2</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>gst_return_year_3_link_password</td>     <td>string</td>     <td></td>          <td>GST return image password for last year -2</td>       <td>12345678</td>  </tr>        <tr>     <td>it_return_year_1_link</td>     <td>array</td>     <td></td>          <td>IT return image for last year</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>it_return_year_1_link_password</td>     <td>string</td>     <td></td>          <td>IT return image password for last year</td>       <td>12345678</td>  </tr>        <tr>     <td>it_return_year_2_link</td>     <td>array</td>     <td></td>          <td>IT return image for last year -1</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>it_return_year_2_link_password</td>     <td>string</td>     <td></td>          <td>IT return image for last year -1</td>       <td>12345678</td>  </tr>        <tr>     <td>it_return_year_3_link</td>     <td>array</td>     <td></td>          <td>IT return image for last year - 2</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>it_return_year_3_link_password</td>     <td>string</td>     <td></td>          <td>IT return image for last year - 2</td>       <td>12345678</td>  </tr>        <tr>     <td>other_income_assesment_proof_link</td>     <td>array</td>     <td></td>          <td>Image of other bills</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_income_assesment_proof_link_password</td>     <td>string</td>     <td></td>          <td>Image password of other bills</td>       <td>12345678</td>  </tr>        <tr>     <td>cam_link</td>     <td>array</td>     <td></td>          <td>CAM Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>cam_link_password</td>     <td>string</td>     <td></td>          <td>CAM Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>cfa_link</td>     <td>array</td>     <td></td>          <td>CFA Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>cfa_link_password</td>     <td>string</td>     <td></td>          <td>CFA Document Password</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>DisbursementAccounts</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>account_type</td>     <td>string</td>     <td></td>          <td>borrower / existing_lender / dealer / sub_dealer / seller / financier</td>       <td>dealer</td>  </tr>        <tr>     <td>bank_name</td>     <td>string</td>     <td></td>          <td>Name of the bank where disbursement needs to be done</td>       <td>HDFC</td>  </tr>        <tr>     <td>bank_account_type</td>     <td>string</td>     <td></td>          <td>Account type - Savings/Current/Overdraft/CC</td>       <td>savings</td>  </tr>        <tr>     <td>account_name</td>     <td>string</td>     <td></td>          <td>Bank account name where disbursement needs to be done</td>       <td>Neeraj Chopra</td>  </tr>        <tr>     <td>date_of_bank_account_opening</td>     <td>string</td>     <td>date</td>          <td>Date on which the bank account is opened</td>       <td>1995-01-01</td>  </tr>        <tr>     <td>bank_branch_name</td>     <td>string</td>     <td></td>          <td>Bank branch name where disbursement needs to be done</td>       <td>Rajaji Salai</td>  </tr>        <tr>     <td>ifsc_code</td>     <td>string</td>     <td></td>          <td>Bank IFSC where disbursement needs to be done</td>       <td>HDFC000123</td>  </tr>        <tr>     <td>entity_type</td>     <td>string</td>     <td></td>          <td>dealer / sub_dealer / originator / existing_lender / end_customer</td>       <td>dealer</td>  </tr>        <tr>     <td>account_no</td>     <td>string</td>     <td></td>          <td>Account number of the bank where disbursement needs to be done</td>       <td>1234567890</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Amount to be transferred to particular Vendor/Borrower</td>       <td>10000.0</td>  </tr>    </tbody>       </table>   <h4>Assets</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>asset_category</td>     <td>string</td>     <td></td>          <td>Residential/Commercial/Plot/Vacant/Machinery/LIC/FD/Mutual Funds/Vehicle/Bonds/KVB patra/Post Office Schemes</td>       <td>residential</td>  </tr>        <tr>     <td>asset_owned_by</td>     <td>string</td>     <td></td>          <td>Name of owner</td>       <td>Polygon</td>  </tr>        <tr>     <td>relationship_to_the_business</td>     <td>string</td>     <td></td>          <td>Promoter/Family/Partner</td>       <td>Promoter</td>  </tr>        <tr>     <td>asset_value_self_declared</td>     <td>string</td>     <td></td>          <td>Approx asset value</td>       <td>100000</td>  </tr>        <tr>     <td>asset_market_value</td>     <td>string</td>     <td></td>          <td>Asset market value</td>       <td>80000</td>  </tr>        <tr>     <td>ltv_asset_market_value</td>     <td>string</td>     <td></td>          <td>Ltv market value</td>       <td>50000</td>  </tr>        <tr>     <td>area_type</td>     <td>string</td>     <td></td>          <td>Urban/Rural/Semi-urban</td>       <td>Urban</td>  </tr>        <tr>     <td>ltv_asset_value_self_declared</td>     <td>number</td>     <td>float</td>          <td>LTV asset image for last self declared</td>       <td>100000.0</td>  </tr>        <tr>     <td>age_of_the_collateral</td>     <td>integer</td>     <td></td>          <td>Age of the collateral</td>       <td>4</td>  </tr>        <tr>     <td>mortgage_in_favour_of</td>     <td>string</td>     <td></td>          <td>Mortgagee in whose name the lien on the mortgage is being placed</td>       <td>PNB Housing</td>  </tr>        <tr>     <td>machinery_type</td>     <td>string</td>     <td></td>          <td>Which type of machinery is it?</td>       <td>Heavy machinery</td>  </tr>        <tr>     <td>hypothecation_value</td>     <td>number</td>     <td>float</td>          <td>Hypothecation value</td>       <td>2000.0</td>  </tr>        <tr>     <td>hypothecation_percentage</td>     <td>number</td>     <td>float</td>          <td>Hypothecation Percentage</td>       <td>35.0</td>  </tr>        <tr>     <td>new_machinery_value</td>     <td>number</td>     <td>float</td>          <td>Value of New Machinery</td>       <td>30000.0</td>  </tr>        <tr>     <td>old_machinery_value</td>     <td>number</td>     <td>float</td>          <td>Value of Old Machinery</td>       <td>10000.0</td>  </tr>        <tr>     <td>new_machinery_ltv</td>     <td>number</td>     <td>float</td>          <td>LTV of New Machinery</td>       <td>20000.0</td>  </tr>        <tr>     <td>old_machinery_ltv</td>     <td>number</td>     <td>float</td>          <td>LTV of Old Machinery</td>       <td>10000.0</td>  </tr>        <tr>     <td>total_number_of_machines</td>     <td>integer</td>     <td></td>          <td>Total Number of Machines</td>       <td>4</td>  </tr>        <tr>     <td>total_value_of_machines</td>     <td>number</td>     <td>float</td>          <td>Total Value of Machines</td>       <td>500000.0</td>  </tr>        <tr>     <td>manufacturer_name</td>     <td>string</td>     <td></td>          <td>Name of the Manufacturer</td>       <td>BMW</td>  </tr>        <tr>     <td>machinery_hypothecated_to</td>     <td>string</td>     <td></td>          <td>Which institution/ individual is the machinery hypothecated to currently?</td>       <td>Neeraj</td>  </tr>        <tr>     <td>property_address</td>     <td>string</td>     <td></td>          <td>Property address</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>property_city</td>     <td>string</td>     <td></td>          <td>Property City</td>       <td>Chennai</td>  </tr>        <tr>     <td>property_district</td>     <td>string</td>     <td></td>          <td>Property District</td>       <td>Chennai</td>  </tr>        <tr>     <td>property_state</td>     <td>string</td>     <td></td>          <td>Property State</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>property_pincode</td>     <td>integer</td>     <td></td>          <td>Property Pincode</td>       <td>600025</td>  </tr>    </tbody>       </table>   <h4>References</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>name</td>     <td>string</td>     <td></td>          <td>Name of reference</td>       <td>Neeraj Chopra</td>  </tr>        <tr>     <td>address</td>     <td>string</td>     <td></td>          <td>Address details of reference</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>pincode</td>     <td>string</td>     <td></td>          <td>Pincode of reference address</td>       <td>600001</td>  </tr>        <tr>     <td>phone</td>     <td>string</td>     <td></td>          <td>Phone number of reference</td>       <td>9876543210</td>  </tr>    </tbody>       </table>   <h4>InsuranceDetails</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>insurance_type</td>     <td>string</td>     <td></td>          <td>Enter &#39;credit&#39;</td>       <td>credit</td>  </tr>        <tr>     <td>insurer_name</td>     <td>string</td>     <td></td>          <td>Loan Insurer Name</td>       <td>Tata AIG</td>  </tr>        <tr>     <td>nominee_details</td>     <td>string</td>     <td></td>          <td>Applicable if Credit Shield insurance is taken. Name of the nominee to be provided</td>       <td>Neeraj</td>  </tr>        <tr>     <td>nominee_date_of_birth</td>     <td>string</td>     <td>date</td>          <td>Applicable if Credit Shield insurance is taken. DOB of the nominee to be provided</td>       <td>1990-01-01</td>  </tr>        <tr>     <td>relationship</td>     <td>string</td>     <td></td>          <td>Applicable if Credit Shield insurance is taken. Relationship of nominee to be provided</td>       <td>friend</td>  </tr>        <tr>     <td>premium</td>     <td>number</td>     <td>float</td>          <td>Applicable if Credit Shield insurance is taken. Premium amount</td>       <td>100000.0</td>  </tr>        <tr>     <td>insurance_amount</td>     <td>number</td>     <td>float</td>          <td>Applicable if Credit Shield insurance is taken. Total insurance amount</td>       <td>300000.0</td>  </tr>        <tr>     <td>policy_number</td>     <td>integer</td>     <td></td>          <td>Applicable if Credit Shield insurance is taken. Policy number</td>       <td>0</td>  </tr>    </tbody>       </table>   <h4>Tranches</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>tranche_number</td>     <td>integer</td>     <td></td>          <td>Tranche Number</td>       <td>1</td>  </tr>        <tr>     <td>principal_amount</td>     <td>integer</td>     <td></td>          <td>Principal amount to be disbursed in the tranche</td>       <td>10000</td>  </tr>        <tr>     <td>differential_interest</td>     <td>integer</td>     <td></td>          <td>Broken period interest amount</td>       <td>100</td>  </tr>        <tr>     <td>processing_fee</td>     <td>integer</td>     <td></td>          <td>Processing fee amount (Inckusive of GST)</td>       <td>50</td>  </tr>        <tr>     <td>stamp_duty</td>     <td>integer</td>     <td></td>          <td>Stamp duty amount</td>       <td>100</td>  </tr>        <tr>     <td>insurance_charges</td>     <td>integer</td>     <td></td>          <td>Insurance premium inclusive of GST</td>       <td>100</td>  </tr>        <tr>     <td>documentation_charges</td>     <td>integer</td>     <td></td>          <td>Total documentation charges inclusive of GST</td>       <td>100</td>  </tr>        <tr>     <td>other_charges</td>     <td>integer</td>     <td></td>          <td>Any other charges inclusive of GST</td>       <td>100</td>  </tr>        <tr>     <td>closing_loan_principal</td>     <td>integer</td>     <td></td>          <td>Balance principal amount after this tranche</td>       <td>5000</td>  </tr>    </tbody>       </table>   <h4>LinkedLoanInfos</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>linked_loan_id</td>     <td>string</td>     <td></td>          <td>client Loan id of the loan that have to be linked to the current loan</td>       <td>CA_123</td>  </tr>        <tr>     <td>foreclosure</td>     <td>string</td>     <td></td>          <td>whether the loan has to be foreclosed or not. true/false</td>       <td>t</td>  </tr>        <tr>     <td>principal</td>     <td>number</td>     <td>float</td>          <td>Foreclosure principal for corresponding Linked loan being foreclosed</td>       <td>1000.0</td>  </tr>        <tr>     <td>interest</td>     <td>number</td>     <td>float</td>          <td>Foreclosure interest for corresponding Linked loan being foreclosed</td>       <td>100.0</td>  </tr>        <tr>     <td>other_charges</td>     <td>number</td>     <td>float</td>          <td>Foreclosure charges for corresponding Linked loan being foreclosed</td>       <td>50.0</td>  </tr>        <tr>     <td>overdue_charges</td>     <td>number</td>     <td>float</td>          <td>Foreclosure charges for corresponding Linked loan being foreclosed</td>       <td>100.0</td>  </tr>        <tr>     <td>penalty_charges</td>     <td>number</td>     <td>float</td>          <td>Foreclosure charges for corresponding Linked loan being foreclosed</td>       <td>100.0</td>  </tr>        <tr>     <td>fee_charges</td>     <td>number</td>     <td>float</td>          <td>Foreclosure charges for corresponding Linked loan being foreclosed</td>       <td>100.0</td>  </tr>        <tr>     <td>bounce_charges</td>     <td>number</td>     <td>float</td>          <td>Foreclosure charges for corresponding Linked loan being foreclosed</td>       <td>100.0</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Foreclosure charges for corresponding Linked loan being foreclosed</td>       <td>100.0</td>  </tr>    </tbody>       </table>   <h4>SourcingDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>source_code</td>     <td>string</td>     <td></td>          <td>Originating system code</td>       <td>PNB</td>  </tr>        <tr>     <td>referrer_code</td>     <td>string</td>     <td></td>          <td>Referrer code in the financial institution&#39;s own CRM system</td>       <td>referrer_code_34</td>  </tr>        <tr>     <td>referrer_group</td>     <td>string</td>     <td></td>          <td>Referrer banking vertical in the financial institution&#39;s own CRM system</td>       <td>referrer_group_44</td>  </tr>        <tr>     <td>referrer_name</td>     <td>string</td>     <td></td>          <td>Name of the lead referrer</td>       <td>Albus</td>  </tr>        <tr>     <td>channel_code</td>     <td>string</td>     <td></td>          <td>Which channel of sourcing it was?</td>       <td>DSA sourcing</td>  </tr>        <tr>     <td>dst_code</td>     <td>string</td>     <td></td>          <td></td>       <td>dst_code_48</td>  </tr>        <tr>     <td>dsa</td>     <td>string</td>     <td></td>          <td>Name of the Direct Selling Agent</td>       <td>John Pvt Ltd.</td>  </tr>        <tr>     <td>dse</td>     <td>string</td>     <td></td>          <td>Name of the Direct Selling Executive</td>       <td>John</td>  </tr>        <tr>     <td>relationship_manager</td>     <td>string</td>     <td></td>          <td>Name of the Relationship Manager</td>       <td>Harry</td>  </tr>    </tbody>       </table>   <h4>DeviationDetails</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>summary</td>     <td>string</td>     <td></td>          <td>Summary details of the deviation being taken</td>       <td>This deviation refers to the nature of the segment itself where the corporate on onboarding high debt can continue to keep capex funding at optimum levels, thus TD/NCA is typically high in these funding cases</td>  </tr>        <tr>     <td>desc</td>     <td>string</td>     <td></td>          <td>Description of the deviation requested</td>       <td>High TD/NCA</td>  </tr>        <tr>     <td>mitigant</td>     <td>string</td>     <td></td>          <td>Mitigant description</td>       <td>Even though interest liabilities are higher on account of all current facilities, the company has shown substantial asset growth and cash flow has remained robust over the past 3 FY</td>  </tr>        <tr>     <td>level</td>     <td>string</td>     <td></td>          <td>Severity of the deviation being requested</td>       <td>high</td>  </tr>    </tbody>       </table>      #   > <h4>Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>201</td>     <td>created</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Invalid Request Format   Missing Required Parameters</td>   </tr>    </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>422</td>     <td>Unprocessable Entity</td>     <td>Client Loan Already Taken   Product Not Found   Document not found/accessible</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>      INDIAN STATES  - jammu_kashmir - himachal_pradesh - punjab - chandigarh - uttaranchal - haryana - delhi - rajasthan - uttar_pradesh - bihar - sikkim - arunachal_pradesh - nagaland - manipur - mizoram - tripura - meghalaya - assam - west_bengal - jharkhand - orissa - chhattisgarh - madhya_pradesh - gujarat - daman_diu - dadra_nagar_haveli - maharashtra - andhra_pradesh - karnataka - goa - lakshadweep - kerala - tamil_nadu - pondicherry - andaman_nicobar_islands - telangana

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.create_loan_success import CreateLoanSuccess
from credavenue_colending.model.create_loan_error import CreateLoanError
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.body_create_loan import BodyCreateLoan
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    body_create_loan = BodyCreateLoan(
        customer_type="customer_type_example",
        customer_category="customer_category_example",
        client_customer_id="client_customer_id_example",
        title="title_example",
        first_name="first_name_example",
        middle_name="middle_name_example",
        last_name="last_name_example",
        gender="gender_example",
        date_of_birth=dateutil_parser('1970-01-01').date(),
        age=1,
        mobile_number=1,
        phone_number=1,
        email="email_example",
        official_email_id="official_email_id_example",
        place_of_birth="place_of_birth_example",
        current_address="current_address_example",
        current_village="current_village_example",
        current_city_tier="current_city_tier_example",
        current_city="current_city_example",
        current_district="current_district_example",
        current_state="current_state_example",
        current_country="current_country_example",
        current_pincode=1,
        residence_type_current_address="residence_type_current_address_example",
        years_of_stay_in_current_address=1,
        permanent_address="permanent_address_example",
        permanent_city="permanent_city_example",
        permanent_city_tier="permanent_city_tier_example",
        permanent_district="permanent_district_example",
        permanent_state="permanent_state_example",
        permanent_pincode=1,
        residence_type_permanent_address="residence_type_permanent_address_example",
        years_of_stay_in_permanent_address=1,
        mailing_address="mailing_address_example",
        marital_status="marital_status_example",
        religion="religion_example",
        nationality="nationality_example",
        father_name="father_name_example",
        mother_name="mother_name_example",
        spouse_name="spouse_name_example",
        education_qualification="education_qualification_example",
        net_monthly_income=3.14,
        annual_income=3.14,
        no_of_dependants=1,
        occupation="occupation_example",
        partner_score_on_the_customer=3.14,
        politically_exposed="politically_exposed_example",
        income_source="income_source_example",
        applicant_profession="applicant_profession_example",
        caution_negative_profile="caution_negative_profile_example",
        udyam_number="udyam_number_example",
        pan_check="pan_check_example",
        dedupe_status="dedupe_status_example",
        pan_number="pan_number_example",
        pan_number_link=[
            "pan_number_link_example",
        ],
        pan_number_link_password="pan_number_link_password_example",
        form_60_link=[
            "form_60_link_example",
        ],
        form_60_link_password="form_60_link_password_example",
        aadhar_number="aadhar_number_example",
        aadhar_number_link=[
            "aadhar_number_link_example",
        ],
        aadhar_number_link_password="aadhar_number_link_password_example",
        voter_id_number="voter_id_number_example",
        voting_id_link=[
            "voting_id_link_example",
        ],
        voting_id_link_password="voting_id_link_password_example",
        driving_license_number="driving_license_number_example",
        driving_license_number_link=[
            "driving_license_number_link_example",
        ],
        driving_license_number_link_password="driving_license_number_link_password_example",
        driving_license_expiry_date=dateutil_parser('1970-01-01').date(),
        passport_number="passport_number_example",
        passport_number_link=[
            "passport_number_link_example",
        ],
        passport_number_link_password="passport_number_link_password_example",
        video_image_link=[
            "video_image_link_example",
        ],
        video_image_link_password="video_image_link_password_example",
        video_kyc_detail=BodyCreateLoanVideoKycDetail(
            profile_id="profile_id_example",
            account_id="account_id_example",
            key="key_example",
            auditor="auditor_example",
            officer="officer_example",
        ),
        other_kyc_number="other_kyc_number_example",
        other_kyc_link=[
            "other_kyc_link_example",
        ],
        other_kyc_link_password="other_kyc_link_password_example",
        rent_agreement_link=[
            "rent_agreement_link_example",
        ],
        rent_agreement_link_password="rent_agreement_link_password_example",
        utility_bills_link=[
            "utility_bills_link_example",
        ],
        utility_bills_link_password="utility_bills_link_password_example",
        photo_link=[
            "photo_link_example",
        ],
        photo_link_password="photo_link_password_example",
        employer_tier="employer_tier_example",
        employer_category="employer_category_example",
        employment_type="employment_type_example",
        employment_details_name="employment_details_name_example",
        employment_details_address="employment_details_address_example",
        employment_details_years_of_experience=3.14,
        employment_details_designation="employment_details_designation_example",
        employement_vintage_current_organisation=1,
        total_work_experience=3.14,
        payslip_link=[
            "payslip_link_example",
        ],
        payslip_link_password="payslip_link_password_example",
        tds_certificate_link=[
            "tds_certificate_link_example",
        ],
        tds_certificate_link_password="tds_certificate_link_password_example",
        business=BodyCreateLoanBusiness(
            name_of_business="name_of_business_example",
            nature_of_business="nature_of_business_example",
            type_of_constitution="type_of_constitution_example",
            type_of_ownership="type_of_ownership_example",
            registration_date=dateutil_parser('1970-01-01').date(),
            incorporation_date=dateutil_parser('1970-01-01').date(),
            industry_type="industry_type_example",
            sector_type="sector_type_example",
            sub_sector_type="sub_sector_type_example",
            business_vintage=1,
            business_registered_office_address="business_registered_office_address_example",
            business_registered_office_district="business_registered_office_district_example",
            business_registered_office_city="business_registered_office_city_example",
            business_registered_office_state="business_registered_office_state_example",
            business_registered_office_pincode=1,
            business_mailing_office_address="business_mailing_office_address_example",
            business_mailing_office_city="business_mailing_office_city_example",
            business_mailing_office_state="business_mailing_office_state_example",
            business_mailing_office_pincode=1,
            business_registered_office_link=[
                "business_registered_office_link_example",
            ],
            business_registered_office_link_password="business_registered_office_link_password_example",
            business_mailing_office_link=[
                "business_mailing_office_link_example",
            ],
            business_mailing_office_link_password="business_mailing_office_link_password_example",
            business_phone_number=[
                1,
            ],
            business_email_id=[
                "business_email_id_example",
            ],
            business_partner_score=3.14,
            business_pan_number="business_pan_number_example",
            business_pan_link=[
                "business_pan_link_example",
            ],
            business_pan_link_password="business_pan_link_password_example",
            business_rc_number="business_rc_number_example",
            business_rc_link=[
                "business_rc_link_example",
            ],
            business_rc_link_password="business_rc_link_password_example",
            business_gst_number="business_gst_number_example",
            business_gst_copy_link=[
                "business_gst_copy_link_example",
            ],
            business_gst_copy_link_password="business_gst_copy_link_password_example",
            business_udyog_aadhar_number="business_udyog_aadhar_number_example",
            business_udyog_aadhar_link=[
                "business_udyog_aadhar_link_example",
            ],
            business_udyog_aadhar_link_password="business_udyog_aadhar_link_password_example",
            business_ssi_number="business_ssi_number_example",
            business_ssi_link=[
                "business_ssi_link_example",
            ],
            business_ssi_link_password="business_ssi_link_password_example",
            business_shops_est_number="business_shops_est_number_example",
            business_shops_est_link=[
                "business_shops_est_link_example",
            ],
            business_shops_est_link_password="business_shops_est_link_password_example",
            business_factory_regn_number="business_factory_regn_number_example",
            business_factory_regn_link=[
                "business_factory_regn_link_example",
            ],
            business_factory_regn_link_password="business_factory_regn_link_password_example",
            business_trade_license_number="business_trade_license_number_example",
            business_trade_license_link=[
                "business_trade_license_link_example",
            ],
            business_trade_license_link_password="business_trade_license_link_password_example",
            business_place_photo_link=[
                "business_place_photo_link_example",
            ],
            business_place_photo_link_password="business_place_photo_link_password_example",
            business_continuity_proof_link=[
                "business_continuity_proof_link_example",
            ],
            business_continuity_proof_link_password="business_continuity_proof_link_password_example",
            other_business_address_proof_number="other_business_address_proof_number_example",
            other_business_address_proof_link=[
                "other_business_address_proof_link_example",
            ],
            other_business_address_proof_link_password="other_business_address_proof_link_password_example",
            no_of_business_authorised_persons=1,
            partnerships=[
                BodyCreateLoanBusinessPartnerships(
                    partnership_type="partnership_type_example",
                    name="name_example",
                    poi_number="poi_number_example",
                    poi_link=[
                        "poi_link_example",
                    ],
                    poi_link_password="poi_link_password_example",
                    poa_number="poa_number_example",
                    poa_link=[
                        "poa_link_example",
                    ],
                    poa_link_password="poa_link_password_example",
                    photo_link=[
                        "photo_link_example",
                    ],
                    photo_link_password="photo_link_password_example",
                ),
            ],
            partnership_detail=BodyCreateLoanBusinessPartnershipDetail(
                partnership_firm_pan="partnership_firm_pan_example",
                partnership_pan_link=[
                    "partnership_pan_link_example",
                ],
                partnership_pan_link_password="partnership_pan_link_password_example",
                partnership_deed_link=[
                    "partnership_deed_link_example",
                ],
                partnership_deed_link_password="partnership_deed_link_password_example",
                beneficiary_owner_details_link=[
                    "beneficiary_owner_details_link_example",
                ],
                beneficiary_owner_details_link_password="beneficiary_owner_details_link_password_example",
            ),
            private_entity_detail=BodyCreateLoanBusinessPrivateEntityDetail(
                cin_number="cin_number_example",
                cin_link=[
                    "cin_link_example",
                ],
                cin_link_password="cin_link_password_example",
                moa_link=[
                    "moa_link_example",
                ],
                moa_link_password="moa_link_password_example",
                aoa_link=[
                    "aoa_link_example",
                ],
                aoa_link_password="aoa_link_password_example",
                board_resoultion_link=[
                    "board_resoultion_link_example",
                ],
                board_resoultion_link_password="board_resoultion_link_password_example",
                share_holding_pattern_link=[
                    "share_holding_pattern_link_example",
                ],
                share_holding_pattern_link_password="share_holding_pattern_link_password_example",
                other_company_proof="other_company_proof_example",
                other_company_proof_link=[
                    "other_company_proof_link_example",
                ],
                other_company_proof_link_password="other_company_proof_link_password_example",
            ),
        ),
        guarantors=[
            BodyCreateLoanGuarantors(
                relationship_with_applicant="relationship_with_applicant_example",
                first_name="first_name_example",
                middle_name="middle_name_example",
                last_name="last_name_example",
                date_of_birth=dateutil_parser('1970-01-01').date(),
                age=1,
                gender="gender_example",
                current_address="current_address_example",
                current_district="current_district_example",
                current_city="current_city_example",
                current_city_tier="current_city_tier_example",
                current_state="current_state_example",
                current_pincode=1,
                years_of_stay_in_current_address=1,
                residence_type_current_address="residence_type_current_address_example",
                permanent_address="permanent_address_example",
                permanent_district="permanent_district_example",
                permanent_city="permanent_city_example",
                permanent_city_tier="permanent_city_tier_example",
                permanent_state="permanent_state_example",
                permanent_pincode=1,
                years_of_stay_in_permanent_address=1,
                residence_type_permanent_address="residence_type_permanent_address_example",
                mobile_number=1,
                email="email_example",
                pan_number="pan_number_example",
                pan_number_link=[
                    "pan_number_link_example",
                ],
                pan_number_link_password="pan_number_link_password_example",
                aadhar_number="aadhar_number_example",
                aadhar_number_link=[
                    "aadhar_number_link_example",
                ],
                aadhar_number_link_password="aadhar_number_link_password_example",
                voter_id_number="voter_id_number_example",
                voting_id_number_link=[
                    "voting_id_number_link_example",
                ],
                voting_id_number_link_password="voting_id_number_link_password_example",
                driving_license_number="driving_license_number_example",
                driving_licence_number_link=[
                    "driving_licence_number_link_example",
                ],
                driving_licence_number_link_password="driving_licence_number_link_password_example",
                passport_number="passport_number_example",
                passport_number_link=[
                    "passport_number_link_example",
                ],
                passport_number_link_password="passport_number_link_password_example",
                video_image_link=[
                    "video_image_link_example",
                ],
                video_image_link_password="video_image_link_password_example",
                video_kyc_detail=BodyCreateLoanVideoKycDetail(
                    profile_id="profile_id_example",
                    account_id="account_id_example",
                    key="key_example",
                    auditor="auditor_example",
                    officer="officer_example",
                ),
                other_kyc_number="other_kyc_number_example",
                other_kyc_number_link=[
                    "other_kyc_number_link_example",
                ],
                other_kyc_number_link_password="other_kyc_number_link_password_example",
                rent_agreement_link=[
                    "rent_agreement_link_example",
                ],
                rent_agreement_link_password="rent_agreement_link_password_example",
                utility_bills_link=[
                    "utility_bills_link_example",
                ],
                utility_bills_link_password="utility_bills_link_password_example",
                photo_link=[
                    "photo_link_example",
                ],
                photo_link_password="photo_link_password_example",
                marital_status="marital_status_example",
                religion="religion_example",
                nationality="nationality_example",
                bureau_score=1,
                bureau_report_link=[
                    "bureau_report_link_example",
                ],
                bureau_report_link_password="bureau_report_link_password_example",
                partner_score=3.14,
            ),
        ],
        co_applicants=[
            BodyCreateLoanCoApplicants(
                relationship_with_applicant="relationship_with_applicant_example",
                first_name="first_name_example",
                middle_name="middle_name_example",
                last_name="last_name_example",
                gender="gender_example",
                date_of_birth=dateutil_parser('1970-01-01').date(),
                age=1,
                mobile_number=1,
                email="email_example",
                current_address="current_address_example",
                current_city="current_city_example",
                current_city_tier="current_city_tier_example",
                current_district="current_district_example",
                current_state="current_state_example",
                current_pincode=1,
                residence_type_current_address="residence_type_current_address_example",
                years_of_stay_in_current_address=1,
                permanent_address="permanent_address_example",
                permanent_city="permanent_city_example",
                permanent_city_tier="permanent_city_tier_example",
                permanent_district="permanent_district_example",
                permanent_state="permanent_state_example",
                permanent_pincode=1,
                residence_type_permanent_address="residence_type_permanent_address_example",
                years_of_stay_in_permanent_address=1,
                marital_status="marital_status_example",
                religion="religion_example",
                nationality="nationality_example",
                father_name="father_name_example",
                mother_name="mother_name_example",
                spouse_name="spouse_name_example",
                education="education_example",
                annual_income=3.14,
                income_proof_link=[
                    "income_proof_link_example",
                ],
                income_proof_link_password="income_proof_link_password_example",
                bank_statement_link=[
                    "bank_statement_link_example",
                ],
                bank_statement_link_password="bank_statement_link_password_example",
                pan_number="pan_number_example",
                pan_number_link=[
                    "pan_number_link_example",
                ],
                pan_number_link_password="pan_number_link_password_example",
                aadhar_number="aadhar_number_example",
                aadhar_number_link=[
                    "aadhar_number_link_example",
                ],
                aadhar_number_link_password="aadhar_number_link_password_example",
                voter_id_number="voter_id_number_example",
                voting_id_number_link=[
                    "voting_id_number_link_example",
                ],
                voting_id_number_link_password="voting_id_number_link_password_example",
                driving_license_number="driving_license_number_example",
                driving_licence_number_link=[
                    "driving_licence_number_link_example",
                ],
                driving_licence_number_link_password="driving_licence_number_link_password_example",
                passport_number="passport_number_example",
                passport_number_link=[
                    "passport_number_link_example",
                ],
                passport_number_link_password="passport_number_link_password_example",
                video_image_link=[
                    "video_image_link_example",
                ],
                video_image_link_password="video_image_link_password_example",
                video_kyc_detail=BodyCreateLoanVideoKycDetail(
                    profile_id="profile_id_example",
                    account_id="account_id_example",
                    key="key_example",
                    auditor="auditor_example",
                    officer="officer_example",
                ),
                other_kyc_number="other_kyc_number_example",
                other_kyc_number_link=[
                    "other_kyc_number_link_example",
                ],
                other_kyc_number_link_password="other_kyc_number_link_password_example",
                rent_agreement_link=[
                    "rent_agreement_link_example",
                ],
                rent_agreement_link_password="rent_agreement_link_password_example",
                utility_bills_link=[
                    "utility_bills_link_example",
                ],
                utility_bills_link_password="utility_bills_link_password_example",
                photo_link=[
                    "photo_link_example",
                ],
                photo_link_password="photo_link_password_example",
                bureau_score=1,
                bureau_report_link=[
                    "bureau_report_link_example",
                ],
                bureau_report_link_password="bureau_report_link_password_example",
                employment_details_link=[
                    "employment_details_link_example",
                ],
                employment_details_link_password="employment_details_link_password_example",
                partner_score=3.14,
            ),
        ],
        bank_statement=BodyCreateLoanBankStatement(
            bank_statement_savings_account_12_months_link=[
                "bank_statement_savings_account_12_months_link_example",
            ],
            bank_statement_savings_account_12_months_link_password="bank_statement_savings_account_12_months_link_password_example",
            bank_statement_current_account_12_months_link=[
                "bank_statement_current_account_12_months_link_example",
            ],
            bank_statement_current_account_12_months_link_password="bank_statement_current_account_12_months_link_password_example",
            no_of_inward_chq_returns_savings_account=1,
            no_of_outward_chq_returns_savings_account=1,
            no_of_inward_chq_returns_current_account=1,
            no_of_outward_chq_returns_current_account=1,
            bank_account_type_for_assessment="bank_account_type_for_assessment_example",
            perfios_link=[
                "perfios_link_example",
            ],
            perfios_link_password="perfios_link_password_example",
            perfios_json_link=[
                "perfios_json_link_example",
            ],
            perfios_json_link_password="perfios_json_link_password_example",
            perfios_json=[
                "perfios_json_example",
            ],
            finbit_link=[
                "finbit_link_example",
            ],
            finbit_link_password="finbit_link_password_example",
            finbit_json_link=[
                "finbit_json_link_example",
            ],
            finbit_json_link_password="finbit_json_link_password_example",
            finbit_json=[
                "finbit_json_example",
            ],
            abb=3.14,
            abd=3.14,
            credit_summation="credit_summation_example",
        ),
        name_of_bureau="name_of_bureau_example",
        bureau_vintage=1,
        bureau_score=1,
        bureau_report_json_link=[
            "bureau_report_json_link_example",
        ],
        bureau_report_json_link_password="bureau_report_json_link_password_example",
        bureau_json_link=[
            "bureau_json_link_example",
        ],
        bureau_json_link_password="bureau_json_link_password_example",
        bureau_json=[
            "bureau_json_example",
        ],
        commercial_bureau_score=1,
        commercial_bureau_score_link=[
            "commercial_bureau_score_link_example",
        ],
        commercial_bureau_score_link_password="commercial_bureau_score_link_password_example",
        partner_score_on_the_customer_including_bureau_report=3.14,
        total_existing_obligations=1,
        credit_card_limit=1,
        no_of_credit_cards=1,
        total_number_of_unsecured_loans=1,
        value_of_total_unsecured_loans=3.14,
        total_number_of_loans=1,
        value_of_total_loans=3.14,
        number_of_enquiries_3months=1,
        number_of_enquiries_6months=1,
        number_of_enquiries_12months=1,
        number_of_writeoff_suitfiled_settled_in_the_last_12_months=1,
        max_dpd_tradeline_last_12months=1,
        max_overdue_tradeline=1,
        total_overdue_amount_in_last_12m=3.14,
        amount_of_loan_settled_in_last_12m=3.14,
        nature_of_loan_settled1="nature_of_loan_settled1_example",
        nature_of_loan_settled2="nature_of_loan_settled2_example",
        total_emi_bounces=1,
        bounces_in_last_6m=1,
        bounces_in_last_12m=1,
        bureau_validity_date=dateutil_parser('1970-01-01').date(),
        financial_data=BodyCreateLoanFinancialData(
            annual_business_turnover=3.14,
            annual_gross_profit=3.14,
            annual_business_ebitda=3.14,
            monthly_net_profit=3.14,
            annual_net_income=1,
            annual_net_profit=3.14,
            gst_annual_turnover=1,
            gst_return_year_1_link=[
                "gst_return_year_1_link_example",
            ],
            gst_return_year_1_link_password="gst_return_year_1_link_password_example",
            gst_return_year_2_link=[
                "gst_return_year_2_link_example",
            ],
            gst_return_year_2_link_password="gst_return_year_2_link_password_example",
            gst_return_year_3_link=[
                "gst_return_year_3_link_example",
            ],
            gst_return_year_3_link_password="gst_return_year_3_link_password_example",
            it_return_year_1_link=[
                "it_return_year_1_link_example",
            ],
            it_return_year_1_link_password="it_return_year_1_link_password_example",
            it_return_year_2_link=[
                "it_return_year_2_link_example",
            ],
            it_return_year_2_link_password="it_return_year_2_link_password_example",
            it_return_year_3_link=[
                "it_return_year_3_link_example",
            ],
            it_return_year_3_link_password="it_return_year_3_link_password_example",
            other_income_assesment_proof_link=[
                "other_income_assesment_proof_link_example",
            ],
            other_income_assesment_proof_link_password="other_income_assesment_proof_link_password_example",
            cam_link=[
                "cam_link_example",
            ],
            cam_link_password="cam_link_password_example",
            cfa_link=[
                "cfa_link_example",
            ],
            cfa_link_password="cfa_link_password_example",
        ),
        abb_emi_ratio=3.14,
        dscr=3.14,
        foir=3.14,
        ltr=3.14,
        insr=3.14,
        eligibility_as_per_insr=3.14,
        eligibility_as_per_foir=3.14,
        eligibility_as_per_ltv=3.14,
        eligibility_loan_amount=3.14,
        fcf=1,
        emi_obligations=1,
        viability_ratio=3.14,
        product_id="product_id_example",
        client_loan_id="client_loan_id_example",
        application_id="application_id_example",
        loan_cycle=1,
        partner_branch_code="partner_branch_code_example",
        partner_branch_name="partner_branch_name_example",
        product_type="product_type_example",
        partner_product_code="partner_product_code_example",
        partner_scheme_code="partner_scheme_code_example",
        category="category_example",
        sub_category="sub_category_example",
        purpose="purpose_example",
        disbursement_type="disbursement_type_example",
        number_of_tranches=1,
        end_borrower_amount=3.14,
        existing_lender_amount=3.14,
        principal_amount=3.14,
        interest_rate=3.14,
        interest_type="interest_type_example",
        tenure=1,
        tenure_frequency="tenure_frequency_example",
        repayment_frequency="repayment_frequency_example",
        number_of_repayments=1,
        first_repayment_date=dateutil_parser('1970-01-01').date(),
        repayment_mode="repayment_mode_example",
        advance_emi=3.14,
        umrn="umrn_example",
        interest_start_date=dateutil_parser('1970-01-01').date(),
        differential_interest=3.14,
        processing_fee=3.14,
        stamp_duty=3.14,
        insurance_charges=3.14,
        documentation_charges=3.14,
        other_charges=3.14,
        loan_plr_type="loan_plr_type_example",
        loan_plr_rate=3.14,
        spread_id="spread_id_example",
        loan_emi=3.14,
        rcu_status="rcu_status_example",
        surrogate="surrogate_example",
        sub_class="sub_class_example",
        weaker_section="weaker_section_example",
        disbursement_accounts=[
            BodyCreateLoanDisbursementAccounts(
                account_type="account_type_example",
                bank_name="bank_name_example",
                bank_account_type="bank_account_type_example",
                account_name="account_name_example",
                date_of_bank_account_opening=dateutil_parser('1970-01-01').date(),
                bank_branch_name="bank_branch_name_example",
                ifsc_code="ifsc_code_example",
                entity_type="entity_type_example",
                account_no="account_no_example",
                amount=3.14,
            ),
        ],
        assets=[
            BodyCreateLoanAssets(
                asset_category="asset_category_example",
                asset_owned_by="asset_owned_by_example",
                relationship_to_the_business="relationship_to_the_business_example",
                asset_value_self_declared="asset_value_self_declared_example",
                asset_market_value="asset_market_value_example",
                ltv_asset_market_value="ltv_asset_market_value_example",
                area_type="area_type_example",
                ltv_asset_value_self_declared=3.14,
                age_of_the_collateral=1,
                mortgage_in_favour_of="mortgage_in_favour_of_example",
                machinery_type="machinery_type_example",
                hypothecation_value=3.14,
                hypothecation_percentage=3.14,
                new_machinery_value=3.14,
                old_machinery_value=3.14,
                new_machinery_ltv=3.14,
                old_machinery_ltv=3.14,
                total_number_of_machines=1,
                total_value_of_machines=3.14,
                manufacturer_name="manufacturer_name_example",
                machinery_hypothecated_to="machinery_hypothecated_to_example",
                property_address="property_address_example",
                property_city="property_city_example",
                property_district="property_district_example",
                property_state="property_state_example",
                property_pincode=1,
            ),
        ],
        references=[
            BodyCreateLoanReferences(
                name="name_example",
                address="address_example",
                pincode="pincode_example",
                phone="phone_example",
            ),
        ],
        insurance_details=[
            BodyCreateLoanInsuranceDetails(
                insurance_type="insurance_type_example",
                insurer_name="insurer_name_example",
                nominee_details="nominee_details_example",
                nominee_date_of_birth=dateutil_parser('1970-01-01').date(),
                relationship="relationship_example",
                premium=3.14,
                insurance_amount=3.14,
                policy_number=1,
            ),
        ],
        psl_flag="psl_flag_example",
        psl_description="psl_description_example",
        psl_code="psl_code_example",
        psl_proof_link=[
            "psl_proof_link_example",
        ],
        psl_proof_link_password="psl_proof_link_password_example",
        tranches=[
            BodyCreateLoanTranches(
                tranche_number=1,
                principal_amount=1,
                differential_interest=1,
                processing_fee=1,
                stamp_duty=1,
                insurance_charges=1,
                documentation_charges=1,
                other_charges=1,
                closing_loan_principal=1,
            ),
        ],
        linked_loan_infos=[
            BodyCreateLoanLinkedLoanInfos(
                linked_loan_id="linked_loan_id_example",
                foreclosure="foreclosure_example",
                principal=3.14,
                interest=3.14,
                other_charges=3.14,
                overdue_charges=3.14,
                penalty_charges=3.14,
                fee_charges=3.14,
                bounce_charges=3.14,
                amount=3.14,
            ),
        ],
        sourcing_detail=BodyCreateLoanSourcingDetail(
            source_code="source_code_example",
            referrer_code="referrer_code_example",
            referrer_group="referrer_group_example",
            referrer_name="referrer_name_example",
            channel_code="channel_code_example",
            dst_code="dst_code_example",
            dsa="dsa_example",
            dse="dse_example",
            relationship_manager="relationship_manager_example",
        ),
        deviation_details=[
            BodyCreateLoanDeviationDetails(
                summary="summary_example",
                desc="desc_example",
                mitigant="mitigant_example",
                level="level_example",
            ),
        ],
    ) # BodyCreateLoan | 

    # example passing only required values which don't have defaults set
    try:
        # #Create Loan
        api_response = api_instance.create_loan(product_id, client_name, body_create_loan)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->create_loan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **body_create_loan** | [**BodyCreateLoan**](BodyCreateLoan.md)|  |

### Return type

[**CreateLoanSuccess**](CreateLoanSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 Created |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**422** | 422 Unprocessable Entity (Client Loan ID Already Taken) |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repayment_schedule**
> CreateRSSuccess create_repayment_schedule(product_id, client_name, loan_id, body_create_repayment_schedule)

#Create Repayment Schedule

Create Repayment Schedule

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>repayment_schedules</td>     <td>array</td>     <td></td>          <td>Refer table RepaymentSchedules for attributes</td>       <td>[{&quot;installment_no&quot;:1,&quot;due_date&quot;:&quot;2021-02-02&quot;,&quot;principal&quot;:10000.0,&quot;interest&quot;:100.0,&quot;amount&quot;:10200.0,&quot;pos&quot;:20000.0,&quot;other_charges&quot;:100.0},{&quot;installment_no&quot;:1,&quot;due_date&quot;:&quot;2021-02-02&quot;,&quot;principal&quot;:10000.0,&quot;interest&quot;:100.0,&quot;amount&quot;:10200.0,&quot;pos&quot;:20000.0,&quot;other_charges&quot;:100.0}]</td>  </tr>    </tbody>       </table>   <h4>RepaymentSchedules</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>installment_no</td>     <td>integer</td>     <td></td>          <td>Installment Number</td>       <td>1</td>  </tr>        <tr>     <td>due_date</td>     <td>string</td>     <td>date</td>          <td>Due Date for the Installment (YYYY-MM-DD)</td>       <td>2021-02-02</td>  </tr>        <tr>     <td>principal</td>     <td>number</td>     <td>float</td>          <td>Principal to be paid in the installment</td>       <td>10000.0</td>  </tr>        <tr>     <td>interest</td>     <td>number</td>     <td>float</td>          <td>Interest to be paid in the installment</td>       <td>100.0</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Total EMI amount</td>       <td>10200.0</td>  </tr>        <tr>     <td>pos</td>     <td>number</td>     <td>float</td>          <td>Closing Principal Outstanding</td>       <td>20000.0</td>  </tr>        <tr>     <td>other_charges</td>     <td>number</td>     <td>float</td>          <td>Other Charges</td>       <td>100.0</td>  </tr>    </tbody>       </table>     #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>201</td>     <td>Created</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters </td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>412</td>     <td>Precondition Failed</td>     <td>Installment(s) already exists / Loan disbursement details not present / Sum of Principal amount in the repayment schedule is not equal to loan's principal amount / Number of installments in the repayment schedule should be equal to tenure or tenure + 1 / First installment date cannot be greater than 60 days from the date of disbursement / First installment due date cannot be before loan disbursement date / Amount is not equal to sum of Principal and Interest / Invalid installment number</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>  </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.create_rs_success import CreateRSSuccess
from credavenue_colending.model.body_create_repayment_schedule import BodyCreateRepaymentSchedule
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_create_repayment_schedule = BodyCreateRepaymentSchedule(
        repayment_schedules=[
            BodyCreateRepaymentScheduleRepaymentSchedules(
                installment_no=1,
                due_date=dateutil_parser('1970-01-01').date(),
                principal=3.14,
                interest=3.14,
                amount=3.14,
                pos=3.14,
                other_charges=3.14,
            ),
        ],
    ) # BodyCreateRepaymentSchedule | 

    # example passing only required values which don't have defaults set
    try:
        # #Create Repayment Schedule
        api_response = api_instance.create_repayment_schedule(product_id, client_name, loan_id, body_create_repayment_schedule)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->create_repayment_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_create_repayment_schedule** | [**BodyCreateRepaymentSchedule**](BodyCreateRepaymentSchedule.md)|  |

### Return type

[**CreateRSSuccess**](CreateRSSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 201 Created |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tranche**
> ResponseCreateTranche create_tranche(loan_id, client_name, body_create_tranche)

#Create Tranche

Create Tranche - This API endpoint can be used to create a tranche.

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>tranche_number</td>     <td>integer</td>     <td></td>          <td>Tranche Number</td>       <td>1</td>  </tr>        <tr>     <td>principal_amount</td>     <td>integer</td>     <td></td>          <td>Principal amount to be disbursed in the tranche</td>       <td>100000</td>  </tr>        <tr>     <td>differential_interest</td>     <td>integer</td>     <td></td>          <td>Broken period interest amount</td>       <td>100</td>  </tr>        <tr>     <td>interest_start_date</td>     <td>string</td>     <td>date</td>          <td>Pre Emi interest due date</td>       <td>2021-01-01</td>  </tr>        <tr>     <td>processing_fee</td>     <td>integer</td>     <td></td>          <td>Processing fee amount (Inckusive of GST)</td>       <td>100</td>  </tr>        <tr>     <td>stamp_duty</td>     <td>integer</td>     <td></td>          <td>Stamp duty amount</td>       <td>100</td>  </tr>        <tr>     <td>insurance_charges</td>     <td>integer</td>     <td></td>          <td>Insurance premium inclusive of GST</td>       <td>100</td>  </tr>        <tr>     <td>documentation_charges</td>     <td>integer</td>     <td></td>          <td>Total documentation charges inclusive of GST</td>       <td>100</td>  </tr>        <tr>     <td>other_charges</td>     <td>integer</td>     <td></td>          <td>Any other charges inclusive of GST</td>       <td>100</td>  </tr>        <tr>     <td>closing_loan_principal</td>     <td>integer</td>     <td></td>          <td>Balance principal amount after this tranche</td>       <td>100000</td>  </tr>        <tr>     <td>tranche_doc_link</td>     <td>string</td>     <td></td>          <td>Link to the corresponding document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>tranche_doc_link_password</td>     <td>string</td>     <td></td>          <td>Link to the corresponding document</td>       <td>12345678</td>  </tr>        <tr>     <td>disbursement_accounts</td>     <td>array</td>     <td></td>          <td>Refer table DisbursementAccounts for attributes</td>       <td>[{&quot;bank_name&quot;:&quot;HDFC&quot;,&quot;bank_account_type&quot;:&quot;savings&quot;,&quot;account_name&quot;:&quot;Arya&quot;,&quot;bank_branch_name&quot;:&quot;Nandanam&quot;,&quot;ifsc_code&quot;:&quot;HDFC000123&quot;,&quot;entity_type&quot;:&quot;dealer&quot;,&quot;account_no&quot;:987656453423,&quot;amount&quot;:1000000},{&quot;bank_name&quot;:&quot;HDFC&quot;,&quot;bank_account_type&quot;:&quot;savings&quot;,&quot;account_name&quot;:&quot;Arya&quot;,&quot;bank_branch_name&quot;:&quot;Nandanam&quot;,&quot;ifsc_code&quot;:&quot;HDFC000123&quot;,&quot;entity_type&quot;:&quot;dealer&quot;,&quot;account_no&quot;:987656453423,&quot;amount&quot;:1000000}]</td>  </tr>        <tr>     <td>loan_data</td>     <td>array</td>     <td></td>          <td>Refer table LoanData for attributes</td>       <td>[{&quot;pan_number&quot;:&quot;POIUY1234H&quot;,&quot;pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_link_password&quot;:&quot;12345678&quot;,&quot;form_60_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;form_60_link_password&quot;:&quot;12345678&quot;,&quot;aadhar_number&quot;:&quot;987612345432&quot;,&quot;aadhar_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number_link_password&quot;:&quot;12345678&quot;,&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voter_id_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voter_id_number_link_password&quot;:&quot;12345678&quot;,&quot;driving_license_number&quot;:&quot;TN0112345&quot;,&quot;driving_license_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_license_number_link_password&quot;:&quot;12345678&quot;,&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_link_password&quot;:&quot;12345678&quot;,&quot;video_image_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_image_link_password&quot;:&quot;12345678&quot;,&quot;video_kyc_detail&quot;:&quot;{&quot;profile_id&quot;:&quot;ABC12345&quot;,&quot;account_id&quot;:&quot;ABC12345&quot;,&quot;key&quot;:&quot;abc@123&quot;}&quot;,&quot;other_kyc_number&quot;:&quot;ABC12345&quot;,&quot;other_kyc_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_kyc_number_link_password&quot;:&quot;12345678&quot;,&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link_password&quot;:&quot;12345678&quot;,&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;,&quot;employer_tier&quot;:&quot;tier_1&quot;,&quot;employment_type&quot;:&quot;salaried&quot;,&quot;employment_details_name&quot;:&quot;Credavenue&quot;,&quot;employment_details_address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;employment_details_years_of_experience&quot;:3.0,&quot;employment_details_designation&quot;:&quot;IT Consultant&quot;,&quot;employement_vintage_current_organisation&quot;:&quot;3&quot;,&quot;payslip_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;payslip_link_password&quot;:&quot;12345678&quot;,&quot;tds_certificate_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;tds_certificate_link_password&quot;:&quot;12345678&quot;},{&quot;pan_number&quot;:&quot;POIUY1234H&quot;,&quot;pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_link_password&quot;:&quot;12345678&quot;,&quot;form_60_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;form_60_link_password&quot;:&quot;12345678&quot;,&quot;aadhar_number&quot;:&quot;987612345432&quot;,&quot;aadhar_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number_link_password&quot;:&quot;12345678&quot;,&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voter_id_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voter_id_number_link_password&quot;:&quot;12345678&quot;,&quot;driving_license_number&quot;:&quot;TN0112345&quot;,&quot;driving_license_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_license_number_link_password&quot;:&quot;12345678&quot;,&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_link_password&quot;:&quot;12345678&quot;,&quot;video_image_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_image_link_password&quot;:&quot;12345678&quot;,&quot;video_kyc_detail&quot;:&quot;{&quot;profile_id&quot;:&quot;ABC12345&quot;,&quot;account_id&quot;:&quot;ABC12345&quot;,&quot;key&quot;:&quot;abc@123&quot;}&quot;,&quot;other_kyc_number&quot;:&quot;ABC12345&quot;,&quot;other_kyc_number_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_kyc_number_link_password&quot;:&quot;12345678&quot;,&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link_password&quot;:&quot;12345678&quot;,&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link_password&quot;:&quot;12345678&quot;,&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link_password&quot;:&quot;12345678&quot;,&quot;employer_tier&quot;:&quot;tier_1&quot;,&quot;employment_type&quot;:&quot;salaried&quot;,&quot;employment_details_name&quot;:&quot;Credavenue&quot;,&quot;employment_details_address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;employment_details_years_of_experience&quot;:3.0,&quot;employment_details_designation&quot;:&quot;IT Consultant&quot;,&quot;employement_vintage_current_organisation&quot;:&quot;3&quot;,&quot;payslip_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;payslip_link_password&quot;:&quot;12345678&quot;,&quot;tds_certificate_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;tds_certificate_link_password&quot;:&quot;12345678&quot;}]</td>  </tr>        <tr>     <td>bureau_report_data</td>     <td>object</td>     <td></td>     <td>Refer table BureauReportData for attributes</td>       <td>{&quot;name_of_bureau&quot;:&quot;cibil&quot;,&quot;bureau_vintage&quot;:3,&quot;bureau_score&quot;:650,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_report_link_password&quot;:&quot;12345678&quot;,&quot;bureau_json_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_json_link_password&quot;:&quot;12345678&quot;,&quot;bureau_json&quot;:[&quot;{}&quot;,&quot;{}&quot;],&quot;commercial_bureau_score&quot;:330,&quot;commercial_bureau_score_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;commercial_bureau_score_link_password&quot;:&quot;12345678&quot;,&quot;partner_score_on_the_customer&quot;:800,&quot;total_existing_obligations&quot;:25000,&quot;credit_card_limit&quot;:30000,&quot;number_of_credit_cards&quot;:3,&quot;number_of_unsecured_loans&quot;:2,&quot;value_of_total_unsecured_loans&quot;:20000.0,&quot;number_of_loans&quot;:2,&quot;value_of_total_loans&quot;:20000.0,&quot;number_of_enquiries_3months&quot;:3,&quot;number_of_enquiries_6months&quot;:3,&quot;number_of_enquiries_12months&quot;:4,&quot;number_of_writeoff_suitfiled_settled_12months&quot;:4,&quot;max_dpd_tradeline_12months&quot;:6,&quot;max_overdue_tradeline&quot;:6,&quot;total_overdue_amount_12months&quot;:10000.0,&quot;loan_amount_settled_12months&quot;:25000.0,&quot;nature_of_loan_settled1&quot;:&quot;settled&quot;,&quot;nature_of_loan_settled2&quot;:&quot;closed&quot;,&quot;total_emi_bounces&quot;:3,&quot;emi_bounces_6months&quot;:3,&quot;emi_bounces_12months&quot;:3}</td>  </tr>        <tr>     <td>client_loan_id</td>     <td>string</td>     <td></td>          <td>Loan ID as per Partner&#39;s LMS</td>       <td>LOAN00001</td>  </tr>        <tr>     <td>business_data</td>     <td>object</td>     <td></td>     <td>Refer table BusinessData for attributes</td>       <td>{&quot;business_pan_number&quot;:&quot;BMMPG9018G&quot;,&quot;business_pan_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_pan_link_password&quot;:&quot;12345678&quot;,&quot;business_rc_number&quot;:&quot;U72200MH2009PLC123456&quot;,&quot;business_rc_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_rc_link_password&quot;:&quot;12345678&quot;,&quot;business_gst_number&quot;:&quot;29ABCDE1234F2Z5&quot;,&quot;business_gst_copy_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_gst_copy_link_password&quot;:&quot;12345678&quot;,&quot;business_udyog_aadhar_number&quot;:&quot;794065346725&quot;,&quot;business_udyog_aadhar_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_udyog_aadhar_link_password&quot;:&quot;12345678&quot;,&quot;business_ssi_number&quot;:&quot;7589297314&quot;,&quot;business_ssi_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_ssi_link_password&quot;:&quot;12345678&quot;,&quot;business_shops_est_number&quot;:&quot;2017086025&quot;,&quot;business_shops_est_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_shops_est_link_password&quot;:&quot;12345678&quot;,&quot;business_factory_regn_number&quot;:&quot;TVEIQ0615232&quot;,&quot;business_factory_regn_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_factory_regn_link_password&quot;:&quot;12345678&quot;,&quot;business_trade_license_number&quot;:&quot;EA131102014709112&quot;,&quot;business_trade_license_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_trade_license_link_password&quot;:&quot;12345678&quot;,&quot;business_place_photo_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_place_photo_link_password&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_continuity_proof_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;business_continuity_proof_link_password&quot;:&quot;12345678&quot;,&quot;other_business_address_proof_number&quot;:&quot;ABC12345&quot;,&quot;other_business_address_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_business_address_proof_link_password&quot;:&quot;12345678&quot;,&quot;no_of_business_authorised_persons&quot;:&quot;3&quot;,&quot;partnership_detail&quot;:&quot;{&quot;partnership_firm_pan&quot;:&quot;BMMPG9018G&quot;,&quot;partnership_pan_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;partnership_pan_link_password&quot;:&quot;12345678&quot;,&quot;partnership_deed_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;partnership_deed_link_password&quot;:&quot;12345678&quot;,&quot;beneficiary_owner_details_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;beneficiary_owner_details_link_password&quot;:&quot;12345678&quot;}&quot;,&quot;private_entity_detail&quot;:&quot;{&quot;cin_number&quot;:&quot;L21091KA2019OPC141331&quot;,&quot;cin_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;cin_link_password&quot;:&quot;12345678&quot;,&quot;moa_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;moa_link_password&quot;:&quot;12345678&quot;,&quot;aoa_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;aoa_link_password&quot;:&quot;12345678&quot;,&quot;board_resoultion_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;board_resoultion_link_password&quot;:&quot;12345678&quot;,&quot;share_holding_pattern_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;share_holding_pattern_link_password&quot;:&quot;12345678&quot;,&quot;other_company_proof&quot;:&quot;ABC12345&quot;,&quot;other_company_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_company_proof_link_password&quot;:&quot;12345678&quot;}&quot;}</td>  </tr>    </tbody>       </table>   <h4>DisbursementAccounts</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>bank_name</td>     <td>string</td>     <td></td>          <td>Name of the bank where disbursement needs to be done</td>       <td>HDFC</td>  </tr>        <tr>     <td>bank_account_type</td>     <td>string</td>     <td></td>          <td>Account type - Savings/Current/Overdraft/CC</td>       <td>savings</td>  </tr>        <tr>     <td>account_name</td>     <td>string</td>     <td></td>          <td>Bank account name where disbursement needs to be done</td>       <td>Arya</td>  </tr>        <tr>     <td>bank_branch_name</td>     <td>string</td>     <td></td>          <td>Bank branch name where disbursement needs to be done</td>       <td>Nandanam</td>  </tr>        <tr>     <td>ifsc_code</td>     <td>string</td>     <td></td>          <td>Bank IFSC wheredisbursement needs to be done</td>       <td>HDFC000123</td>  </tr>        <tr>     <td>entity_type</td>     <td>string</td>     <td></td>          <td>dealer / sub_dealer / originator / existing_lender / end_customer</td>       <td>dealer</td>  </tr>        <tr>     <td>account_no</td>     <td>integer</td>     <td></td>          <td>Account number of bank where disbursement needs to be done</td>       <td>987656453423</td>  </tr>        <tr>     <td>amount</td>     <td>integer</td>     <td></td>          <td>Amount to be transferred to particular Vendor/borrower</td>       <td>1000000</td>  </tr>    </tbody>       </table>   <h4>VideoKycDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>profile_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Profile ID of the case as per the video KYC vendor</td>       <td>ABC12345</td>  </tr>        <tr>     <td>account_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Account ID of the case as per the video KYC vendor</td>       <td>ABC12345</td>  </tr>        <tr>     <td>key</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Key as per the video KYC vendor</td>       <td>abc@123</td>  </tr>    </tbody>       </table>   <h4>LoanData</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>pan_number</td>     <td>string</td>     <td></td>          <td>PAN Number of the Customer (10 digit Alphanumeric)</td>       <td>POIUY1234H</td>  </tr>        <tr>     <td>pan_link</td>     <td>array</td>     <td></td>          <td>PAN Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>pan_link_password</td>     <td>string</td>     <td></td>          <td>PAN Document Link</td>       <td>12345678</td>  </tr>        <tr>     <td>form_60_link</td>     <td>array</td>     <td></td>          <td>Form 60 Doument Link (If applicable)</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>form_60_link_password</td>     <td>string</td>     <td></td>          <td>Form 60 Doument Link Password (If applicable)</td>       <td>12345678</td>  </tr>        <tr>     <td>aadhar_number</td>     <td>string</td>     <td></td>          <td>Aadhar Number of the Customer (12 digits)</td>       <td>987612345432</td>  </tr>        <tr>     <td>aadhar_number_link</td>     <td>array</td>     <td></td>          <td>Aadhar Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aadhar_number_link_password</td>     <td>string</td>     <td></td>          <td>Aadhar Document Link</td>       <td>12345678</td>  </tr>        <tr>     <td>voter_id_number</td>     <td>string</td>     <td></td>          <td>Voter ID Number of the Customer</td>       <td>RTG2291234</td>  </tr>        <tr>     <td>voter_id_number_link</td>     <td>array</td>     <td></td>          <td>Voter Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>voter_id_number_link_password</td>     <td>string</td>     <td></td>          <td>Voter Document Link</td>       <td>12345678</td>  </tr>        <tr>     <td>driving_license_number</td>     <td>string</td>     <td></td>          <td>Driving License Number of the Customer</td>       <td>TN0112345</td>  </tr>        <tr>     <td>driving_license_number_link</td>     <td>array</td>     <td></td>          <td>Driving License Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>driving_license_number_link_password</td>     <td>string</td>     <td></td>          <td>Driving License Document Link</td>       <td>12345678</td>  </tr>        <tr>     <td>passport_number</td>     <td>string</td>     <td></td>          <td>Passport Number of the Customer</td>       <td>L4018345</td>  </tr>        <tr>     <td>passport_link</td>     <td>array</td>     <td></td>          <td>Passport Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>passport_link_password</td>     <td>string</td>     <td></td>          <td>Passport Document Link</td>       <td>12345678</td>  </tr>        <tr>     <td>video_image_link</td>     <td>array</td>     <td></td>          <td>Video Image of the Applicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_image_link_password</td>     <td>string</td>     <td></td>          <td>Video Image of the Applicant</td>       <td>12345678</td>  </tr>        <tr>     <td>video_kyc_detail</td>     <td>object</td>     <td></td>      <td>Refer table VideoKycDetail for attributes</td>       <td>{&quot;profile_id&quot;:&quot;ABC12345&quot;,&quot;account_id&quot;:&quot;ABC12345&quot;,&quot;key&quot;:&quot;abc@123&quot;}</td>  </tr>        <tr>     <td>other_kyc_number</td>     <td>string</td>     <td></td>          <td>KYC Number of the Customer</td>       <td>ABC12345</td>  </tr>        <tr>     <td>other_kyc_number_link</td>     <td>array</td>     <td></td>          <td>KYC Image of the Customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_kyc_number_link_password</td>     <td>string</td>     <td></td>          <td>KYC Image of the Customer</td>       <td>12345678</td>  </tr>        <tr>     <td>rent_agreement_link</td>     <td>array</td>     <td></td>          <td>Rent Agreement Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>rent_agreement_link_password</td>     <td>string</td>     <td></td>          <td>Rent Agreement Document Link</td>       <td>12345678</td>  </tr>        <tr>     <td>utility_bills_link</td>     <td>array</td>     <td></td>          <td>Utility Bills Copies (If any)</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>utility_bills_link_password</td>     <td>string</td>     <td></td>          <td>Utility Bills Copies (If any)</td>       <td>12345678</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo Image of the Customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link_password</td>     <td>string</td>     <td></td>          <td>Photo Image of the Customer</td>       <td>12345678</td>  </tr>        <tr>     <td>employer_tier</td>     <td>string</td>     <td></td>          <td>tier_1, tier_2 etc. for  the employer</td>       <td>tier_1</td>  </tr>        <tr>     <td>employment_type</td>     <td>string</td>     <td></td>          <td>Salaried / Self-Employed</td>       <td>salaried</td>  </tr>        <tr>     <td>employment_details_name</td>     <td>string</td>     <td></td>          <td>Employer Name</td>       <td>Credavenue</td>  </tr>        <tr>     <td>employment_details_address</td>     <td>string</td>     <td></td>          <td>Office Address</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>employment_details_years_of_experience</td>     <td>number</td>     <td>float</td>          <td>Applicant&#39;s years of experience in the current organization</td>       <td>3.0</td>  </tr>        <tr>     <td>employment_details_designation</td>     <td>string</td>     <td></td>          <td>Applicant&#39;s Current Designation</td>       <td>IT Consultant</td>  </tr>        <tr>     <td>employement_vintage_current_organisation</td>     <td>string</td>     <td></td>          <td>Vintage</td>       <td>3</td>  </tr>        <tr>     <td>payslip_link</td>     <td>array</td>     <td></td>          <td>Last 3 Months Payslips</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>payslip_link_password</td>     <td>string</td>     <td></td>          <td>Last 3 Months Payslips</td>       <td>12345678</td>  </tr>        <tr>     <td>tds_certificate_link</td>     <td>array</td>     <td></td>          <td>Last 3 Years TDS Certificate</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>tds_certificate_link_password</td>     <td>string</td>     <td></td>          <td>Last 3 Years TDS Certificate</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>BureauJson</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>  </tbody>       </table>   <h4>BureauReportData</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>name_of_bureau</td>     <td>string</td>     <td></td>          <td>Cibil / Experian / Himark</td>       <td>cibil</td>  </tr>        <tr>     <td>bureau_vintage</td>     <td>integer</td>     <td></td>          <td>Vintage in the bureau. Number of years from the first trade line</td>       <td>3</td>  </tr>        <tr>     <td>bureau_score</td>     <td>integer</td>     <td></td>          <td>Bureau Score</td>       <td>650</td>  </tr>        <tr>     <td>bureau_report_link</td>     <td>array</td>     <td></td>          <td>Document of the bureau</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_report_link_password</td>     <td>string</td>     <td></td>          <td>Document of the bureau - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>bureau_json_link</td>     <td>array</td>     <td></td>          <td>Bureau Json placed in a link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_json_link_password</td>     <td>string</td>     <td></td>          <td>Bureau Json placed in a link - Password</td>       <td>12345678</td>  </tr>        <tr>     <td>bureau_json</td>     <td>array</td>     <td></td>          <td>Refer table BureauJson for attributes</td>       <td>[{},{}]</td>  </tr>        <tr>     <td>commercial_bureau_score</td>     <td>integer</td>     <td></td>          <td>CRIF score</td>       <td>330</td>  </tr>        <tr>     <td>commercial_bureau_score_link</td>     <td>array</td>     <td></td>          <td>Commercial Bureau Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>commercial_bureau_score_link_password</td>     <td>string</td>     <td></td>          <td>Commercial Bureau Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>partner_score_on_the_customer</td>     <td>integer</td>     <td></td>          <td>Score Captured by the Partner</td>       <td>800</td>  </tr>        <tr>     <td>total_existing_obligations</td>     <td>integer</td>     <td></td>          <td>Total Existing Obligations basis the Bureau Report</td>       <td>25000</td>  </tr>        <tr>     <td>credit_card_limit</td>     <td>integer</td>     <td></td>          <td>Total Credit Card Limit basis the Bureau Report</td>       <td>30000</td>  </tr>        <tr>     <td>number_of_credit_cards</td>     <td>integer</td>     <td></td>          <td>Total Number of Credit Cards per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_unsecured_loans</td>     <td>integer</td>     <td></td>          <td>Total Number of Unsecured Loans per Bureau Report</td>       <td>2</td>  </tr>        <tr>     <td>value_of_total_unsecured_loans</td>     <td>number</td>     <td>float</td>          <td>Total value of unsecured loans</td>       <td>20000.0</td>  </tr>        <tr>     <td>number_of_loans</td>     <td>integer</td>     <td></td>          <td>Total Number of Loans per Bureau Report</td>       <td>2</td>  </tr>        <tr>     <td>value_of_total_loans</td>     <td>number</td>     <td>float</td>          <td>Total value of loans</td>       <td>20000.0</td>  </tr>        <tr>     <td>number_of_enquiries_3months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 3 Months per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_enquiries_6months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 6 Months per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_enquiries_12months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 12 Months per Bureau Report</td>       <td>4</td>  </tr>        <tr>     <td>number_of_writeoff_suitfiled_settled_12months</td>     <td>integer</td>     <td></td>          <td>Number of Writeoff Suitfiled Settled in the Last 12 Months</td>       <td>4</td>  </tr>        <tr>     <td>max_dpd_tradeline_12months</td>     <td>integer</td>     <td></td>          <td>Maximum DPD Tradeline in the Last 12 Months</td>       <td>6</td>  </tr>        <tr>     <td>max_overdue_tradeline</td>     <td>integer</td>     <td></td>          <td>Maximum Overdue Tradeline</td>       <td>6</td>  </tr>        <tr>     <td>total_overdue_amount_12months</td>     <td>number</td>     <td>float</td>          <td>Total Overdue Amount in the Last 12 Months</td>       <td>10000.0</td>  </tr>        <tr>     <td>loan_amount_settled_12months</td>     <td>number</td>     <td>float</td>          <td>Loan Amount Settled in the Last 12 Months</td>       <td>25000.0</td>  </tr>        <tr>     <td>nature_of_loan_settled1</td>     <td>string</td>     <td></td>          <td>The nature of past loan settlement if any (Loan 1) - Settled/ Closed/ Written-off</td>       <td>settled</td>  </tr>        <tr>     <td>nature_of_loan_settled2</td>     <td>string</td>     <td></td>          <td>The nature of past loan settlement if any (Loan 2) - Settled/ Closed/ Written-off</td>       <td>closed</td>  </tr>        <tr>     <td>total_emi_bounces</td>     <td>integer</td>     <td></td>          <td>Total EMI Bounces</td>       <td>3</td>  </tr>        <tr>     <td>emi_bounces_6months</td>     <td>integer</td>     <td></td>          <td>EMI Bounces in the Last 6 Months</td>       <td>3</td>  </tr>        <tr>     <td>emi_bounces_12months</td>     <td>integer</td>     <td></td>          <td>EMI Bounces in the Last 12 Months</td>       <td>3</td>  </tr>    </tbody>       </table>   <h4>PartnershipDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>partnership_firm_pan</td>     <td>string</td>     <td></td>          <td>PAN number of partnership</td>       <td>BMMPG9018G</td>  </tr>        <tr>     <td>partnership_pan_link</td>     <td>string</td>     <td></td>          <td>PAN image of partnership</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>partnership_pan_link_password</td>     <td>string</td>     <td></td>          <td>PAN image password of partnership</td>       <td>12345678</td>  </tr>        <tr>     <td>partnership_deed_link</td>     <td>string</td>     <td></td>          <td>Partnership deed image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>partnership_deed_link_password</td>     <td>string</td>     <td></td>          <td>Partnership deed image password</td>       <td>12345678</td>  </tr>        <tr>     <td>beneficiary_owner_details_link</td>     <td>string</td>     <td></td>          <td>Shareholding pattern of the firm</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>beneficiary_owner_details_link_password</td>     <td>string</td>     <td></td>          <td>Shareholding pattern of the firm - password</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>PrivateEntityDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>cin_number</td>     <td>string</td>     <td></td>          <td>CIN number in case of a company</td>       <td>L21091KA2019OPC141331</td>  </tr>        <tr>     <td>cin_link</td>     <td>string</td>     <td></td>          <td>CIN image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>cin_link_password</td>     <td>string</td>     <td></td>          <td>CIN image password</td>       <td>12345678</td>  </tr>        <tr>     <td>moa_link</td>     <td>string</td>     <td></td>          <td>MOA image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>moa_link_password</td>     <td>string</td>     <td></td>          <td>MOA image password</td>       <td>12345678</td>  </tr>        <tr>     <td>aoa_link</td>     <td>string</td>     <td></td>          <td>AOA image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>aoa_link_password</td>     <td>string</td>     <td></td>          <td>AOA image password</td>       <td>12345678</td>  </tr>        <tr>     <td>board_resoultion_link</td>     <td>string</td>     <td></td>          <td>Board resolution image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>board_resoultion_link_password</td>     <td>string</td>     <td></td>          <td>Board resolution image password</td>       <td>12345678</td>  </tr>        <tr>     <td>share_holding_pattern_link</td>     <td>string</td>     <td></td>          <td>Shareholding pattern image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>share_holding_pattern_link_password</td>     <td>string</td>     <td></td>          <td>Shareholding pattern image password</td>       <td>12345678</td>  </tr>        <tr>     <td>other_company_proof</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>ABC12345</td>  </tr>        <tr>     <td>other_company_proof_link</td>     <td>array</td>     <td></td>          <td>Image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_company_proof_link_password</td>     <td>string</td>     <td></td>          <td>Image password</td>       <td>12345678</td>  </tr>    </tbody>       </table>   <h4>BusinessData</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>business_pan_number</td>     <td>string</td>     <td></td>          <td>PAN number of business</td>       <td>BMMPG9018G</td>  </tr>        <tr>     <td>business_pan_link</td>     <td>string</td>     <td></td>          <td>PAN image of business</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_pan_link_password</td>     <td>string</td>     <td></td>          <td>PAN image password of business</td>       <td>12345678</td>  </tr>        <tr>     <td>business_rc_number</td>     <td>string</td>     <td></td>          <td>Registration number of the business</td>       <td>U72200MH2009PLC123456</td>  </tr>        <tr>     <td>business_rc_link</td>     <td>string</td>     <td></td>          <td>Image of the RC</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_rc_link_password</td>     <td>string</td>     <td></td>          <td>Image password of the RC</td>       <td>12345678</td>  </tr>        <tr>     <td>business_gst_number</td>     <td>string</td>     <td></td>          <td>Business GST number</td>       <td>29ABCDE1234F2Z5</td>  </tr>        <tr>     <td>business_gst_copy_link</td>     <td>string</td>     <td></td>          <td>Business GST image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_gst_copy_link_password</td>     <td>string</td>     <td></td>          <td>Business GST image password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_udyog_aadhar_number</td>     <td>string</td>     <td></td>          <td>Business Udyog Aadhar Number</td>       <td>794065346725</td>  </tr>        <tr>     <td>business_udyog_aadhar_link</td>     <td>string</td>     <td></td>          <td>Business Udyog Aadhar Document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_udyog_aadhar_link_password</td>     <td>string</td>     <td></td>          <td>Business Udyog Aadhar Document Password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_ssi_number</td>     <td>string</td>     <td></td>          <td>Small scall industries registration number</td>       <td>7589297314</td>  </tr>        <tr>     <td>business_ssi_link</td>     <td>string</td>     <td></td>          <td>Small scall industries registration document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_ssi_link_password</td>     <td>string</td>     <td></td>          <td>Small scall industries registration document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_shops_est_number</td>     <td>string</td>     <td></td>          <td>Shop establishment number</td>       <td>2017086025</td>  </tr>        <tr>     <td>business_shops_est_link</td>     <td>string</td>     <td></td>          <td>Shop establishment document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_shops_est_link_password</td>     <td>string</td>     <td></td>          <td>Shop establishment document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_factory_regn_number</td>     <td>string</td>     <td></td>          <td>Factory riegistration number</td>       <td>TVEIQ0615232</td>  </tr>        <tr>     <td>business_factory_regn_link</td>     <td>string</td>     <td></td>          <td>Factory riegistration document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_factory_regn_link_password</td>     <td>string</td>     <td></td>          <td>Factory riegistration document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_trade_license_number</td>     <td>string</td>     <td></td>          <td>Trade license number</td>       <td>EA131102014709112</td>  </tr>        <tr>     <td>business_trade_license_link</td>     <td>string</td>     <td></td>          <td>Trade license document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_trade_license_link_password</td>     <td>string</td>     <td></td>          <td>Trade license document password</td>       <td>12345678</td>  </tr>        <tr>     <td>business_place_photo_link</td>     <td>string</td>     <td></td>          <td>Business place photo image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_place_photo_link_password</td>     <td>string</td>     <td></td>          <td>Business place photo image</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_continuity_proof_link</td>     <td>string</td>     <td></td>          <td>Business continuity proof document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>business_continuity_proof_link_password</td>     <td>string</td>     <td></td>          <td>Business continuity proof document password</td>       <td>12345678</td>  </tr>        <tr>     <td>other_business_address_proof_number</td>     <td>string</td>     <td></td>          <td>any other adddress proof number</td>       <td>ABC12345</td>  </tr>        <tr>     <td>other_business_address_proof_link</td>     <td>array</td>     <td></td>          <td>any other adddress proof image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_business_address_proof_link_password</td>     <td>string</td>     <td></td>          <td>any other adddress proof image password</td>       <td>12345678</td>  </tr>        <tr>     <td>no_of_business_authorised_persons</td>     <td>string</td>     <td></td>          <td>Number of authorized person for business</td>       <td>3</td>  </tr>        <tr>     <td>partnership_detail</td>     <td>object</td>     <td></td>     <td>Refer table PartnershipDetail for attributes</td>       <td>{&quot;partnership_firm_pan&quot;:&quot;BMMPG9018G&quot;,&quot;partnership_pan_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;partnership_pan_link_password&quot;:&quot;12345678&quot;,&quot;partnership_deed_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;partnership_deed_link_password&quot;:&quot;12345678&quot;,&quot;beneficiary_owner_details_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;beneficiary_owner_details_link_password&quot;:&quot;12345678&quot;}</td>  </tr>        <tr>     <td>private_entity_detail</td>     <td>object</td>           <td>Refer table PrivateEntityDetail for attributes</td>       <td>{&quot;cin_number&quot;:&quot;L21091KA2019OPC141331&quot;,&quot;cin_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;cin_link_password&quot;:&quot;12345678&quot;,&quot;moa_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;moa_link_password&quot;:&quot;12345678&quot;,&quot;aoa_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;aoa_link_password&quot;:&quot;12345678&quot;,&quot;board_resoultion_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;board_resoultion_link_password&quot;:&quot;12345678&quot;,&quot;share_holding_pattern_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;share_holding_pattern_link_password&quot;:&quot;12345678&quot;,&quot;other_company_proof&quot;:&quot;ABC12345&quot;,&quot;other_company_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_company_proof_link_password&quot;:&quot;12345678&quot;}</td>  </tr>    </tbody>       </table>     #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>201</td>     <td>Created</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters</td>   </tr>    </tbody>   <tbody>      <tr>     <td>422</td>     <td>Unprocessable Entity</td>     <td>Tranche Number Already Taken/ Loan Not Found/ Document not found/accessible</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.response_create_tranche import ResponseCreateTranche
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.body_create_tranche import BodyCreateTranche
from credavenue_colending.model.error422_create_tranche import Error422CreateTranche
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    client_name = "allcloud" # str | Name of the client
    body_create_tranche = BodyCreateTranche(
        tranche_number=1,
        principal_amount=1,
        differential_interest=1,
        interest_start_date=dateutil_parser('1970-01-01').date(),
        processing_fee=1,
        stamp_duty=1,
        insurance_charges=1,
        documentation_charges=1,
        other_charges=1,
        closing_loan_principal=1,
        tranche_doc_link="tranche_doc_link_example",
        tranche_doc_link_password="tranche_doc_link_password_example",
        disbursement_accounts=[
            ResponseCreateTrancheDisbursementAccounts(
                bank_name="bank_name_example",
                bank_account_type="bank_account_type_example",
                account_name="account_name_example",
                bank_branch_name="bank_branch_name_example",
                ifsc_code="ifsc_code_example",
                entity_type="entity_type_example",
                account_no=1,
                amount=1,
            ),
        ],
        loan_data=[
            ResponseCreateTrancheLoanData(
                pan_number="pan_number_example",
                pan_link=[
                    "pan_link_example",
                ],
                pan_link_password="pan_link_password_example",
                form_60_link=[
                    "form_60_link_example",
                ],
                form_60_link_password="form_60_link_password_example",
                aadhar_number="aadhar_number_example",
                aadhar_number_link=[
                    "aadhar_number_link_example",
                ],
                aadhar_number_link_password="aadhar_number_link_password_example",
                voter_id_number="voter_id_number_example",
                voter_id_number_link=[
                    "voter_id_number_link_example",
                ],
                voter_id_number_link_password="voter_id_number_link_password_example",
                driving_license_number="driving_license_number_example",
                driving_license_number_link=[
                    "driving_license_number_link_example",
                ],
                driving_license_number_link_password="driving_license_number_link_password_example",
                passport_number="passport_number_example",
                passport_link=[
                    "passport_link_example",
                ],
                passport_link_password="passport_link_password_example",
                video_image_link=[
                    "video_image_link_example",
                ],
                video_image_link_password="video_image_link_password_example",
                video_kyc_detail=BodyUpdatePostDisbursementVideoKycDetail(
                    profile_id="profile_id_example",
                    account_id="account_id_example",
                    key="key_example",
                ),
                other_kyc_number="other_kyc_number_example",
                other_kyc_number_link=[
                    "other_kyc_number_link_example",
                ],
                other_kyc_number_link_password="other_kyc_number_link_password_example",
                rent_agreement_link=[
                    "rent_agreement_link_example",
                ],
                rent_agreement_link_password="rent_agreement_link_password_example",
                utility_bills_link=[
                    "utility_bills_link_example",
                ],
                utility_bills_link_password="utility_bills_link_password_example",
                photo_link=[
                    "photo_link_example",
                ],
                photo_link_password="photo_link_password_example",
                employer_tier="employer_tier_example",
                employment_type="employment_type_example",
                employment_details_name="employment_details_name_example",
                employment_details_address="employment_details_address_example",
                employment_details_years_of_experience=3.14,
                employment_details_designation="employment_details_designation_example",
                employement_vintage_current_organisation="employement_vintage_current_organisation_example",
                payslip_link=[
                    "payslip_link_example",
                ],
                payslip_link_password="payslip_link_password_example",
                tds_certificate_link=[
                    "tds_certificate_link_example",
                ],
                tds_certificate_link_password="tds_certificate_link_password_example",
            ),
        ],
        bureau_report_data=ResponseCreateTrancheBureauReportData(
            name_of_bureau="name_of_bureau_example",
            bureau_vintage=1,
            bureau_score=1,
            bureau_report_link=[
                "bureau_report_link_example",
            ],
            bureau_report_link_password="bureau_report_link_password_example",
            bureau_json_link=[
                "bureau_json_link_example",
            ],
            bureau_json_link_password="bureau_json_link_password_example",
            bureau_json=[
                {},
            ],
            commercial_bureau_score=1,
            commercial_bureau_score_link=[
                "commercial_bureau_score_link_example",
            ],
            commercial_bureau_score_link_password="commercial_bureau_score_link_password_example",
            partner_score_on_the_customer=1,
            total_existing_obligations=1,
            credit_card_limit=1,
            number_of_credit_cards=1,
            number_of_unsecured_loans=1,
            value_of_total_unsecured_loans=3.14,
            number_of_loans=1,
            value_of_total_loans=3.14,
            number_of_enquiries_3months=1,
            number_of_enquiries_6months=1,
            number_of_enquiries_12months=1,
            number_of_writeoff_suitfiled_settled_12months=1,
            max_dpd_tradeline_12months=1,
            max_overdue_tradeline=1,
            total_overdue_amount_12months=3.14,
            loan_amount_settled_12months=3.14,
            nature_of_loan_settled1="nature_of_loan_settled1_example",
            nature_of_loan_settled2="nature_of_loan_settled2_example",
            total_emi_bounces=1,
            emi_bounces_6months=1,
            emi_bounces_12months=1,
        ),
        client_loan_id="client_loan_id_example",
        business_data=ResponseCreateTrancheBusinessData(
            business_pan_number="business_pan_number_example",
            business_pan_link="business_pan_link_example",
            business_pan_link_password="business_pan_link_password_example",
            business_rc_number="business_rc_number_example",
            business_rc_link="business_rc_link_example",
            business_rc_link_password="business_rc_link_password_example",
            business_gst_number="business_gst_number_example",
            business_gst_copy_link="business_gst_copy_link_example",
            business_gst_copy_link_password="business_gst_copy_link_password_example",
            business_udyog_aadhar_number="business_udyog_aadhar_number_example",
            business_udyog_aadhar_link="business_udyog_aadhar_link_example",
            business_udyog_aadhar_link_password="business_udyog_aadhar_link_password_example",
            business_ssi_number="business_ssi_number_example",
            business_ssi_link="business_ssi_link_example",
            business_ssi_link_password="business_ssi_link_password_example",
            business_shops_est_number="business_shops_est_number_example",
            business_shops_est_link="business_shops_est_link_example",
            business_shops_est_link_password="business_shops_est_link_password_example",
            business_factory_regn_number="business_factory_regn_number_example",
            business_factory_regn_link="business_factory_regn_link_example",
            business_factory_regn_link_password="business_factory_regn_link_password_example",
            business_trade_license_number="business_trade_license_number_example",
            business_trade_license_link="business_trade_license_link_example",
            business_trade_license_link_password="business_trade_license_link_password_example",
            business_place_photo_link="business_place_photo_link_example",
            business_place_photo_link_password="business_place_photo_link_password_example",
            business_continuity_proof_link="business_continuity_proof_link_example",
            business_continuity_proof_link_password="business_continuity_proof_link_password_example",
            other_business_address_proof_number="other_business_address_proof_number_example",
            other_business_address_proof_link=[
                "other_business_address_proof_link_example",
            ],
            other_business_address_proof_link_password="other_business_address_proof_link_password_example",
            no_of_business_authorised_persons="no_of_business_authorised_persons_example",
            partnership_detail=ResponseCreateTrancheBusinessDataPartnershipDetail(
                partnership_firm_pan="partnership_firm_pan_example",
                partnership_pan_link="partnership_pan_link_example",
                partnership_pan_link_password="partnership_pan_link_password_example",
                partnership_deed_link="partnership_deed_link_example",
                partnership_deed_link_password="partnership_deed_link_password_example",
                beneficiary_owner_details_link="beneficiary_owner_details_link_example",
                beneficiary_owner_details_link_password="beneficiary_owner_details_link_password_example",
            ),
            private_entity_detail=ResponseCreateTrancheBusinessDataPrivateEntityDetail(
                cin_number="cin_number_example",
                cin_link="cin_link_example",
                cin_link_password="cin_link_password_example",
                moa_link="moa_link_example",
                moa_link_password="moa_link_password_example",
                aoa_link="aoa_link_example",
                aoa_link_password="aoa_link_password_example",
                board_resoultion_link="board_resoultion_link_example",
                board_resoultion_link_password="board_resoultion_link_password_example",
                share_holding_pattern_link="share_holding_pattern_link_example",
                share_holding_pattern_link_password="share_holding_pattern_link_password_example",
                other_company_proof="other_company_proof_example",
                other_company_proof_link=[
                    "other_company_proof_link_example",
                ],
                other_company_proof_link_password="other_company_proof_link_password_example",
            ),
        ),
    ) # BodyCreateTranche | 

    # example passing only required values which don't have defaults set
    try:
        # #Create Tranche
        api_response = api_instance.create_tranche(loan_id, client_name, body_create_tranche)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->create_tranche: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **client_name** | **str**| Name of the client |
 **body_create_tranche** | [**BodyCreateTranche**](BodyCreateTranche.md)|  |

### Return type

[**ResponseCreateTranche**](ResponseCreateTranche.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**422** | 422 Unprocessable Entity (Tranche Number Already Taken) |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disburse_loan**
> AgreementSignedSuccess disburse_loan(product_id, client_name, loan_id, body_disburse_loan)

#Disburse Loan

Disburse Loan API - This endpoint can be used to disburse the loan.

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>first_repayment_date</td>     <td>string</td>     <td>date</td>          <td>First repayment date as per repayment schedule</td>       <td>2021-02-02</td>  </tr>        <tr>     <td>disbursement_date</td>     <td>string</td>     <td>date</td>          <td>Disbursement date to the end customer</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>instrument_number</td>     <td>string</td>     <td></td>          <td>UTR / Cheque Number</td>       <td>UTR123456</td>  </tr>        <tr>     <td>instrument_type</td>     <td>string</td>     <td></td>          <td>RTGS / NEFT / UPI / Cheque</td>       <td>NEFT</td>  </tr>        <tr>     <td>penny_test_status</td>     <td>boolean</td>     <td>boolean</td>          <td>Penny Test Status</td>       <td>true</td>  </tr>        <tr>     <td>penny_test_report_link</td>     <td>array</td>     <td></td>          <td>Penny Test Status Report Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>penny_test_report_link_password</td>     <td>string</td>     <td></td>          <td>Penny Test Status Report Link Password</td>       <td>12345678</td>  </tr>        <tr>     <td>disbursement_accounts</td>     <td>array</td>     <td></td>          <td>Refer table DisbursementAccounts for attributes</td>       <td>[{&quot;account_no&quot;:&quot;42710779755&quot;,&quot;disbursement_date&quot;:&quot;2021-01-02&quot;,&quot;disbursed_amount&quot;:100000.0,&quot;instrument_number&quot;:&quot;UTR123456&quot;,&quot;instrument_type&quot;:&quot;NEFT&quot;},{&quot;account_no&quot;:&quot;42710779755&quot;,&quot;disbursement_date&quot;:&quot;2021-01-02&quot;,&quot;disbursed_amount&quot;:100000.0,&quot;instrument_number&quot;:&quot;UTR123456&quot;,&quot;instrument_type&quot;:&quot;NEFT&quot;}]</td>  </tr>    </tbody>       </table>   <h4>DisbursementAccounts</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>account_no</td>     <td>string</td>     <td></td>          <td>Account number of the bank where disbursement needs to be done</td>       <td>42710779755</td>  </tr>        <tr>     <td>disbursement_date</td>     <td>string</td>     <td>date</td>          <td>Disbursement date to the end customer</td>       <td>2021-01-02</td>  </tr>        <tr>     <td>disbursed_amount</td>     <td>number</td>     <td>float</td>          <td>Disbursed Amount</td>       <td>100000.0</td>  </tr>        <tr>     <td>instrument_number</td>     <td>string</td>     <td></td>          <td>UTR / Cheque Number</td>       <td>UTR123456</td>  </tr>        <tr>     <td>instrument_type</td>     <td>string</td>     <td></td>          <td>RTGS / NEFT / UPI / Cheque</td>       <td>NEFT</td>  </tr>    </tbody>       </table>     #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>
### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.agreement_signed_success import AgreementSignedSuccess
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.body_disburse_loan import BodyDisburseLoan
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_disburse_loan = BodyDisburseLoan(
        first_repayment_date=dateutil_parser('1970-01-01').date(),
        disbursement_date=dateutil_parser('1970-01-01').date(),
        instrument_number="instrument_number_example",
        instrument_type="instrument_type_example",
        penny_test_status=True,
        penny_test_report_link=[
            "penny_test_report_link_example",
        ],
        penny_test_report_link_password="penny_test_report_link_password_example",
        disbursement_accounts=[
            BodyDisburseLoanDisbursementAccounts(
                account_no="account_no_example",
                disbursement_date=dateutil_parser('1970-01-01').date(),
                disbursed_amount=3.14,
                instrument_number="instrument_number_example",
                instrument_type="instrument_type_example",
            ),
        ],
    ) # BodyDisburseLoan | 

    # example passing only required values which don't have defaults set
    try:
        # #Disburse Loan
        api_response = api_instance.disburse_loan(product_id, client_name, loan_id, body_disburse_loan)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->disburse_loan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_disburse_loan** | [**BodyDisburseLoan**](BodyDisburseLoan.md)|  |

### Return type

[**AgreementSignedSuccess**](AgreementSignedSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_details**
> GetPaymentSuccess get_collection_details(product_id, client_name, loan_id)

Get Collection Details

#Get Collection Details

Get Collection Details  This API endpoint can be used to get the Payment details.  Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>200</td>     <td>OK</td>     <td>Success</td>   </tr>    </tbody>     <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.get_payment_success import GetPaymentSuccess
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation

    # example passing only required values which don't have defaults set
    try:
        # Get Collection Details
        api_response = api_instance.get_collection_details(product_id, client_name, loan_id)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->get_collection_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |

### Return type

[**GetPaymentSuccess**](GetPaymentSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interest_accrual**
> AgreementSignedSuccess get_interest_accrual(product_id, client_name, loan_id, file_id)

#Get Interest Accrual

Get Interest Accrual API

Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.agreement_signed_success import AgreementSignedSuccess
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    file_id = "1" # str | File ID returned in the response of upload interest accrual

    # example passing only required values which don't have defaults set
    try:
        # #Get Interest Accrual
        api_response = api_instance.get_interest_accrual(product_id, client_name, loan_id, file_id)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->get_interest_accrual: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **file_id** | **str**| File ID returned in the response of upload interest accrual |

### Return type

[**AgreementSignedSuccess**](AgreementSignedSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_details**
> BodyGetLoanDetails get_loan_details(product_id, client_name, loan_id)

#Get Loan Details

This API endpoint can be used to get the loan details. The possible loan status values are :

Loan Status</h4>  <table>   <thead>     <tr>       <th>State</th>       <th>Description</th>   </tr>   </thead>   <tbody>      <tr>     <td>New</td>     <td>When the loan is created</td>    </tr>    </tbody>    <tbody>      <tr>     <td>Approved</td>     <td>When the loan is approved by the investor</td>   </tr>    </tbody>   <tbody>      <tr>     <td>Rejected</td>     <td>When the loan is rejected by the investor</td>    </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>agreement_signed</td>     <td>When end borrower agreement/EKYC is signed/collected</td>     </tr>    </tbody>  <tbody>      <tr>     <td>disbursement_ready</td>     <td>When investor is ready to disburse the funds</td>     </tr>    </tbody>  <tbody>      <tr>     <td>dropped</td>     <td>When the loan gets rejected by the investor at agreement signed state</td>     </tr>    </tbody>  <tbody>      <tr>     <td>disbursed</td>     <td>When the loan moves to the disbursed state by the investor from agreement signed state </td>     </tr>    </tbody>  <tbody>      <tr>     <td>matured</td>     <td>After closure of all installments, the loan moves to the matured state</td>     </tr>    </tbody>   </table>    # Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>200</td>     <td>OK</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>    <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.body_get_loan_details import BodyGetLoanDetails
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation

    # example passing only required values which don't have defaults set
    try:
        # #Get Loan Details
        api_response = api_instance.get_loan_details(product_id, client_name, loan_id)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->get_loan_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |

### Return type

[**BodyGetLoanDetails**](BodyGetLoanDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repayment_schedule_details**
> GetRSSuccess get_repayment_schedule_details(product_id, client_name, loan_id)

#Get Repayment Schedule Details

Get RS Details  This API endpoint can be used to get the repayment schedule details of the loan.

Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>200</td>     <td>OK</td>     <td>Success</td>   </tr>    </tbody>     <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.get_rs_success import GetRSSuccess
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation

    # example passing only required values which don't have defaults set
    try:
        # #Get Repayment Schedule Details
        api_response = api_instance.get_repayment_schedule_details(product_id, client_name, loan_id)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->get_repayment_schedule_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |

### Return type

[**GetRSSuccess**](GetRSSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tranche_details**
> get_tranche_details(product_id, client_name, loan_id, id)

#Get Tranche Details

Get Tranche Details - This API endpoint can be used to get the tranche details of loan.

Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>200</td>     <td>OK</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan not found</td>   </tr>    </tbody>   <tbody>   </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    id = 1 # float | Tranche Number of Loan

    # example passing only required values which don't have defaults set
    try:
        # #Get Tranche Details
        api_instance.get_tranche_details(product_id, client_name, loan_id, id)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->get_tranche_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **id** | **float**| Tranche Number of Loan |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_review**
> PropertyReviewSuccess property_review(product_id, client_name, loan_id, body_property_review)

#Property Review

#Property Review

Property Review API - This endpoint is used for SME Secured to share the Property details or documents after the loan is credit approved by lender.   **Expected Loan Status: "credit_approved"**

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>legal_report_link</td>     <td>array</td>     <td></td>          <td>LEGAL REPORT LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>validation_report_link</td>     <td>array</td>     <td></td>          <td>VALUATION REPORT LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>collateral_photo_link</td>     <td>array</td>     <td></td>          <td>COLLATERAL PHOTO LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>field_verification_report_link</td>     <td>array</td>     <td></td>          <td>FIELD VERIFICATION REPORT LINK</td>       <td>[&quot;12345678&quot;, &quot;12345678&quot;]</td>  </tr>        <tr>     <td>tele_verification_report_link</td>     <td>array</td>     <td></td>          <td>TELE VERIFICATION REPORT LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>property_inspection_report_link</td>     <td>array</td>     <td></td>          <td>PROPERTY INSPECTION REPORT LINK</td>       <td>[&quot;12345678&quot;, &quot;12345678&quot;]</td>  </tr>        <tr>     <td>unit_visit_report_link</td>     <td>array</td>     <td></td>          <td>UNIT VISIT REPORT LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>cersai_check_report_link</td>     <td>array</td>     <td></td>          <td>DRF Image</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>balance_transfer_report_link</td>     <td>array</td>     <td></td>          <td>BALANCE TRANSFER REPORT LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>noc_from_existing_lender_link</td>     <td>array</td>     <td></td>          <td>NOC FROM EXISTING LENDER LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>property_tax_card_or_receipt_link</td>     <td>array</td>     <td></td>          <td>PROPERTY TAX CARD/RECEIPT_LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>water_tax_or_receipt_link</td>     <td>array</td>     <td></td>          <td>WATER TAX CARD/RECEIPT_LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>eb_card_link</td>     <td>array</td>     <td></td>          <td>EB CARD LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>mod_receipt_link</td>     <td>array</td>     <td></td>          <td>MOD RECEIPT_LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>entire_set_of_property_documents_link</td>     <td>array</td>     <td></td>          <td>ENTIRE SET OF PROPERTY DOCUMENTS LINK</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>    </tbody>       </table>    #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.property_review_success import PropertyReviewSuccess
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.body_property_review import BodyPropertyReview
from credavenue_colending.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_property_review = BodyPropertyReview(
        legal_report_link=[
            "legal_report_link_example",
        ],
        validation_report_link=[
            "validation_report_link_example",
        ],
        collateral_photo_link=[
            "collateral_photo_link_example",
        ],
        field_verification_report_link=[
            "field_verification_report_link_example",
        ],
        tele_verification_report_link=[
            "tele_verification_report_link_example",
        ],
        property_inspection_report_link=[
            "property_inspection_report_link_example",
        ],
        unit_visit_report_link=[
            "unit_visit_report_link_example",
        ],
        cersai_check_report_link=[
            "cersai_check_report_link_example",
        ],
        balance_transfer_report_link=[
            "balance_transfer_report_link_example",
        ],
        noc_from_existing_lender_link=[
            "noc_from_existing_lender_link_example",
        ],
        property_tax_card_or_receipt_link=[
            "property_tax_card_or_receipt_link_example",
        ],
        water_tax_or_receipt_link=[
            "water_tax_or_receipt_link_example",
        ],
        eb_card_link=[
            "eb_card_link_example",
        ],
        mod_receipt_link=[
            "mod_receipt_link_example",
        ],
        entire_set_of_property_documents_link=[
            "entire_set_of_property_documents_link_example",
        ],
    ) # BodyPropertyReview | 

    # example passing only required values which don't have defaults set
    try:
        # #Property Review
        api_response = api_instance.property_review(product_id, client_name, loan_id, body_property_review)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->property_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_property_review** | [**BodyPropertyReview**](BodyPropertyReview.md)|  |

### Return type

[**PropertyReviewSuccess**](PropertyReviewSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_advance_collection**
> RequestSuccess update_advance_collection(product_id, client_name, loan_id, advance_payment_id, body_update_advance_collection)

#Update Advance Collection

Update Advance Collection API

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>investor_transfer_date</td>     <td>string</td>     <td>date</td>          <td>Date when originator transferred the amount to investor (YYYY-MM-DD)</td>       <td>2020-10-03</td>  </tr>    </tbody>       </table>    Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table> 

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.body_update_advance_collection import BodyUpdateAdvanceCollection
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.request_success import RequestSuccess
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    advance_payment_id = "1276" # str | Advance Payment ID returned in Create Advance API
    body_update_advance_collection = BodyUpdateAdvanceCollection(
        investor_transfer_date=dateutil_parser('1970-01-01').date(),
    ) # BodyUpdateAdvanceCollection | 

    # example passing only required values which don't have defaults set
    try:
        # #Update Advance Collection
        api_response = api_instance.update_advance_collection(product_id, client_name, loan_id, advance_payment_id, body_update_advance_collection)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->update_advance_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **advance_payment_id** | **str**| Advance Payment ID returned in Create Advance API |
 **body_update_advance_collection** | [**BodyUpdateAdvanceCollection**](BodyUpdateAdvanceCollection.md)|  |

### Return type

[**RequestSuccess**](RequestSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection_entry**
> AgreementSignedSuccess update_collection_entry(product_id, client_name, loan_id, payment_id, body_update_collection_entry)

#Update Collection Entry

Update Collection API

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>investor_transfer_date</td>     <td>string</td>     <td>date</td>          <td>Date when originator transferred the amount to investor (YYYY-MM-DD)</td>       <td>2021-02-02</td>  </tr>    </tbody>       </table>    <h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>investor_transfer_date</td>     <td>string</td>     <td>date</td>          <td>Date when originator transferred the amount to investor (YYYY-MM-DD)</td>       <td>2016-06-16</td>  </tr>    </tbody>       </table>     # Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>
### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.body_update_collection_entry import BodyUpdateCollectionEntry
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.agreement_signed_success import AgreementSignedSuccess
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    payment_id = "ref-1269653245" # str | Payment Reference/Instrument Number as provided during collection creation
    body_update_collection_entry = BodyUpdateCollectionEntry(
        investor_transfer_date=dateutil_parser('1970-01-01').date(),
    ) # BodyUpdateCollectionEntry | 

    # example passing only required values which don't have defaults set
    try:
        # #Update Collection Entry
        api_response = api_instance.update_collection_entry(product_id, client_name, loan_id, payment_id, body_update_collection_entry)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->update_collection_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **payment_id** | **str**| Payment Reference/Instrument Number as provided during collection creation |
 **body_update_collection_entry** | [**BodyUpdateCollectionEntry**](BodyUpdateCollectionEntry.md)|  |

### Return type

[**AgreementSignedSuccess**](AgreementSignedSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan**
> RequestSuccess update_loan(product_id, client_name, loan_id, body_update_loan)

#Update Loan

Update Loan API - This endpoint can be used to update the loan status to agreement signed.  **Expected Loan Status: "approved"**

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>principal_amount</td>     <td>number</td>     <td>float</td>          <td>Total Loan Amount to the Borrower (in Rupees)</td>       <td>1000000.0</td>  </tr>        <tr>     <td>loan_amount</td>     <td>number</td>     <td>float</td>          <td>Total Loan Amount</td>       <td>1000000.0</td>  </tr>        <tr>     <td>interest_rate</td>     <td>number</td>     <td>float</td>          <td>Reducing balance interest rate of the customer in %. This is the interest rate to be mentioned in the sanction letter as well</td>       <td>20.2</td>  </tr>        <tr>     <td>tenure</td>     <td>integer</td>     <td></td>          <td>Tenure of the loan</td>       <td>12</td>  </tr>        <tr>     <td>tenure_frequency</td>     <td>string</td>     <td></td>          <td>Daily / Weekly / Monthly</td>       <td>monthly</td>  </tr>        <tr>     <td>repayment_frequency</td>     <td>string</td>     <td></td>          <td>Daily / Weekly / Monthly / Bullet</td>       <td>monthly</td>  </tr>        <tr>     <td>number_of_repayments</td>     <td>integer</td>     <td></td>          <td>Number of repayments as per the repayment schedule</td>       <td>12</td>  </tr>        <tr>     <td>disbursement_accounts</td>     <td>array</td>     <td></td>          <td>Refer table DisbursementAccounts for attributes</td>       <td>[{&quot;id&quot;:&quot;1&quot;,&quot;account_type&quot;:&quot;borrower&quot;,&quot;bank_name&quot;:&quot;HDFC&quot;,&quot;bank_account_type&quot;:&quot;savings&quot;,&quot;account_name&quot;:&quot;Arya&quot;,&quot;bank_branch_name&quot;:&quot;Nandanam&quot;,&quot;ifsc_code&quot;:&quot;HDFC000123&quot;,&quot;entity_type&quot;:&quot;end_customer&quot;,&quot;account_no&quot;:&quot;54321678912&quot;,&quot;amount&quot;:100000.0},{&quot;id&quot;:&quot;1&quot;,&quot;account_type&quot;:&quot;borrower&quot;,&quot;bank_name&quot;:&quot;HDFC&quot;,&quot;bank_account_type&quot;:&quot;savings&quot;,&quot;account_name&quot;:&quot;Arya&quot;,&quot;bank_branch_name&quot;:&quot;Nandanam&quot;,&quot;ifsc_code&quot;:&quot;HDFC000123&quot;,&quot;entity_type&quot;:&quot;end_customer&quot;,&quot;account_no&quot;:&quot;54321678912&quot;,&quot;amount&quot;:100000.0}]</td>  </tr>    </tbody>       </table>   <h4>DisbursementAccounts</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>id</td>     <td>string</td>     <td></td>          <td>ID as provided in Get Loan Details API</td>       <td>1</td>  </tr>        <tr>     <td>account_type</td>     <td>string</td>     <td></td>          <td>Borrower/Existing Lender</td>       <td>borrower</td>  </tr>        <tr>     <td>bank_name</td>     <td>string</td>     <td></td>          <td>Name of the bank where disbursement needs to be done</td>       <td>HDFC</td>  </tr>        <tr>     <td>bank_account_type</td>     <td>string</td>     <td></td>          <td>Account type - Savings/Current/Overdraft/CC</td>       <td>savings</td>  </tr>        <tr>     <td>account_name</td>     <td>string</td>     <td></td>          <td>Bank account name where disbursement needs to be done</td>       <td>Arya</td>  </tr>        <tr>     <td>bank_branch_name</td>     <td>string</td>     <td></td>          <td>Bank branch name where disbursement needs to be done</td>       <td>Nandanam</td>  </tr>        <tr>     <td>ifsc_code</td>     <td>string</td>     <td></td>          <td>Bank IFSC where disbursement needs to be done</td>       <td>HDFC000123</td>  </tr>        <tr>     <td>entity_type</td>     <td>string</td>     <td></td>          <td>Dealer / Sub-Dealer / Originator / Existing Lender / End Customer</td>       <td>end_customer</td>  </tr>        <tr>     <td>account_no</td>     <td>string</td>     <td></td>          <td>Account number of the bank where disbursement needs to be done</td>       <td>54321678912</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Amount to be transferred to particular Vendor/Borrower</td>       <td>100000.0</td>  </tr>    </tbody>       </table>     #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.request_success import RequestSuccess
from credavenue_colending.model.body_update_loan import BodyUpdateLoan
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_update_loan = BodyUpdateLoan(
        principal_amount=3.14,
        loan_amount=3.14,
        interest_rate=3.14,
        tenure=1,
        tenure_frequency="tenure_frequency_example",
        repayment_frequency="repayment_frequency_example",
        number_of_repayments=1,
        disbursement_accounts=[
            BodyUpdateLoanDisbursementAccounts(
                id="id_example",
                account_type="account_type_example",
                bank_name="bank_name_example",
                bank_account_type="bank_account_type_example",
                account_name="account_name_example",
                bank_branch_name="bank_branch_name_example",
                ifsc_code="ifsc_code_example",
                entity_type="entity_type_example",
                account_no="account_no_example",
                amount=3.14,
            ),
        ],
    ) # BodyUpdateLoan | 

    # example passing only required values which don't have defaults set
    try:
        # #Update Loan
        api_response = api_instance.update_loan(product_id, client_name, loan_id, body_update_loan)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->update_loan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_update_loan** | [**BodyUpdateLoan**](BodyUpdateLoan.md)|  |

### Return type

[**RequestSuccess**](RequestSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post_disbursement**
> RequestSuccess update_post_disbursement(product_id, client_name, loan_id, body_update_post_disbursement)

Update Post Disbursement API

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>customer_type</td>     <td>string</td>     <td></td>          <td>Individual / Corporate</td>       <td>individual</td>  </tr>        <tr>     <td>customer_category</td>     <td>string</td>     <td></td>          <td>Salaried, Self-Empolyed</td>       <td>salaried</td>  </tr>        <tr>     <td>first_name</td>     <td>string</td>     <td></td>          <td>First Name of the Customer</td>       <td>Neeraj</td>  </tr>        <tr>     <td>middle_name</td>     <td>string</td>     <td></td>          <td>Middle Name of the Customer</td>       <td>Kumar</td>  </tr>        <tr>     <td>last_name</td>     <td>string</td>     <td></td>          <td>Last Name of the Customer</td>       <td>Chopra</td>  </tr>        <tr>     <td>gender</td>     <td>string</td>     <td></td>          <td>M / F / O</td>       <td>M</td>  </tr>        <tr>     <td>date_of_birth</td>     <td>string</td>     <td>date</td>          <td>Date of birth in YYYY-MM-DD</td>       <td>1995-12-05</td>  </tr>        <tr>     <td>age</td>     <td>integer</td>     <td></td>          <td>Age in years</td>       <td>26</td>  </tr>        <tr>     <td>mobile_number</td>     <td>integer</td>     <td></td>          <td>Mobile Number of the Customer (10 digits)</td>       <td>9876543210</td>  </tr>        <tr>     <td>email</td>     <td>string</td>     <td></td>          <td>Permanent Email id of the Customer</td>       <td>minato@gmail.com</td>  </tr>        <tr>     <td>official_email_id</td>     <td>string</td>     <td></td>          <td>Official Email ID of the Customer</td>       <td>minato_namikaze@credavenue.com</td>  </tr>        <tr>     <td>current_address</td>     <td>string</td>     <td></td>          <td>Current address of the applicant. Free flowing text</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>current_city</td>     <td>string</td>     <td></td>          <td>City in which applicant is currently residing. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_district</td>     <td>string</td>     <td></td>          <td>District in which applicant is currently residing. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_state</td>     <td>string</td>     <td></td>          <td>State in which applicant is currently residing. Free flowing for now</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>current_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_current_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>rented</td>  </tr>        <tr>     <td>years_of_stay_in_current_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the current address</td>       <td>5</td>  </tr>        <tr>     <td>permanent_address</td>     <td>string</td>     <td></td>          <td>Permanent address of the customer. Free flowing for now</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>permanent_city</td>     <td>string</td>     <td></td>          <td>Permanent city of the customer. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_district</td>     <td>string</td>     <td></td>          <td>Permanent district of the customer. Free flowing for now</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_state</td>     <td>string</td>     <td></td>          <td>Permanent state of the customer. Free flowing for now</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>permanent_pincode</td>     <td>integer</td>     <td></td>          <td>Permanent pincode of the customer. Free flowing for now</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_permanent_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>owned</td>  </tr>        <tr>     <td>years_of_stay_in_permanent_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the permanent address</td>       <td>5</td>  </tr>        <tr>     <td>marital_status</td>     <td>string</td>     <td></td>          <td>married / unmarried</td>       <td>unmarried</td>  </tr>        <tr>     <td>religion</td>     <td>string</td>     <td></td>          <td>Religion of customer. Free flow text</td>       <td>Hindu</td>  </tr>        <tr>     <td>nationality</td>     <td>string</td>     <td></td>          <td>Nationality of customer. Free flow text</td>       <td>indian</td>  </tr>        <tr>     <td>father_name</td>     <td>string</td>     <td></td>          <td>Father name of customer. Free flow text</td>       <td>Dan Kato</td>  </tr>        <tr>     <td>mother_name</td>     <td>string</td>     <td></td>          <td>Mother name of customer; Free flow text</td>       <td>Tsunade Senju</td>  </tr>        <tr>     <td>spouse_name</td>     <td>string</td>     <td></td>          <td>Spouse name of customer; Free flow text</td>       <td>Kushina Uzumaki</td>  </tr>        <tr>     <td>education_qualification</td>     <td>string</td>     <td></td>          <td>Educational Qualifications</td>       <td>MBA</td>  </tr>        <tr>     <td>net_monthly_income</td>     <td>number</td>     <td>float</td>          <td>Monthly Income of the Customer (in Rupees)</td>       <td>10000.0</td>  </tr>        <tr>     <td>annual_income</td>     <td>number</td>     <td>float</td>          <td>Annual income of the customer in number (don’t convert into thousand/lacs etc)</td>       <td>120000.0</td>  </tr>        <tr>     <td>no_of_dependants</td>     <td>integer</td>     <td></td>          <td>Number of dependants</td>       <td>3</td>  </tr>        <tr>     <td>occupation</td>     <td>string</td>     <td></td>          <td>salaried / business / retired / self_employed and others</td>       <td>salaried</td>  </tr>        <tr>     <td>pan_number</td>     <td>string</td>     <td></td>          <td>PAN number of customer</td>       <td>BMMPH9018G</td>  </tr>        <tr>     <td>pan_number_link</td>     <td>array</td>     <td></td>          <td>PAN image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>form_60_link</td>     <td>array</td>     <td></td>          <td>Form 60 If applicable</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aadhar_number</td>     <td>string</td>     <td></td>          <td>Aadhar number of customer</td>       <td>794065231234</td>  </tr>        <tr>     <td>aadhar_link</td>     <td>array</td>     <td></td>          <td>Aadhar image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>voter_id_number</td>     <td>string</td>     <td></td>          <td>Voter ID Number of customer</td>       <td>RTG2291234</td>  </tr>        <tr>     <td>voting_id_link</td>     <td>array</td>     <td></td>          <td>Voter ID image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>driving_license_number</td>     <td>string</td>     <td></td>          <td>Driving license number of customer</td>       <td>TN0112345</td>  </tr>        <tr>     <td>driving_license_link</td>     <td>array</td>     <td></td>          <td>Driving License image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>passport_number</td>     <td>string</td>     <td></td>          <td>Passport number of customer</td>       <td>L4018345</td>  </tr>        <tr>     <td>passport_link</td>     <td>array</td>     <td></td>          <td>Passport image of the document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_image_link</td>     <td>array</td>     <td></td>          <td>Video KYC of the Applicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_kyc_detail</td>     <td>object</td>        <td></td>     <td>Refer table VideoKycDetail for attributes</td>       <td>{&quot;profile_id&quot;:&quot;AB12345&quot;,&quot;account_id&quot;:&quot;AB12345&quot;,&quot;key&quot;:&quot;abc@123&quot;}</td>  </tr>        <tr>     <td>other_kyc_number</td>     <td>string</td>     <td></td>          <td>KYC Number of the Customer</td>       <td>ABC1234</td>  </tr>        <tr>     <td>other_kyc_link</td>     <td>array</td>     <td></td>          <td>KYC Image of the Customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>rent_agreement_link</td>     <td>array</td>     <td></td>          <td>KYC number of customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>utility_bills_link</td>     <td>array</td>     <td></td>          <td>Utility bills link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo Image of the Customer</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>employment_type</td>     <td>string</td>     <td></td>          <td>salaried / self_employed</td>       <td>self_employed</td>  </tr>        <tr>     <td>employment_details_name</td>     <td>string</td>     <td></td>          <td>Employer name. Free flowing text</td>       <td>Credavenue</td>  </tr>        <tr>     <td>employment_details_address</td>     <td>string</td>     <td></td>          <td>Office address. Free flowing text</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>employment_details_years_of_experience</td>     <td>number</td>     <td>float</td>          <td>Applicant Number of years in the current organization</td>       <td>5.0</td>  </tr>        <tr>     <td>employment_details_designation</td>     <td>string</td>     <td></td>          <td>Designation in current role, free flowing text</td>       <td>Manager</td>  </tr>        <tr>     <td>employement_vintage_current_organisation</td>     <td>integer</td>     <td></td>          <td>No of Years in the same Organisation</td>       <td>3</td>  </tr>        <tr>     <td>payslip_link</td>     <td>array</td>     <td></td>          <td>Last three month pay slip</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>tds_certificate_link</td>     <td>array</td>     <td></td>          <td>Last Three Year TDS Certificate Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>name_of_bureau</td>     <td>string</td>     <td></td>          <td>Cibil / Experian / Himark</td>       <td>cibil</td>  </tr>        <tr>     <td>bureau_vintage</td>     <td>integer</td>     <td></td>          <td>Vintage in the bureau. Number of years from the first trade line</td>       <td>3</td>  </tr>        <tr>     <td>bureau_score</td>     <td>integer</td>     <td></td>          <td>Bureau Score</td>       <td>650</td>  </tr>        <tr>     <td>bureau_report_link</td>     <td>array</td>     <td></td>          <td>Document of the bureau</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>commercial_bureau_score</td>     <td>integer</td>     <td></td>          <td>CRIF score</td>       <td>330</td>  </tr>        <tr>     <td>commercial_bureau_score_link</td>     <td>array</td>     <td></td>          <td>Commercial Bureau Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>partner_score_on_the_customer</td>     <td>number</td>     <td>float</td>          <td>Score Captured by the Partner</td>       <td>800.0</td>  </tr>        <tr>     <td>total_existing_obligations</td>     <td>integer</td>     <td></td>          <td>Total Existing Obligations basis the Bureau Report</td>       <td>25000</td>  </tr>        <tr>     <td>credit_card_limit</td>     <td>integer</td>     <td></td>          <td>Total Credit Card Limit basis the Bureau Report</td>       <td>30000</td>  </tr>        <tr>     <td>number_of_credit_cards</td>     <td>integer</td>     <td></td>          <td>Total Number of Credit Cards per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_unsecured_loans</td>     <td>integer</td>     <td></td>          <td>Total Number of Unsecured Loans per Bureau Report</td>       <td>2</td>  </tr>        <tr>     <td>value_of_total_unsecured_loans</td>     <td>number</td>     <td>float</td>          <td>Total value of unsecured loans</td>       <td>20000.0</td>  </tr>        <tr>     <td>number_of_loans</td>     <td>integer</td>     <td></td>          <td>Total Number of Loans per Bureau Report</td>       <td>2</td>  </tr>        <tr>     <td>value_of_total_loans</td>     <td>number</td>     <td>float</td>          <td>Total value of loans</td>       <td>20000.0</td>  </tr>        <tr>     <td>number_of_enquiries_3months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 3 Months per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_enquiries_6months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 6 Months per Bureau Report</td>       <td>3</td>  </tr>        <tr>     <td>number_of_enquiries_12months</td>     <td>integer</td>     <td></td>          <td>Number of Enquiries in the Last 12 Months per Bureau Report</td>       <td>4</td>  </tr>        <tr>     <td>number_of_writeoff_suitfiled_settled_12months</td>     <td>integer</td>     <td></td>          <td>Number of Writeoff Suitfiled Settled in the Last 12 Months</td>       <td>4</td>  </tr>        <tr>     <td>max_dpd_tradeline_12months</td>     <td>integer</td>     <td></td>          <td>Maximum DPD Tradeline in the Last 12 Months</td>       <td>6</td>  </tr>        <tr>     <td>max_overdue_tradeline</td>     <td>integer</td>     <td></td>          <td>Maximum Overdue Tradeline</td>       <td>6</td>  </tr>        <tr>     <td>total_overdue_amount_12months</td>     <td>number</td>     <td>float</td>          <td>Total Overdue Amount in the Last 12 Months</td>       <td>10000.0</td>  </tr>        <tr>     <td>loan_amount_settled_12months</td>     <td>number</td>     <td>float</td>          <td>Loan Amount Settled in the Last 12 Months</td>       <td>25000.0</td>  </tr>        <tr>     <td>nature_of_loan_settled1</td>     <td>string</td>     <td></td>          <td>The nature of past loan settlement if any (Loan 1) - Settled/ Closed/ Written-off</td>       <td>settled</td>  </tr>        <tr>     <td>nature_of_loan_settled2</td>     <td>string</td>     <td></td>          <td>The nature of past loan settlement if any (Loan 2) - Settled/ Closed/ Written-off</td>       <td>closed</td>  </tr>        <tr>     <td>total_emi_bounces</td>     <td>integer</td>     <td></td>          <td>Total EMI Bounces</td>       <td>3</td>  </tr>        <tr>     <td>emi_bounces_6months</td>     <td>integer</td>     <td></td>          <td>EMI Bounces in the Last 6 Months</td>       <td>3</td>  </tr>        <tr>     <td>emi_bounces_12months</td>     <td>integer</td>     <td></td>          <td>EMI Bounces in the Last 12 Months</td>       <td>3</td>  </tr>        <tr>     <td>bank_statement</td>     <td>object</td>      <td></td>       <td>Refer table BankStatement for attributes</td>       <td>{&quot;bank_statement_savings_account_12_months_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_current_account_12_months_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;no_of_inward_chq_returns_savings_account&quot;:3,&quot;no_of_outward_chq_returns_savings_account&quot;:4,&quot;no_of_inward_chq_returns_current_account&quot;:5,&quot;no_of_outward_chq_returns_current_account&quot;:6,&quot;bank_account_type_for_assessment&quot;:&quot;savings&quot;,&quot;perfios_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;finbit_link&quot;:&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;abb&quot;:25000.0,&quot;abd&quot;:10000.0}</td>  </tr>        <tr>     <td>financial_data</td>     <td>object</td>        <td></td>     <td>Refer table FinancialData for attributes</td>       <td>{&quot;annual_business_turnover&quot;:1000000.0,&quot;annual_gross_profit&quot;:8000000.0,&quot;annual_business_ebitda&quot;:5000000.0,&quot;monthly_net_profit&quot;:14000.0,&quot;annual_net_profit&quot;:30000000.0,&quot;gst_return_year_1_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;gst_return_year_2_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;gst_return_year_3_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;it_return_year_1_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;it_return_year_2_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;it_return_year_3_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;other_income_assessment_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;cam_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;cfa_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]}</td>  </tr>        <tr>     <td>co_applicants</td>     <td>array</td>     <td></td>          <td>Refer table CoApplicants for attributes</td>       <td>[{&quot;relationship_with_applicant&quot;:&quot;father&quot;,&quot;first_name&quot;:&quot;Minato&quot;,&quot;middle_name&quot;:&quot;Kumar&quot;,&quot;last_name&quot;:&quot;Namikaze&quot;,&quot;gender&quot;:&quot;M&quot;,&quot;date_of_birth&quot;:&quot;1995-12-05&quot;,&quot;age&quot;:26,&quot;mobile_number&quot;:9876543210,&quot;email&quot;:&quot;minato@gmail.com&quot;,&quot;current_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;current_city&quot;:&quot;Chennai&quot;,&quot;current_district&quot;:&quot;Chennai&quot;,&quot;current_state&quot;:&quot;tamil_nadu&quot;,&quot;current_pincode&quot;:600089,&quot;residence_type_current_address&quot;:&quot;rented&quot;,&quot;years_of_stay_in_current_address&quot;:5,&quot;permanent_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;permanent_city&quot;:&quot;Chennai&quot;,&quot;permanent_district&quot;:&quot;Chennai&quot;,&quot;permanent_state&quot;:&quot;tamil_nadu&quot;,&quot;permanent_pincode&quot;:600089,&quot;residence_type_permanent_address&quot;:&quot;owned&quot;,&quot;years_of_stay_in_permanent_address&quot;:5,&quot;marital_status&quot;:&quot;unmarried&quot;,&quot;religion&quot;:&quot;buddhist&quot;,&quot;nationality&quot;:&quot;indian&quot;,&quot;father_name&quot;:&quot;Dan Kato&quot;,&quot;mother_name&quot;:&quot;Tsunade Senju&quot;,&quot;spouse_name&quot;:&quot;Kushina Uzumaki&quot;,&quot;education&quot;:&quot;Hokage&quot;,&quot;annual_income&quot;:120000.0,&quot;income_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_12_months_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_number&quot;:&quot;BMMPG9018Y&quot;,&quot;pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number&quot;:&quot;794065346725&quot;,&quot;aadhar_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voting_id_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_license_number&quot;:&quot;TN01123345&quot;,&quot;driving_license_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_kyc_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_kyc_profile_id&quot;:&quot;ABC12345&quot;,&quot;video_kyc_account_id&quot;:&quot;ABC12345&quot;,&quot;video_kyc_key&quot;:&quot;abc_123&quot;,&quot;other_kyc_number&quot;:&quot;ABC12456&quot;,&quot;other_kyc_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_score&quot;:700,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;partner_score&quot;:3},{&quot;relationship_with_applicant&quot;:&quot;father&quot;,&quot;first_name&quot;:&quot;Minato&quot;,&quot;middle_name&quot;:&quot;Kumar&quot;,&quot;last_name&quot;:&quot;Namikaze&quot;,&quot;gender&quot;:&quot;M&quot;,&quot;date_of_birth&quot;:&quot;1995-12-05&quot;,&quot;age&quot;:26,&quot;mobile_number&quot;:9876543210,&quot;email&quot;:&quot;minato@gmail.com&quot;,&quot;current_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;current_city&quot;:&quot;Chennai&quot;,&quot;current_district&quot;:&quot;Chennai&quot;,&quot;current_state&quot;:&quot;tamil_nadu&quot;,&quot;current_pincode&quot;:600089,&quot;residence_type_current_address&quot;:&quot;rented&quot;,&quot;years_of_stay_in_current_address&quot;:5,&quot;permanent_address&quot;:&quot;2, Mount Road, Teynampet&quot;,&quot;permanent_city&quot;:&quot;Chennai&quot;,&quot;permanent_district&quot;:&quot;Chennai&quot;,&quot;permanent_state&quot;:&quot;tamil_nadu&quot;,&quot;permanent_pincode&quot;:600089,&quot;residence_type_permanent_address&quot;:&quot;owned&quot;,&quot;years_of_stay_in_permanent_address&quot;:5,&quot;marital_status&quot;:&quot;unmarried&quot;,&quot;religion&quot;:&quot;buddhist&quot;,&quot;nationality&quot;:&quot;indian&quot;,&quot;father_name&quot;:&quot;Dan Kato&quot;,&quot;mother_name&quot;:&quot;Tsunade Senju&quot;,&quot;spouse_name&quot;:&quot;Kushina Uzumaki&quot;,&quot;education&quot;:&quot;Hokage&quot;,&quot;annual_income&quot;:120000.0,&quot;income_proof_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bank_statement_12_months_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;pan_number&quot;:&quot;BMMPG9018Y&quot;,&quot;pan_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;aadhar_number&quot;:&quot;794065346725&quot;,&quot;aadhar_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;voter_id_number&quot;:&quot;RTG2291234&quot;,&quot;voting_id_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;driving_license_number&quot;:&quot;TN01123345&quot;,&quot;driving_license_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;passport_number&quot;:&quot;L4018345&quot;,&quot;passport_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_kyc_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;video_kyc_profile_id&quot;:&quot;ABC12345&quot;,&quot;video_kyc_account_id&quot;:&quot;ABC12345&quot;,&quot;video_kyc_key&quot;:&quot;abc_123&quot;,&quot;other_kyc_number&quot;:&quot;ABC12456&quot;,&quot;other_kyc_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;rent_agreement_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;utility_bills_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;photo_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;bureau_score&quot;:700,&quot;bureau_report_link&quot;:[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;,&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;],&quot;partner_score&quot;:3}]</td>  </tr>        <tr>     <td>abb_emi_ratio</td>     <td>number</td>     <td>float</td>          <td>Average Bank balance to EMI</td>       <td>2.0</td>  </tr>        <tr>     <td>dscr</td>     <td>number</td>     <td>float</td>          <td>Debt Service Coverage Ratio</td>       <td>3.0</td>  </tr>        <tr>     <td>foir</td>     <td>number</td>     <td>float</td>          <td>Fixed Obligations to Income Ratio</td>       <td>4.0</td>  </tr>        <tr>     <td>ltr</td>     <td>number</td>     <td>float</td>          <td>Loan Transfer Ratio</td>       <td>5.0</td>  </tr>        <tr>     <td>eligibility_loan_amount</td>     <td>number</td>     <td>float</td>          <td>Eligibility Loan amount</td>       <td>40000.0</td>  </tr>        <tr>     <td>insurance_details</td>     <td>array</td>     <td></td>          <td>Refer table InsuranceDetails for attributes</td>       <td>[{&quot;insurance_type&quot;:&quot;credit&quot;,&quot;insurer_name&quot;:&quot;Tata AIG&quot;,&quot;nominee_details&quot;:&quot;Neeraj&quot;,&quot;relationship&quot;:&quot;friend&quot;,&quot;premium&quot;:100000.0,&quot;insurance_amount&quot;:300000.0,&quot;policy_number&quot;:&quot;ABC12345&quot;},{&quot;insurance_type&quot;:&quot;credit&quot;,&quot;insurer_name&quot;:&quot;Tata AIG&quot;,&quot;nominee_details&quot;:&quot;Neeraj&quot;,&quot;relationship&quot;:&quot;friend&quot;,&quot;premium&quot;:100000.0,&quot;insurance_amount&quot;:300000.0,&quot;policy_number&quot;:&quot;ABC12345&quot;}]</td>  </tr>        <tr>     <td>references</td>     <td>array</td>     <td></td>          <td>Refer table References for attributes</td>       <td>[{&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;pincode&quot;:&quot;600001&quot;,&quot;phone&quot;:&quot;9876543210&quot;},{&quot;name&quot;:&quot;Neeraj Chopra&quot;,&quot;address&quot;:&quot;221B, Baker Street, Chennai&quot;,&quot;pincode&quot;:&quot;600001&quot;,&quot;phone&quot;:&quot;9876543210&quot;}]</td>  </tr>        <tr>     <td>psl_flag</td>     <td>string</td>     <td></td>          <td>Does this loan belong to Priority Sector Lending?</td>       <td>t</td>  </tr>        <tr>     <td>psl_description</td>     <td>string</td>     <td></td>          <td>Description on Priority Sector Lending</td>       <td>psl_description_47</td>  </tr>        <tr>     <td>psl_code</td>     <td>string</td>     <td></td>          <td>Priority Sector Lending code</td>       <td>psl_code_65</td>  </tr>        <tr>     <td>psl_proof_link</td>     <td>array</td>     <td></td>          <td>Any documents as proof for PSL</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>loan_agreement_link</td>     <td>array</td>     <td></td>          <td>Loan Agreement Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>sanction_letter_link</td>     <td>array</td>     <td></td>          <td>Sanction letter Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>laf_link</td>     <td>array</td>     <td></td>          <td>LAF Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>self_declaration_letter_link</td>     <td>array</td>     <td></td>          <td>Self declaration form link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>authorisation_letter_link</td>     <td>array</td>     <td></td>          <td>Authorisation letter link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>enach_pdc_link</td>     <td>array</td>     <td></td>          <td>eNACH PDC Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>guarantor_agreements_link</td>     <td>array</td>     <td></td>          <td>Guarantor Agreements Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>    </tbody>       </table>   <h4>VideoKycDetail</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>profile_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Profile ID of the case as per the video KYC vendor</td>       <td>AB12345</td>  </tr>        <tr>     <td>account_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Account ID of the case as per the video KYC vendor</td>       <td>AB12345</td>  </tr>        <tr>     <td>key</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Key as per the video KYC vendor</td>       <td>abc@123</td>  </tr>    </tbody>       </table>   <h4>BankStatement</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>bank_statement_savings_account_12_months_link</td>     <td>array</td>     <td></td>          <td>Savings bank account statement for last 12 months</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bank_statement_current_account_12_months_link</td>     <td>array</td>     <td></td>          <td>Current account bank details for last 12 months</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>no_of_inward_chq_returns_savings_account</td>     <td>integer</td>     <td></td>          <td>Number of inward cheque returns in savings account</td>       <td>3</td>  </tr>        <tr>     <td>no_of_outward_chq_returns_savings_account</td>     <td>integer</td>     <td></td>          <td>Number of outward cheque returns in savings account</td>       <td>4</td>  </tr>        <tr>     <td>no_of_inward_chq_returns_current_account</td>     <td>integer</td>     <td></td>          <td>Number of inward cheque returns in current account</td>       <td>5</td>  </tr>        <tr>     <td>no_of_outward_chq_returns_current_account</td>     <td>integer</td>     <td></td>          <td>Number of outward cheque returns in current account</td>       <td>6</td>  </tr>        <tr>     <td>bank_account_type_for_assessment</td>     <td>string</td>     <td></td>          <td>Savings / Current / Overdraft / CC</td>       <td>savings</td>  </tr>        <tr>     <td>perfios_link</td>     <td>string</td>     <td></td>          <td>Perfios report in form of document</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>finbit_link</td>     <td>string</td>     <td></td>          <td>Finbit Link</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg</td>  </tr>        <tr>     <td>abb</td>     <td>number</td>     <td>float</td>          <td>Average Bank Balance maintaiend on the EMI dates (Calculated by the Originator for the Last 12 Months)</td>       <td>25000.0</td>  </tr>        <tr>     <td>abd</td>     <td>number</td>     <td>float</td>          <td>Average Monthly Bank Deposits for the Last 12 Months</td>       <td>10000.0</td>  </tr>    </tbody>       </table>   <h4>FinancialData</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>annual_business_turnover</td>     <td>number</td>     <td>float</td>          <td>Annual Business Turnover (in Rupees)</td>       <td>1000000.0</td>  </tr>        <tr>     <td>annual_gross_profit</td>     <td>number</td>     <td>float</td>          <td>Annual Gross Profit (in Rupees)</td>       <td>8000000.0</td>  </tr>        <tr>     <td>annual_business_ebitda</td>     <td>number</td>     <td>float</td>          <td>Annual Business EBITDA (in Rupees)</td>       <td>5000000.0</td>  </tr>        <tr>     <td>monthly_net_profit</td>     <td>number</td>     <td>float</td>          <td>Monthly Net Profit (in Rupees)</td>       <td>14000.0</td>  </tr>        <tr>     <td>annual_net_profit</td>     <td>number</td>     <td>float</td>          <td>Net Profit After Tax (in Rupees)</td>       <td>30000000.0</td>  </tr>        <tr>     <td>gst_return_year_1_link</td>     <td>array</td>     <td></td>          <td>GST return image for last year</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>gst_return_year_2_link</td>     <td>array</td>     <td></td>          <td>GST return image for last year -1</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>gst_return_year_3_link</td>     <td>array</td>     <td></td>          <td>GST return image for last year -2</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>it_return_year_1_link</td>     <td>array</td>     <td></td>          <td>IT return image for last year</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>it_return_year_2_link</td>     <td>array</td>     <td></td>          <td>IT return image for last year -1</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>it_return_year_3_link</td>     <td>array</td>     <td></td>          <td>IT return image for last year - 2</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>other_income_assessment_proof_link</td>     <td>array</td>     <td></td>          <td>Image of other bills</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>cam_link</td>     <td>array</td>     <td></td>          <td>CAM Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>cfa_link</td>     <td>array</td>     <td></td>          <td>CFA Document</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>    </tbody>       </table>   <h4>CoApplicants</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>relationship_with_applicant</td>     <td>string</td>     <td></td>          <td>Father/Mother/Brother/Son/Daughter/Friend/Other relative</td>       <td>father</td>  </tr>        <tr>     <td>first_name</td>     <td>string</td>     <td></td>          <td>First Name of the CoApplicant</td>       <td>Minato</td>  </tr>        <tr>     <td>middle_name</td>     <td>string</td>     <td></td>          <td>Middle Name of the CoApplicant</td>       <td>Kumar</td>  </tr>        <tr>     <td>last_name</td>     <td>string</td>     <td></td>          <td>Last Name of the CoApplicant</td>       <td>Namikaze</td>  </tr>        <tr>     <td>gender</td>     <td>string</td>     <td></td>          <td>M / F / O</td>       <td>M</td>  </tr>        <tr>     <td>date_of_birth</td>     <td>string</td>     <td>date</td>          <td>Date of Birth (YYYY-MM-DD)</td>       <td>1995-12-05</td>  </tr>        <tr>     <td>age</td>     <td>integer</td>     <td></td>          <td>Age in years</td>       <td>26</td>  </tr>        <tr>     <td>mobile_number</td>     <td>integer</td>     <td></td>          <td>Mobile Number of the CoApplicant (10 digits)</td>       <td>9876543210</td>  </tr>        <tr>     <td>email</td>     <td>string</td>     <td></td>          <td>Personal Email ID of the CoApplicant</td>       <td>minato@gmail.com</td>  </tr>        <tr>     <td>current_address</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>2, Mount Road, Teynampet</td>  </tr>        <tr>     <td>current_city</td>     <td>string</td>     <td></td>          <td>City in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_district</td>     <td>string</td>     <td></td>          <td>District in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>current_state</td>     <td>string</td>     <td></td>          <td>State in which CoApplicant is currently residing</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>current_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_current_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>rented</td>  </tr>        <tr>     <td>years_of_stay_in_current_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the current address</td>       <td>5</td>  </tr>        <tr>     <td>permanent_address</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>2, Mount Road, Teynampet</td>  </tr>        <tr>     <td>permanent_city</td>     <td>string</td>     <td></td>          <td>City in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_district</td>     <td>string</td>     <td></td>          <td>District in which CoApplicant is currently residing</td>       <td>Chennai</td>  </tr>        <tr>     <td>permanent_state</td>     <td>string</td>     <td></td>          <td>State in which CoApplicant is currently residing</td>       <td>tamil_nadu</td>  </tr>        <tr>     <td>permanent_pincode</td>     <td>integer</td>     <td></td>          <td>Pincode of the current address</td>       <td>600089</td>  </tr>        <tr>     <td>residence_type_permanent_address</td>     <td>string</td>     <td></td>          <td>rented / owned / leased</td>       <td>owned</td>  </tr>        <tr>     <td>years_of_stay_in_permanent_address</td>     <td>integer</td>     <td></td>          <td>How many years stayed in the permanent address</td>       <td>5</td>  </tr>        <tr>     <td>marital_status</td>     <td>string</td>     <td></td>          <td>Married / Unmarried</td>       <td>unmarried</td>  </tr>        <tr>     <td>religion</td>     <td>string</td>     <td></td>          <td>Religion of the CoApplicant</td>       <td>buddhist</td>  </tr>        <tr>     <td>nationality</td>     <td>string</td>     <td></td>          <td>Nationality of the CoApplicant</td>       <td>indian</td>  </tr>        <tr>     <td>father_name</td>     <td>string</td>     <td></td>          <td>Father Name of the CoApplicant</td>       <td>Dan Kato</td>  </tr>        <tr>     <td>mother_name</td>     <td>string</td>     <td></td>          <td>Mother Name of the CoApplicant</td>       <td>Tsunade Senju</td>  </tr>        <tr>     <td>spouse_name</td>     <td>string</td>     <td></td>          <td>Spouse Name of the CoApplicant</td>       <td>Kushina Uzumaki</td>  </tr>        <tr>     <td>education</td>     <td>string</td>     <td></td>          <td>Free flowing text</td>       <td>Hokage</td>  </tr>        <tr>     <td>annual_income</td>     <td>number</td>     <td>float</td>          <td>Annual Income of the CoApplicant (in Rupees)</td>       <td>120000.0</td>  </tr>        <tr>     <td>income_proof_link</td>     <td>array</td>     <td></td>          <td>CoApplicant Income Proof Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bank_statement_12_months_link</td>     <td>array</td>     <td></td>          <td>CoApplicant Bank Statement Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>pan_number</td>     <td>string</td>     <td></td>          <td>PAN Number of the CoApplicant (10 digit Alphanumeric)</td>       <td>BMMPG9018Y</td>  </tr>        <tr>     <td>pan_link</td>     <td>array</td>     <td></td>          <td>PAN Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>aadhar_number</td>     <td>string</td>     <td></td>          <td>Aadhar Number of the CoApplicant (12 digits)</td>       <td>794065346725</td>  </tr>        <tr>     <td>aadhar_link</td>     <td>array</td>     <td></td>          <td>Aadhar Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>voter_id_number</td>     <td>string</td>     <td></td>          <td>Voter ID Number of the CoApplicant</td>       <td>RTG2291234</td>  </tr>        <tr>     <td>voting_id_link</td>     <td>array</td>     <td></td>          <td>Voter Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>driving_license_number</td>     <td>string</td>     <td></td>          <td>Driving License Number of the CoApplicant</td>       <td>TN01123345</td>  </tr>        <tr>     <td>driving_license_link</td>     <td>array</td>     <td></td>          <td>Driving License Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>passport_number</td>     <td>string</td>     <td></td>          <td>Passport Number of the CoApplicant</td>       <td>L4018345</td>  </tr>        <tr>     <td>passport_link</td>     <td>array</td>     <td></td>          <td>Passport Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_kyc_link</td>     <td>array</td>     <td></td>          <td>Video KYC of the CoApplicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>video_kyc_profile_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Profile ID of the case as per the video KYC vendor</td>       <td>ABC12345</td>  </tr>        <tr>     <td>video_kyc_account_id</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Account ID of the case as per the video KYC vendor</td>       <td>ABC12345</td>  </tr>        <tr>     <td>video_kyc_key</td>     <td>string</td>     <td></td>          <td>Required if video KYC is done. Key as per the video KYC vendor</td>       <td>abc_123</td>  </tr>        <tr>     <td>other_kyc_number</td>     <td>string</td>     <td></td>          <td>KYC Number of the CoApplicant</td>       <td>ABC12456</td>  </tr>        <tr>     <td>other_kyc_link</td>     <td>array</td>     <td></td>          <td>KYC Image of the CoApplicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>rent_agreement_link</td>     <td>array</td>     <td></td>          <td>CoApplicant Rent Agreement Document Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>utility_bills_link</td>     <td>array</td>     <td></td>          <td>Utility Bills Copies (If any)</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>photo_link</td>     <td>array</td>     <td></td>          <td>Photo Image of the CoApplicant</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>bureau_score</td>     <td>integer</td>     <td></td>          <td>Bureau Score of the CoApplicant</td>       <td>700</td>  </tr>        <tr>     <td>bureau_report_link</td>     <td>array</td>     <td></td>          <td>CoApplicant&#39;s Bureau Report Link</td>       <td>[&quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;, &quot;https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg&quot;]</td>  </tr>        <tr>     <td>partner_score</td>     <td>integer</td>     <td></td>          <td>Score Captured by the Partner</td>       <td>3</td>  </tr>    </tbody>       </table>   <h4>InsuranceDetails</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>insurance_type</td>     <td>string</td>     <td></td>          <td>Enter &#39;credit&#39;</td>       <td>credit</td>  </tr>        <tr>     <td>insurer_name</td>     <td>string</td>     <td></td>          <td>Loan Insurer Name</td>       <td>Tata AIG</td>  </tr>        <tr>     <td>nominee_details</td>     <td>string</td>     <td></td>          <td>Applicable if Credit Shield insurance is taken. Name of the nominee to be provided</td>       <td>Neeraj</td>  </tr>        <tr>     <td>relationship</td>     <td>string</td>     <td></td>          <td>Applicable if Credit Shield insurance is taken. Relationship of nominee to be provided</td>       <td>friend</td>  </tr>        <tr>     <td>premium</td>     <td>number</td>     <td>float</td>          <td>Applicable if Credit Shield insurance is taken. Premium amount</td>       <td>100000.0</td>  </tr>        <tr>     <td>insurance_amount</td>     <td>number</td>     <td>float</td>          <td>Applicable if Credit Shield insurance is taken. Total insurance amount</td>       <td>300000.0</td>  </tr>        <tr>     <td>policy_number</td>     <td>string</td>     <td></td>          <td>Applicable if Credit Shield insurance is taken. Policy number</td>       <td>ABC12345</td>  </tr>    </tbody>       </table>   <h4>References</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>name</td>     <td>string</td>     <td></td>          <td>Name of reference</td>       <td>Neeraj Chopra</td>  </tr>        <tr>     <td>address</td>     <td>string</td>     <td></td>          <td>Address details of reference</td>       <td>221B, Baker Street, Chennai</td>  </tr>        <tr>     <td>pincode</td>     <td>string</td>     <td></td>          <td>Pincode of reference address</td>       <td>600001</td>  </tr>        <tr>     <td>phone</td>     <td>string</td>     <td></td>          <td>Phone number of reference</td>       <td>9876543210</td>  </tr>    </tbody>       </table>    #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table>    INDIAN STATES  - jammu_kashmir - himachal_pradesh - punjab - chandigarh - uttaranchal - haryana - delhi - rajasthan - uttar_pradesh - bihar - sikkim - arunachal_pradesh - nagaland - manipur - mizoram - tripura - meghalaya - assam - west_bengal - jharkhand - orissa - chhattisgarh - madhya_pradesh - gujarat - daman_diu - dadra_nagar_haveli - maharashtra - andhra_pradesh - karnataka - goa - lakshadweep - kerala - tamil_nadu - pondicherry - andaman_nicobar_islands - telangana


### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.request_success import RequestSuccess
from credavenue_colending.model.body_update_post_disbursement import BodyUpdatePostDisbursement
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_update_post_disbursement = BodyUpdatePostDisbursement(
        customer_type="customer_type_example",
        customer_category="customer_category_example",
        first_name="first_name_example",
        middle_name="middle_name_example",
        last_name="last_name_example",
        gender="gender_example",
        date_of_birth=dateutil_parser('1970-01-01').date(),
        age=1,
        mobile_number=1,
        email="email_example",
        official_email_id="official_email_id_example",
        current_address="current_address_example",
        current_city="current_city_example",
        current_district="current_district_example",
        current_state="current_state_example",
        current_pincode=1,
        residence_type_current_address="residence_type_current_address_example",
        years_of_stay_in_current_address=1,
        permanent_address="permanent_address_example",
        permanent_city="permanent_city_example",
        permanent_district="permanent_district_example",
        permanent_state="permanent_state_example",
        permanent_pincode=1,
        residence_type_permanent_address="residence_type_permanent_address_example",
        years_of_stay_in_permanent_address=1,
        marital_status="marital_status_example",
        religion="religion_example",
        nationality="nationality_example",
        father_name="father_name_example",
        mother_name="mother_name_example",
        spouse_name="spouse_name_example",
        education_qualification="education_qualification_example",
        net_monthly_income=3.14,
        annual_income=3.14,
        no_of_dependants=1,
        occupation="occupation_example",
        pan_number="pan_number_example",
        pan_number_link=[
            "pan_number_link_example",
        ],
        form_60_link=[
            "form_60_link_example",
        ],
        aadhar_number="aadhar_number_example",
        aadhar_link=[
            "aadhar_link_example",
        ],
        voter_id_number="voter_id_number_example",
        voting_id_link=[
            "voting_id_link_example",
        ],
        driving_license_number="driving_license_number_example",
        driving_license_link=[
            "driving_license_link_example",
        ],
        passport_number="passport_number_example",
        passport_link=[
            "passport_link_example",
        ],
        video_image_link=[
            "video_image_link_example",
        ],
        video_kyc_detail=BodyUpdatePostDisbursementVideoKycDetail(
            profile_id="profile_id_example",
            account_id="account_id_example",
            key="key_example",
        ),
        other_kyc_number="other_kyc_number_example",
        other_kyc_link=[
            "other_kyc_link_example",
        ],
        rent_agreement_link=[
            "rent_agreement_link_example",
        ],
        utility_bills_link=[
            "utility_bills_link_example",
        ],
        photo_link=[
            "photo_link_example",
        ],
        employment_type="employment_type_example",
        employment_details_name="employment_details_name_example",
        employment_details_address="employment_details_address_example",
        employment_details_years_of_experience=3.14,
        employment_details_designation="employment_details_designation_example",
        employement_vintage_current_organisation=1,
        payslip_link=[
            "payslip_link_example",
        ],
        tds_certificate_link=[
            "tds_certificate_link_example",
        ],
        name_of_bureau="name_of_bureau_example",
        bureau_vintage=1,
        bureau_score=1,
        bureau_report_link=[
            "bureau_report_link_example",
        ],
        commercial_bureau_score=1,
        commercial_bureau_score_link=[
            "commercial_bureau_score_link_example",
        ],
        partner_score_on_the_customer=3.14,
        total_existing_obligations=1,
        credit_card_limit=1,
        number_of_credit_cards=1,
        number_of_unsecured_loans=1,
        value_of_total_unsecured_loans=3.14,
        number_of_loans=1,
        value_of_total_loans=3.14,
        number_of_enquiries_3months=1,
        number_of_enquiries_6months=1,
        number_of_enquiries_12months=1,
        number_of_writeoff_suitfiled_settled_12months=1,
        max_dpd_tradeline_12months=1,
        max_overdue_tradeline=1,
        total_overdue_amount_12months=3.14,
        loan_amount_settled_12months=3.14,
        nature_of_loan_settled1="nature_of_loan_settled1_example",
        nature_of_loan_settled2="nature_of_loan_settled2_example",
        total_emi_bounces=1,
        emi_bounces_6months=1,
        emi_bounces_12months=1,
        bank_statement=BodyUpdatePostDisbursementBankStatement(
            bank_statement_savings_account_12_months_link=[
                "bank_statement_savings_account_12_months_link_example",
            ],
            bank_statement_current_account_12_months_link=[
                "bank_statement_current_account_12_months_link_example",
            ],
            no_of_inward_chq_returns_savings_account=1,
            no_of_outward_chq_returns_savings_account=1,
            no_of_inward_chq_returns_current_account=1,
            no_of_outward_chq_returns_current_account=1,
            bank_account_type_for_assessment="bank_account_type_for_assessment_example",
            perfios_link="perfios_link_example",
            finbit_link="finbit_link_example",
            abb=3.14,
            abd=3.14,
        ),
        financial_data=BodyUpdatePostDisbursementFinancialData(
            annual_business_turnover=3.14,
            annual_gross_profit=3.14,
            annual_business_ebitda=3.14,
            monthly_net_profit=3.14,
            annual_net_profit=3.14,
            gst_return_year_1_link=[
                "gst_return_year_1_link_example",
            ],
            gst_return_year_2_link=[
                "gst_return_year_2_link_example",
            ],
            gst_return_year_3_link=[
                "gst_return_year_3_link_example",
            ],
            it_return_year_1_link=[
                "it_return_year_1_link_example",
            ],
            it_return_year_2_link=[
                "it_return_year_2_link_example",
            ],
            it_return_year_3_link=[
                "it_return_year_3_link_example",
            ],
            other_income_assessment_proof_link=[
                "other_income_assessment_proof_link_example",
            ],
            cam_link=[
                "cam_link_example",
            ],
            cfa_link=[
                "cfa_link_example",
            ],
        ),
        co_applicants=[
            BodyUpdatePostDisbursementCoApplicants(
                relationship_with_applicant="relationship_with_applicant_example",
                first_name="first_name_example",
                middle_name="middle_name_example",
                last_name="last_name_example",
                gender="gender_example",
                date_of_birth=dateutil_parser('1970-01-01').date(),
                age=1,
                mobile_number=1,
                email="email_example",
                current_address="current_address_example",
                current_city="current_city_example",
                current_district="current_district_example",
                current_state="current_state_example",
                current_pincode=1,
                residence_type_current_address="residence_type_current_address_example",
                years_of_stay_in_current_address=1,
                permanent_address="permanent_address_example",
                permanent_city="permanent_city_example",
                permanent_district="permanent_district_example",
                permanent_state="permanent_state_example",
                permanent_pincode=1,
                residence_type_permanent_address="residence_type_permanent_address_example",
                years_of_stay_in_permanent_address=1,
                marital_status="marital_status_example",
                religion="religion_example",
                nationality="nationality_example",
                father_name="father_name_example",
                mother_name="mother_name_example",
                spouse_name="spouse_name_example",
                education="education_example",
                annual_income=3.14,
                income_proof_link=[
                    "income_proof_link_example",
                ],
                bank_statement_12_months_link=[
                    "bank_statement_12_months_link_example",
                ],
                pan_number="pan_number_example",
                pan_link=[
                    "pan_link_example",
                ],
                aadhar_number="aadhar_number_example",
                aadhar_link=[
                    "aadhar_link_example",
                ],
                voter_id_number="voter_id_number_example",
                voting_id_link=[
                    "voting_id_link_example",
                ],
                driving_license_number="driving_license_number_example",
                driving_license_link=[
                    "driving_license_link_example",
                ],
                passport_number="passport_number_example",
                passport_link=[
                    "passport_link_example",
                ],
                video_kyc_link=[
                    "video_kyc_link_example",
                ],
                video_kyc_profile_id="video_kyc_profile_id_example",
                video_kyc_account_id="video_kyc_account_id_example",
                video_kyc_key="video_kyc_key_example",
                other_kyc_number="other_kyc_number_example",
                other_kyc_link=[
                    "other_kyc_link_example",
                ],
                rent_agreement_link=[
                    "rent_agreement_link_example",
                ],
                utility_bills_link=[
                    "utility_bills_link_example",
                ],
                photo_link=[
                    "photo_link_example",
                ],
                bureau_score=1,
                bureau_report_link=[
                    "bureau_report_link_example",
                ],
                partner_score=1,
            ),
        ],
        abb_emi_ratio=3.14,
        dscr=3.14,
        foir=3.14,
        ltr=3.14,
        eligibility_loan_amount=3.14,
        insurance_details=[
            BodyUpdatePostDisbursementInsuranceDetails(
                insurance_type="insurance_type_example",
                insurer_name="insurer_name_example",
                nominee_details="nominee_details_example",
                relationship="relationship_example",
                premium=3.14,
                insurance_amount=3.14,
                policy_number="policy_number_example",
            ),
        ],
        references=[
            BodyCreateLoanReferences(
                name="name_example",
                address="address_example",
                pincode="pincode_example",
                phone="phone_example",
            ),
        ],
        psl_flag="psl_flag_example",
        psl_description="psl_description_example",
        psl_code="psl_code_example",
        psl_proof_link=[
            "psl_proof_link_example",
        ],
        loan_agreement_link=[
            "loan_agreement_link_example",
        ],
        sanction_letter_link=[
            "sanction_letter_link_example",
        ],
        laf_link=[
            "laf_link_example",
        ],
        self_declaration_letter_link=[
            "self_declaration_letter_link_example",
        ],
        authorisation_letter_link=[
            "authorisation_letter_link_example",
        ],
        enach_pdc_link=[
            "enach_pdc_link_example",
        ],
        guarantor_agreements_link=[
            "guarantor_agreements_link_example",
        ],
    ) # BodyUpdatePostDisbursement | 

    # example passing only required values which don't have defaults set
    try:
        # #Update Post Disbursement
        api_response = api_instance.update_post_disbursement(product_id, client_name, loan_id, body_update_post_disbursement)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->update_post_disbursement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_update_post_disbursement** | [**BodyUpdatePostDisbursement**](BodyUpdatePostDisbursement.md)|  |

### Return type

[**RequestSuccess**](RequestSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repayment_schedule**
> GetRSSuccess update_repayment_schedule(product_id, client_name, loan_id, body_update_repayment_schedule)

#Update Repayment Schedule

Update Repayment Schedule API - This endpoint can be used to update the repayment schedules.

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>repayment_schedules</td>     <td>array</td>     <td></td>          <td>Refer table RepaymentSchedules for attributes</td>       <td>[{&quot;installment_no&quot;:1,&quot;due_date&quot;:&quot;2021-01-01&quot;,&quot;principal&quot;:10000.0,&quot;interest&quot;:100.0,&quot;amount&quot;:10200.0,&quot;pos&quot;:100000.0,&quot;other_charges&quot;:100.0},{&quot;installment_no&quot;:1,&quot;due_date&quot;:&quot;2021-01-01&quot;,&quot;principal&quot;:10000.0,&quot;interest&quot;:100.0,&quot;amount&quot;:10200.0,&quot;pos&quot;:100000.0,&quot;other_charges&quot;:100.0}]</td>  </tr>    </tbody>       </table>   <h4>RepaymentSchedules</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>installment_no</td>     <td>integer</td>     <td></td>          <td>Installment Number</td>       <td>1</td>  </tr>        <tr>     <td>due_date</td>     <td>string</td>     <td>date</td>          <td>Installment Due Date (YYYY-MM-DD)</td>       <td>2021-01-01</td>  </tr>        <tr>     <td>principal</td>     <td>number</td>     <td>float</td>          <td>Principal to be paid in the installment</td>       <td>10000.0</td>  </tr>        <tr>     <td>interest</td>     <td>number</td>     <td>float</td>          <td>Interest to be paid in the installment</td>       <td>100.0</td>  </tr>        <tr>     <td>amount</td>     <td>number</td>     <td>float</td>          <td>Total EMI amount</td>       <td>10200.0</td>  </tr>        <tr>     <td>pos</td>     <td>number</td>     <td>float</td>          <td>Closing principal outstanding</td>       <td>100000.0</td>  </tr>        <tr>     <td>other_charges</td>     <td>number</td>     <td>float</td>          <td>Other Charges</td>       <td>100.0</td>  </tr>    </tbody>       </table>     #Response Codes</h4>  <table>   <thead>     <tr>       <th>Code</th>       <th>Message</th>       <th>Reason</th>    </tr>   </thead>   <tbody>      <tr>     <td>204</td>     <td>No content</td>     <td>Success</td>   </tr>    </tbody>    <tbody>      <tr>     <td>400</td>     <td>Bad Request</td>     <td>Failed due to invalid Request Format /  Missing Required Parameters /  Loan is in invalid state</td>   </tr>    </tbody>   <tbody>      <tr>     <td>404</td>     <td>Not Found</td>     <td>Loan Not Found</td>   </tr>    </tbody>  </tbody>   <tbody>      <tr>     <td>401</td>     <td>Unauthorized</td>     <td>Invalid API Key</td>   </tr>    </tbody>  <tbody>      <tr>     <td>500</td>     <td>Internal Server Error</td>     <td>Error occurred in the backend</td>   </tr>    </tbody>   </table> 

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.get_rs_success import GetRSSuccess
from credavenue_colending.model.body_update_repayment_schedule import BodyUpdateRepaymentSchedule
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_update_repayment_schedule = BodyUpdateRepaymentSchedule(
        repayment_schedules=[
            BodyUpdateRepaymentScheduleRepaymentSchedules(
                installment_no=1,
                due_date=dateutil_parser('1970-01-01').date(),
                principal=3.14,
                interest=3.14,
                amount=3.14,
                pos=3.14,
                other_charges=3.14,
            ),
        ],
    ) # BodyUpdateRepaymentSchedule | 

    # example passing only required values which don't have defaults set
    try:
        # #Update Repayment Schedule
        api_response = api_instance.update_repayment_schedule(product_id, client_name, loan_id, body_update_repayment_schedule)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->update_repayment_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_update_repayment_schedule** | [**BodyUpdateRepaymentSchedule**](BodyUpdateRepaymentSchedule.md)|  |

### Return type

[**GetRSSuccess**](GetRSSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_interest_accruals**
> RequestSuccess upload_interest_accruals(product_id, client_name, loan_id, body_upload_interest_accruals)

#Upload Interest Accruals

Upload Interest Accruals API

<h4>Request Parameters</h4>  <table>   <thead>     <tr>       <th>Field</th>       <th>Type</th>       <th>Format</th>              <th>Description</th>       <th>Example</th>     </tr>   </thead>   <tbody>      <tr>     <td>file_link</td>     <td>string</td>     <td></td>          <td>Interest Accrual File URL</td>       <td>https://cdn.pixabay.com/photo/2017/06/22/20/22/green-2432374_1280.jpg </td>  </tr>        <tr>     <td>file_link_password</td>     <td>string</td>     <td></td>          <td>Interest Accrual File URL</td>       <td>12345678</td>  </tr>    </tbody>       </table>

### Example

* Api Key Authentication (api_key):

```python
import time
import credavenue_colending
from credavenue_colending.api import colending_api
from credavenue_colending.model.body_upload_interest_accruals import BodyUploadInterestAccruals
from credavenue_colending.model.unauthorized import Unauthorized
from credavenue_colending.model.internal_server_error import InternalServerError
from credavenue_colending.model.not_found import NotFound
from credavenue_colending.model.bad_request import BadRequest
from credavenue_colending.model.request_success import RequestSuccess
from pprint import pprint
# Defining the host is optional and defaults to https://colend-uat-01-api.credavenue.in/colending
# See configuration.py for a list of all supported configuration parameters.
configuration = credavenue_colending.Configuration(
    host = "https://colend-uat-01-api.credavenue.in/colending"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with credavenue_colending.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colending_api.ColendingApi(api_client)
    product_id = "XYZ_001" # str | Product Code given by CoLending
    client_name = "allcloud" # str | Name of the client
    loan_id = "AB001" # str | Client Loan ID as provided during loan creation
    body_upload_interest_accruals = BodyUploadInterestAccruals(
        file_link="file_link_example",
        file_link_password="file_link_password_example",
    ) # BodyUploadInterestAccruals | 

    # example passing only required values which don't have defaults set
    try:
        # #Upload Interest Accruals
        api_response = api_instance.upload_interest_accruals(product_id, client_name, loan_id, body_upload_interest_accruals)
        pprint(api_response)
    except credavenue_colending.ApiException as e:
        print("Exception when calling ColendingApi->upload_interest_accruals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product Code given by CoLending |
 **client_name** | **str**| Name of the client |
 **loan_id** | **str**| Client Loan ID as provided during loan creation |
 **body_upload_interest_accruals** | [**BodyUploadInterestAccruals**](BodyUploadInterestAccruals.md)|  |

### Return type

[**RequestSuccess**](RequestSuccess.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | 500 Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

