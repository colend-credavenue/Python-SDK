"""
    Allcloud (Allcloud)

    # Integration Document  The following are the endpoints to be called during and pre/post disbursement state of a loan.  ## Authentication  Authentication details and host will be shared privately.  ## Workflow  **Create Loan** is the initial endpoint to be called to create a loan. Loan will be processed in the background and the status of loan will be provided through the configured Webhook. However, the client can also poll the server via the **Get Loan Details** endpoint to know the loan's status(**Get Loan Details** is rate throttled and polling this API will be restricted). Loan's shall be considered rejected if proper response is not available within 10minutes.  All other endpoints are self-explanatory and can be retried upto 3 times before marking as failure.  ## Allowed Links  All Link attributes should contain 1. Accessible File Link URL which can be Public/Expiry URL/Whitelisted File Server Link(Write to tech.colending@credavenue.com for obtaining our IP address to whitelist) 2. File Link URL with Header Authentication (Header values should be shared with tech.colending@credavenue.com)  ## Allowed Fields Length <table border=\"2\" cellspacing=\"0\" cellpadding=\"6\" rules=\"groups\" frame=\"hsides\">  <colgroup>  <col  class=\"org-left\" />  <col  class=\"org-left\" />  </colgroup> <thead> <tr> <th scope=\"col\" class=\"org-left\">Data Type</th> <th scope=\"col\" class=\"org-left\">Max Length</th> </tr> </thead>  <tbody> <tr> <td class=\"org-left\">String</td> <td class=\"org-left\">65,535 bytes</td> </tr>  <tr> <td class=\"org-left\">Float</td> <td class=\"org-left\">8 bytes</td> </tr>  <tr> <td class=\"org-left\">Integer</td> <td class=\"org-left\">4 bytes</td> </tr>  <tr> <td class=\"org-left\">Date</td> <td class=\"org-left\">10 characters</td> </tr>  </tbody> </table>  # Webhooks  Webhooks can be configured for the below events  1. Loan status change      Response Payload :      {         \"product_id\": \"\",         \"client_loan_id\": \"\",         \"principal_amount\": \"\",         \"interest_rate\": \"\",         \"tenure\": \"\",         \"tenure_frequency\": \"MONTHLY\",         \"cibil_score\": \"\",         \"purpose\": \"\",         \"repayment_frequency\":\"\",         \"number_of_repayments\": \"\",         \"status\": \"\",         \"principal_outstanding\": \"\",         \"reject_reason\": \"\"     }          Statuses : ['new', 'approved', 'rejected', 'agreement_signed', 'dropped', 'disbursement_ready', 'disbursed', 'matured', 'partner_settled']     2. Loan disbursement details (Disbursed through razorpay)      Callback Payload:      {         \"client_loan_id\":\"\",         \"status\":\"borrower_disbursed\",         \"disbursed_date\":\"\",         \"utr_number\":\"\",         \"disbursement_type\":\"\",         \"payment_reversed\": \"TRUE/FALSE\",         \"disbursement_amount\":\"\",         \"investor_disbursed_amount\": \"\",         \"partner_disbursed_amount\": \"\",         \"differential_interest\":\"\",         \"investor_differential_interest\":\"\",         \"partner_differential_interest\":\"\",         \"differential_days\":\"\",         \"interest_start_date\":\"\",         \"investor_processing_fee\":\"\",         \"partner_processing_fee\":\"\",         \"investor_stamp_duty\":\"\",         \"partner_stamp_duty\":\"\",         \"investor_documentation_charges\":\"\",         \"partner_documentation_charges\":\"\"     }  Provide the following details to configure the webhooks 1. callback URL 2. authentication for the callback URL (header authentication)    # Validations  **PAN**  - **Example**: ABGPA1232P - **Sequence**: First five digits will be alpha, next four will be Numerical and again last single digit will be alpha  **GSTIN**  - **Example**: 33AAACT2727Q1ZV - **Sequence**: First two digits is Numerical, Next is PAN sequence as specified above, again thirteenth digit will be numerical, fourteenth digit is alpha, last digit will be alpha or numerical  **CIN**  - **Example**: U65929TN2017PTC117196 - **Sequence**: First digit is Alpha, next 5 numeric digits, next two alpha, next set of 4 numeric digits, Next 3 alpha, last 6 numeric digits  **PASSPORT**  - **Example**: A2096457 - **Sequence**: Total 8 digits, first digit is Alpha, remaining digits are numerical  **AADHAR NO**  - The standard 12 digits numerical.  **MOBILE NO**  - **Sequence**: 10 numerical digits  **IFSC CODE**  - **Example**: PUNB0596600 - **Sequence**: First four alpha, next fifth digit is 0 (zero) always and last six digit is alpha/numeric. Totally 11 digits.  **PIN CODE**  - 6 numerical digits  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@colending.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from credavenue_colending.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from credavenue_colending.exceptions import ApiAttributeError



class ResponseCreateTrancheBureauReportData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'name_of_bureau': (str,),  # noqa: E501
            'bureau_vintage': (int,),  # noqa: E501
            'bureau_score': (int,),  # noqa: E501
            'bureau_report_link': ([str],),  # noqa: E501
            'bureau_report_link_password': (str,),  # noqa: E501
            'bureau_json_link': ([str],),  # noqa: E501
            'bureau_json_link_password': (str,),  # noqa: E501
            'bureau_json': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),  # noqa: E501
            'commercial_bureau_score': (int,),  # noqa: E501
            'commercial_bureau_score_link': ([str],),  # noqa: E501
            'commercial_bureau_score_link_password': (str,),  # noqa: E501
            'partner_score_on_the_customer': (int,),  # noqa: E501
            'total_existing_obligations': (int,),  # noqa: E501
            'credit_card_limit': (int,),  # noqa: E501
            'number_of_credit_cards': (int,),  # noqa: E501
            'number_of_unsecured_loans': (int,),  # noqa: E501
            'value_of_total_unsecured_loans': (float,),  # noqa: E501
            'number_of_loans': (int,),  # noqa: E501
            'value_of_total_loans': (float,),  # noqa: E501
            'number_of_enquiries_3months': (int,),  # noqa: E501
            'number_of_enquiries_6months': (int,),  # noqa: E501
            'number_of_enquiries_12months': (int,),  # noqa: E501
            'number_of_writeoff_suitfiled_settled_12months': (int,),  # noqa: E501
            'max_dpd_tradeline_12months': (int,),  # noqa: E501
            'max_dpd_tradeline_last_6months': (int,),  # noqa: E501
            'max_dpd_tradeline_last_3months': (int,),  # noqa: E501
            'number_of_pl_enquiries_in_last_30days': (int,),  # noqa: E501
            'value_of_total_outstanding_loans': (float,),  # noqa: E501
            'max_overdue_tradeline': (int,),  # noqa: E501
            'total_overdue_amount_12months': (float,),  # noqa: E501
            'loan_amount_settled_12months': (float,),  # noqa: E501
            'nature_of_loan_settled1': (str,),  # noqa: E501
            'nature_of_loan_settled2': (str,),  # noqa: E501
            'total_emi_bounces': (int,),  # noqa: E501
            'emi_bounces_6months': (int,),  # noqa: E501
            'emi_bounces_12months': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name_of_bureau': 'name_of_bureau',  # noqa: E501
        'bureau_vintage': 'bureau_vintage',  # noqa: E501
        'bureau_score': 'bureau_score',  # noqa: E501
        'bureau_report_link': 'bureau_report_link',  # noqa: E501
        'bureau_report_link_password': 'bureau_report_link_password',  # noqa: E501
        'bureau_json_link': 'bureau_json_link',  # noqa: E501
        'bureau_json_link_password': 'bureau_json_link_password',  # noqa: E501
        'bureau_json': 'bureau_json',  # noqa: E501
        'commercial_bureau_score': 'commercial_bureau_score',  # noqa: E501
        'commercial_bureau_score_link': 'commercial_bureau_score_link',  # noqa: E501
        'commercial_bureau_score_link_password': 'commercial_bureau_score_link_password',  # noqa: E501
        'partner_score_on_the_customer': 'partner_score_on_the_customer',  # noqa: E501
        'total_existing_obligations': 'total_existing_obligations',  # noqa: E501
        'credit_card_limit': 'credit_card_limit',  # noqa: E501
        'number_of_credit_cards': 'number_of_credit_cards',  # noqa: E501
        'number_of_unsecured_loans': 'number_of_unsecured_loans',  # noqa: E501
        'value_of_total_unsecured_loans': 'value_of_total_unsecured_loans',  # noqa: E501
        'number_of_loans': 'number_of_loans',  # noqa: E501
        'value_of_total_loans': 'value_of_total_loans',  # noqa: E501
        'number_of_enquiries_3months': 'number_of_enquiries_3months',  # noqa: E501
        'number_of_enquiries_6months': 'number_of_enquiries_6months',  # noqa: E501
        'number_of_enquiries_12months': 'number_of_enquiries_12months',  # noqa: E501
        'number_of_writeoff_suitfiled_settled_12months': 'number_of_writeoff_suitfiled_settled_12months',  # noqa: E501
        'max_dpd_tradeline_12months': 'max_dpd_tradeline_12months',  # noqa: E501
        'max_dpd_tradeline_last_6months': 'max_dpd_tradeline_last_6months',  # noqa: E501
        'max_dpd_tradeline_last_3months': 'max_dpd_tradeline_last_3months',  # noqa: E501
        'number_of_pl_enquiries_in_last_30days': 'number_of_pl_enquiries_in_last_30days',  # noqa: E501
        'value_of_total_outstanding_loans': 'value_of_total_outstanding_loans',  # noqa: E501
        'max_overdue_tradeline': 'max_overdue_tradeline',  # noqa: E501
        'total_overdue_amount_12months': 'total_overdue_amount_12months',  # noqa: E501
        'loan_amount_settled_12months': 'loan_amount_settled_12months',  # noqa: E501
        'nature_of_loan_settled1': 'nature_of_loan_settled1',  # noqa: E501
        'nature_of_loan_settled2': 'nature_of_loan_settled2',  # noqa: E501
        'total_emi_bounces': 'total_emi_bounces',  # noqa: E501
        'emi_bounces_6months': 'emi_bounces_6months',  # noqa: E501
        'emi_bounces_12months': 'emi_bounces_12months',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ResponseCreateTrancheBureauReportData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name_of_bureau (str): Cibil / Experian / Himark. [optional]  # noqa: E501
            bureau_vintage (int): Vintage in the bureau. Number of years from the first trade line. [optional]  # noqa: E501
            bureau_score (int): Bureau Score. [optional]  # noqa: E501
            bureau_report_link ([str]): Document of the bureau. [optional]  # noqa: E501
            bureau_report_link_password (str): Document of the bureau - Password. [optional]  # noqa: E501
            bureau_json_link ([str]): Bureau Json placed in a link. [optional]  # noqa: E501
            bureau_json_link_password (str): Bureau Json placed in a link - Password. [optional]  # noqa: E501
            bureau_json ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Refer table BureauJson for attributes. [optional]  # noqa: E501
            commercial_bureau_score (int): CRIF score. [optional]  # noqa: E501
            commercial_bureau_score_link ([str]): Commercial Bureau Document. [optional]  # noqa: E501
            commercial_bureau_score_link_password (str): Commercial Bureau Document Password. [optional]  # noqa: E501
            partner_score_on_the_customer (int): Score Captured by the Partner. [optional]  # noqa: E501
            total_existing_obligations (int): Total Existing Obligations basis the Bureau Report. [optional]  # noqa: E501
            credit_card_limit (int): Total Credit Card Limit basis the Bureau Report. [optional]  # noqa: E501
            number_of_credit_cards (int): Total Number of Credit Cards per Bureau Report. [optional]  # noqa: E501
            number_of_unsecured_loans (int): Total Number of Unsecured Loans per Bureau Report. [optional]  # noqa: E501
            value_of_total_unsecured_loans (float): Total value of unsecured loans. [optional]  # noqa: E501
            number_of_loans (int): Total Number of Loans per Bureau Report. [optional]  # noqa: E501
            value_of_total_loans (float): Total value of loans. [optional]  # noqa: E501
            number_of_enquiries_3months (int): Number of Enquiries in the Last 3 Months per Bureau Report. [optional]  # noqa: E501
            number_of_enquiries_6months (int): Number of Enquiries in the Last 6 Months per Bureau Report. [optional]  # noqa: E501
            number_of_enquiries_12months (int): Number of Enquiries in the Last 12 Months per Bureau Report. [optional]  # noqa: E501
            number_of_writeoff_suitfiled_settled_12months (int): Number of Writeoff Suitfiled Settled in the Last 12 Months. [optional]  # noqa: E501
            max_dpd_tradeline_12months (int): Maximum DPD Tradeline in the Last 12 Months. [optional]  # noqa: E501
            max_dpd_tradeline_last_6months (int): Maximum DPD Tradeline in the Last 6 Months. [optional]  # noqa: E501
            max_dpd_tradeline_last_3months (int): Maximum DPD Tradeline in the Last 3 Months. [optional]  # noqa: E501
            number_of_pl_enquiries_in_last_30days (int): Number of Pl enquires in the Last 12 Months [optional]  # noqa: E501
            value_of_total_outstanding_loans (float): Value of total outstanding loan in the Last 12 Months [optional]  # noqa: E501
            max_overdue_tradeline (int): Maximum Overdue Tradeline. [optional]  # noqa: E501
            total_overdue_amount_12months (float): Total Overdue Amount in the Last 12 Months. [optional]  # noqa: E501
            loan_amount_settled_12months (float): Loan Amount Settled in the Last 12 Months. [optional]  # noqa: E501
            nature_of_loan_settled1 (str): The nature of past loan settlement if any (Loan 1) - Settled/ Closed/ Written-off. [optional]  # noqa: E501
            nature_of_loan_settled2 (str): The nature of past loan settlement if any (Loan 2) - Settled/ Closed/ Written-off. [optional]  # noqa: E501
            total_emi_bounces (int): Total EMI Bounces. [optional]  # noqa: E501
            emi_bounces_6months (int): EMI Bounces in the Last 6 Months. [optional]  # noqa: E501
            emi_bounces_12months (int): EMI Bounces in the Last 12 Months. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ResponseCreateTrancheBureauReportData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name_of_bureau (str): Cibil / Experian / Himark. [optional]  # noqa: E501
            bureau_vintage (int): Vintage in the bureau. Number of years from the first trade line. [optional]  # noqa: E501
            bureau_score (int): Bureau Score. [optional]  # noqa: E501
            bureau_report_link ([str]): Document of the bureau. [optional]  # noqa: E501
            bureau_report_link_password (str): Document of the bureau - Password. [optional]  # noqa: E501
            bureau_json_link ([str]): Bureau Json placed in a link. [optional]  # noqa: E501
            bureau_json_link_password (str): Bureau Json placed in a link - Password. [optional]  # noqa: E501
            bureau_json ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Refer table BureauJson for attributes. [optional]  # noqa: E501
            commercial_bureau_score (int): CRIF score. [optional]  # noqa: E501
            commercial_bureau_score_link ([str]): Commercial Bureau Document. [optional]  # noqa: E501
            commercial_bureau_score_link_password (str): Commercial Bureau Document Password. [optional]  # noqa: E501
            partner_score_on_the_customer (int): Score Captured by the Partner. [optional]  # noqa: E501
            total_existing_obligations (int): Total Existing Obligations basis the Bureau Report. [optional]  # noqa: E501
            credit_card_limit (int): Total Credit Card Limit basis the Bureau Report. [optional]  # noqa: E501
            number_of_credit_cards (int): Total Number of Credit Cards per Bureau Report. [optional]  # noqa: E501
            number_of_unsecured_loans (int): Total Number of Unsecured Loans per Bureau Report. [optional]  # noqa: E501
            value_of_total_unsecured_loans (float): Total value of unsecured loans. [optional]  # noqa: E501
            number_of_loans (int): Total Number of Loans per Bureau Report. [optional]  # noqa: E501
            value_of_total_loans (float): Total value of loans. [optional]  # noqa: E501
            number_of_enquiries_3months (int): Number of Enquiries in the Last 3 Months per Bureau Report. [optional]  # noqa: E501
            number_of_enquiries_6months (int): Number of Enquiries in the Last 6 Months per Bureau Report. [optional]  # noqa: E501
            number_of_enquiries_12months (int): Number of Enquiries in the Last 12 Months per Bureau Report. [optional]  # noqa: E501
            number_of_writeoff_suitfiled_settled_12months (int): Number of Writeoff Suitfiled Settled in the Last 12 Months. [optional]  # noqa: E501
            max_dpd_tradeline_12months (int): Maximum DPD Tradeline in the Last 12 Months. [optional]  # noqa: E501
            max_dpd_tradeline_last_6months (int): Maximum DPD Tradeline in the Last 6 Months. [optional]  # noqa: E501
            max_dpd_tradeline_last_3months (int): Maximum DPD Tradeline in the Last 3 Months. [optional]  # noqa: E501
            number_of_pl_enquiries_in_last_30days (int): Number of Pl enquires in the Last 12 Months [optional]  # noqa: E501
            value_of_total_outstanding_loans (float): Value of total outstanding loan in the Last 12 Months [optional]  # noqa: E501
            max_overdue_tradeline (int): Maximum Overdue Tradeline. [optional]  # noqa: E501
            total_overdue_amount_12months (float): Total Overdue Amount in the Last 12 Months. [optional]  # noqa: E501
            loan_amount_settled_12months (float): Loan Amount Settled in the Last 12 Months. [optional]  # noqa: E501
            nature_of_loan_settled1 (str): The nature of past loan settlement if any (Loan 1) - Settled/ Closed/ Written-off. [optional]  # noqa: E501
            nature_of_loan_settled2 (str): The nature of past loan settlement if any (Loan 2) - Settled/ Closed/ Written-off. [optional]  # noqa: E501
            total_emi_bounces (int): Total EMI Bounces. [optional]  # noqa: E501
            emi_bounces_6months (int): EMI Bounces in the Last 6 Months. [optional]  # noqa: E501
            emi_bounces_12months (int): EMI Bounces in the Last 12 Months. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
