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


def lazy_import():
    from credavenue_colending.model.body_create_loan_business_partnership_detail import BodyCreateLoanBusinessPartnershipDetail
    from credavenue_colending.model.body_create_loan_business_partnerships import BodyCreateLoanBusinessPartnerships
    from credavenue_colending.model.body_create_loan_business_private_entity_detail import BodyCreateLoanBusinessPrivateEntityDetail
    globals()['BodyCreateLoanBusinessPartnershipDetail'] = BodyCreateLoanBusinessPartnershipDetail
    globals()['BodyCreateLoanBusinessPartnerships'] = BodyCreateLoanBusinessPartnerships
    globals()['BodyCreateLoanBusinessPrivateEntityDetail'] = BodyCreateLoanBusinessPrivateEntityDetail


class BodyCreateLoanBusiness(ModelNormal):
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
        lazy_import()
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
        lazy_import()
        return {
            'name_of_business': (str,),  # noqa: E501
            'nature_of_business': (str,),  # noqa: E501
            'type_of_constitution': (str,),  # noqa: E501
            'type_of_ownership': (str,),  # noqa: E501
            'registration_date': (date,),  # noqa: E501
            'incorporation_date': (date,),  # noqa: E501
            'industry_type': (str,),  # noqa: E501
            'sector_type': (str,),  # noqa: E501
            'sub_sector_type': (str,),  # noqa: E501
            'business_vintage': (int,),  # noqa: E501
            'business_registered_office_address': (str,),  # noqa: E501
            'business_registered_office_district': (str,),  # noqa: E501
            'business_registered_office_city': (str,),  # noqa: E501
            'business_registered_office_state': (str,),  # noqa: E501
            'business_registered_office_pincode': (int,),  # noqa: E501
            'business_mailing_office_address': (str,),  # noqa: E501
            'business_mailing_office_city': (str,),  # noqa: E501
            'business_mailing_office_state': (str,),  # noqa: E501
            'business_mailing_office_pincode': (int,),  # noqa: E501
            'business_registered_office_link': ([str],),  # noqa: E501
            'business_registered_office_link_password': (str,),  # noqa: E501
            'business_mailing_office_link': ([str],),  # noqa: E501
            'business_mailing_office_link_password': (str,),  # noqa: E501
            'business_phone_number': ([int],),  # noqa: E501
            'business_email_id': ([str],),  # noqa: E501
            'business_partner_score': (float,),  # noqa: E501
            'business_pan_number': (str,),  # noqa: E501
            'business_pan_link': ([str],),  # noqa: E501
            'business_pan_link_password': (str,),  # noqa: E501
            'business_rc_number': (str,),  # noqa: E501
            'business_rc_link': ([str],),  # noqa: E501
            'business_rc_link_password': (str,),  # noqa: E501
            'business_gst_number': (str,),  # noqa: E501
            'business_gst_copy_link': ([str],),  # noqa: E501
            'business_gst_copy_link_password': (str,),  # noqa: E501
            'business_udyog_aadhar_number': (str,),  # noqa: E501
            'business_udyog_aadhar_link': ([str],),  # noqa: E501
            'business_udyog_aadhar_link_password': (str,),  # noqa: E501
            'business_ssi_number': (str,),  # noqa: E501
            'business_ssi_link': ([str],),  # noqa: E501
            'business_ssi_link_password': (str,),  # noqa: E501
            'business_shops_est_number': (str,),  # noqa: E501
            'business_shops_est_link': ([str],),  # noqa: E501
            'business_shops_est_link_password': (str,),  # noqa: E501
            'business_factory_regn_number': (str,),  # noqa: E501
            'business_factory_regn_link': ([str],),  # noqa: E501
            'business_factory_regn_link_password': (str,),  # noqa: E501
            'business_trade_license_number': (str,),  # noqa: E501
            'business_trade_license_link': ([str],),  # noqa: E501
            'business_trade_license_link_password': (str,),  # noqa: E501
            'business_place_photo_link': ([str],),  # noqa: E501
            'business_place_photo_link_password': (str,),  # noqa: E501
            'business_continuity_proof_link': ([str],),  # noqa: E501
            'business_continuity_proof_link_password': (str,),  # noqa: E501
            'other_business_address_proof_number': (str,),  # noqa: E501
            'other_business_address_proof_link': ([str],),  # noqa: E501
            'other_business_address_proof_link_password': (str,),  # noqa: E501
            'no_of_business_authorised_persons': (int,),  # noqa: E501
            'partnerships': ([BodyCreateLoanBusinessPartnerships],),  # noqa: E501
            'partnership_detail': (BodyCreateLoanBusinessPartnershipDetail,),  # noqa: E501
            'private_entity_detail': (BodyCreateLoanBusinessPrivateEntityDetail,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name_of_business': 'name_of_business',  # noqa: E501
        'nature_of_business': 'nature_of_business',  # noqa: E501
        'type_of_constitution': 'type_of_constitution',  # noqa: E501
        'type_of_ownership': 'type_of_ownership',  # noqa: E501
        'registration_date': 'registration_date',  # noqa: E501
        'incorporation_date': 'incorporation_date',  # noqa: E501
        'industry_type': 'industry_type',  # noqa: E501
        'sector_type': 'sector_type',  # noqa: E501
        'sub_sector_type': 'sub_sector_type',  # noqa: E501
        'business_vintage': 'business_vintage',  # noqa: E501
        'business_registered_office_address': 'business_registered_office_address',  # noqa: E501
        'business_registered_office_district': 'business_registered_office_district',  # noqa: E501
        'business_registered_office_city': 'business_registered_office_city',  # noqa: E501
        'business_registered_office_state': 'business_registered_office_state',  # noqa: E501
        'business_registered_office_pincode': 'business_registered_office_pincode',  # noqa: E501
        'business_mailing_office_address': 'business_mailing_office_address',  # noqa: E501
        'business_mailing_office_city': 'business_mailing_office_city',  # noqa: E501
        'business_mailing_office_state': 'business_mailing_office_state',  # noqa: E501
        'business_mailing_office_pincode': 'business_mailing_office_pincode',  # noqa: E501
        'business_registered_office_link': 'business_registered_office_link',  # noqa: E501
        'business_registered_office_link_password': 'business_registered_office_link_password',  # noqa: E501
        'business_mailing_office_link': 'business_mailing_office_link',  # noqa: E501
        'business_mailing_office_link_password': 'business_mailing_office_link_password',  # noqa: E501
        'business_phone_number': 'business_phone_number',  # noqa: E501
        'business_email_id': 'business_email_id',  # noqa: E501
        'business_partner_score': 'business_partner_score',  # noqa: E501
        'business_pan_number': 'business_pan_number',  # noqa: E501
        'business_pan_link': 'business_pan_link',  # noqa: E501
        'business_pan_link_password': 'business_pan_link_password',  # noqa: E501
        'business_rc_number': 'business_rc_number',  # noqa: E501
        'business_rc_link': 'business_rc_link',  # noqa: E501
        'business_rc_link_password': 'business_rc_link_password',  # noqa: E501
        'business_gst_number': 'business_gst_number',  # noqa: E501
        'business_gst_copy_link': 'business_gst_copy_link',  # noqa: E501
        'business_gst_copy_link_password': 'business_gst_copy_link_password',  # noqa: E501
        'business_udyog_aadhar_number': 'business_udyog_aadhar_number',  # noqa: E501
        'business_udyog_aadhar_link': 'business_udyog_aadhar_link',  # noqa: E501
        'business_udyog_aadhar_link_password': 'business_udyog_aadhar_link_password',  # noqa: E501
        'business_ssi_number': 'business_ssi_number',  # noqa: E501
        'business_ssi_link': 'business_ssi_link',  # noqa: E501
        'business_ssi_link_password': 'business_ssi_link_password',  # noqa: E501
        'business_shops_est_number': 'business_shops_est_number',  # noqa: E501
        'business_shops_est_link': 'business_shops_est_link',  # noqa: E501
        'business_shops_est_link_password': 'business_shops_est_link_password',  # noqa: E501
        'business_factory_regn_number': 'business_factory_regn_number',  # noqa: E501
        'business_factory_regn_link': 'business_factory_regn_link',  # noqa: E501
        'business_factory_regn_link_password': 'business_factory_regn_link_password',  # noqa: E501
        'business_trade_license_number': 'business_trade_license_number',  # noqa: E501
        'business_trade_license_link': 'business_trade_license_link',  # noqa: E501
        'business_trade_license_link_password': 'business_trade_license_link_password',  # noqa: E501
        'business_place_photo_link': 'business_place_photo_link',  # noqa: E501
        'business_place_photo_link_password': 'business_place_photo_link_password',  # noqa: E501
        'business_continuity_proof_link': 'business_continuity_proof_link',  # noqa: E501
        'business_continuity_proof_link_password': 'business_continuity_proof_link_password',  # noqa: E501
        'other_business_address_proof_number': 'other_business_address_proof_number',  # noqa: E501
        'other_business_address_proof_link': 'other_business_address_proof_link',  # noqa: E501
        'other_business_address_proof_link_password': 'other_business_address_proof_link_password',  # noqa: E501
        'no_of_business_authorised_persons': 'no_of_business_authorised_persons',  # noqa: E501
        'partnerships': 'partnerships',  # noqa: E501
        'partnership_detail': 'partnership_detail',  # noqa: E501
        'private_entity_detail': 'private_entity_detail',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """BodyCreateLoanBusiness - a model defined in OpenAPI

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
            name_of_business (str): Business name. [optional]  # noqa: E501
            nature_of_business (str): The sector this business belongs to. [optional]  # noqa: E501
            type_of_constitution (str): Partnership/Propertorship/Private Ltd. [optional]  # noqa: E501
            type_of_ownership (str): Type of Ownership. [optional]  # noqa: E501
            registration_date (date): Registration date of the business. [optional]  # noqa: E501
            incorporation_date (date): Incorporation date of the business. [optional]  # noqa: E501
            industry_type (str): trading/ manufacturing/ services. [optional]  # noqa: E501
            sector_type (str): Name of the sector. [optional]  # noqa: E501
            sub_sector_type (str): Name of the Sub sector. [optional]  # noqa: E501
            business_vintage (int): Number of years of business existence. [optional]  # noqa: E501
            business_registered_office_address (str): Address of the business location. [optional]  # noqa: E501
            business_registered_office_district (str): Address of the business location. [optional]  # noqa: E501
            business_registered_office_city (str): City of business address. [optional]  # noqa: E501
            business_registered_office_state (str): State of business address. [optional]  # noqa: E501
            business_registered_office_pincode (int): Pincode of business address. [optional]  # noqa: E501
            business_mailing_office_address (str): Address of business location. [optional]  # noqa: E501
            business_mailing_office_city (str): City of business address. [optional]  # noqa: E501
            business_mailing_office_state (str): State of business location. [optional]  # noqa: E501
            business_mailing_office_pincode (int): Pincode of business location. [optional]  # noqa: E501
            business_registered_office_link ([str]): Registered office document. [optional]  # noqa: E501
            business_registered_office_link_password (str): Registered office document password. [optional]  # noqa: E501
            business_mailing_office_link ([str]): Mailing office document. [optional]  # noqa: E501
            business_mailing_office_link_password (str): Mailing office document password. [optional]  # noqa: E501
            business_phone_number ([int]): Phone number of business address. [optional]  # noqa: E501
            business_email_id ([str]): Email id of the business. [optional]  # noqa: E501
            business_partner_score (float): Partner score for the business. [optional]  # noqa: E501
            business_pan_number (str): PAN number of business. [optional]  # noqa: E501
            business_pan_link ([str]): PAN image of business. [optional]  # noqa: E501
            business_pan_link_password (str): PAN image password of business. [optional]  # noqa: E501
            business_rc_number (str): Registration number of the business. [optional]  # noqa: E501
            business_rc_link ([str]): Image of the RC. [optional]  # noqa: E501
            business_rc_link_password (str): Image password of the RC. [optional]  # noqa: E501
            business_gst_number (str): Business GST number. [optional]  # noqa: E501
            business_gst_copy_link ([str]): Business GST image. [optional]  # noqa: E501
            business_gst_copy_link_password (str): Business GST image password. [optional]  # noqa: E501
            business_udyog_aadhar_number (str): Business Udyog Aadhar Number. [optional]  # noqa: E501
            business_udyog_aadhar_link ([str]): Business Udyog Aadhar Document. [optional]  # noqa: E501
            business_udyog_aadhar_link_password (str): Business Udyog Aadhar Document Password. [optional]  # noqa: E501
            business_ssi_number (str): Small scall industries registration number. [optional]  # noqa: E501
            business_ssi_link ([str]): Small scall industries registration document. [optional]  # noqa: E501
            business_ssi_link_password (str): Small scall industries registration document password. [optional]  # noqa: E501
            business_shops_est_number (str): Shop establishment number. [optional]  # noqa: E501
            business_shops_est_link ([str]): Shop establishment document. [optional]  # noqa: E501
            business_shops_est_link_password (str): Shop establishment document password. [optional]  # noqa: E501
            business_factory_regn_number (str): Factory riegistration number. [optional]  # noqa: E501
            business_factory_regn_link ([str]): Factory riegistration document. [optional]  # noqa: E501
            business_factory_regn_link_password (str): Factory riegistration document password. [optional]  # noqa: E501
            business_trade_license_number (str): Trade license number. [optional]  # noqa: E501
            business_trade_license_link ([str]): Trade license document. [optional]  # noqa: E501
            business_trade_license_link_password (str): Trade license document password. [optional]  # noqa: E501
            business_place_photo_link ([str]): Business place photo image. [optional]  # noqa: E501
            business_place_photo_link_password (str): Business place photo image. [optional]  # noqa: E501
            business_continuity_proof_link ([str]): Business continuity proof document. [optional]  # noqa: E501
            business_continuity_proof_link_password (str): Business continuity proof document password. [optional]  # noqa: E501
            other_business_address_proof_number (str): any other adddress proof number. [optional]  # noqa: E501
            other_business_address_proof_link ([str]): any other adddress proof image. [optional]  # noqa: E501
            other_business_address_proof_link_password (str): any other adddress proof image password. [optional]  # noqa: E501
            no_of_business_authorised_persons (int): Number of authorized person for business. [optional]  # noqa: E501
            partnerships ([BodyCreateLoanBusinessPartnerships]): Refer table Partnerships for attributes. [optional]  # noqa: E501
            partnership_detail (BodyCreateLoanBusinessPartnershipDetail): [optional]  # noqa: E501
            private_entity_detail (BodyCreateLoanBusinessPrivateEntityDetail): [optional]  # noqa: E501
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
        """BodyCreateLoanBusiness - a model defined in OpenAPI

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
            name_of_business (str): Business name. [optional]  # noqa: E501
            nature_of_business (str): The sector this business belongs to. [optional]  # noqa: E501
            type_of_constitution (str): Partnership/Propertorship/Private Ltd. [optional]  # noqa: E501
            type_of_ownership (str): Type of Ownership. [optional]  # noqa: E501
            registration_date (date): Registration date of the business. [optional]  # noqa: E501
            incorporation_date (date): Incorporation date of the business. [optional]  # noqa: E501
            industry_type (str): trading/ manufacturing/ services. [optional]  # noqa: E501
            sector_type (str): Name of the sector. [optional]  # noqa: E501
            sub_sector_type (str): Name of the Sub sector. [optional]  # noqa: E501
            business_vintage (int): Number of years of business existence. [optional]  # noqa: E501
            business_registered_office_address (str): Address of the business location. [optional]  # noqa: E501
            business_registered_office_district (str): Address of the business location. [optional]  # noqa: E501
            business_registered_office_city (str): City of business address. [optional]  # noqa: E501
            business_registered_office_state (str): State of business address. [optional]  # noqa: E501
            business_registered_office_pincode (int): Pincode of business address. [optional]  # noqa: E501
            business_mailing_office_address (str): Address of business location. [optional]  # noqa: E501
            business_mailing_office_city (str): City of business address. [optional]  # noqa: E501
            business_mailing_office_state (str): State of business location. [optional]  # noqa: E501
            business_mailing_office_pincode (int): Pincode of business location. [optional]  # noqa: E501
            business_registered_office_link ([str]): Registered office document. [optional]  # noqa: E501
            business_registered_office_link_password (str): Registered office document password. [optional]  # noqa: E501
            business_mailing_office_link ([str]): Mailing office document. [optional]  # noqa: E501
            business_mailing_office_link_password (str): Mailing office document password. [optional]  # noqa: E501
            business_phone_number ([int]): Phone number of business address. [optional]  # noqa: E501
            business_email_id ([str]): Email id of the business. [optional]  # noqa: E501
            business_partner_score (float): Partner score for the business. [optional]  # noqa: E501
            business_pan_number (str): PAN number of business. [optional]  # noqa: E501
            business_pan_link ([str]): PAN image of business. [optional]  # noqa: E501
            business_pan_link_password (str): PAN image password of business. [optional]  # noqa: E501
            business_rc_number (str): Registration number of the business. [optional]  # noqa: E501
            business_rc_link ([str]): Image of the RC. [optional]  # noqa: E501
            business_rc_link_password (str): Image password of the RC. [optional]  # noqa: E501
            business_gst_number (str): Business GST number. [optional]  # noqa: E501
            business_gst_copy_link ([str]): Business GST image. [optional]  # noqa: E501
            business_gst_copy_link_password (str): Business GST image password. [optional]  # noqa: E501
            business_udyog_aadhar_number (str): Business Udyog Aadhar Number. [optional]  # noqa: E501
            business_udyog_aadhar_link ([str]): Business Udyog Aadhar Document. [optional]  # noqa: E501
            business_udyog_aadhar_link_password (str): Business Udyog Aadhar Document Password. [optional]  # noqa: E501
            business_ssi_number (str): Small scall industries registration number. [optional]  # noqa: E501
            business_ssi_link ([str]): Small scall industries registration document. [optional]  # noqa: E501
            business_ssi_link_password (str): Small scall industries registration document password. [optional]  # noqa: E501
            business_shops_est_number (str): Shop establishment number. [optional]  # noqa: E501
            business_shops_est_link ([str]): Shop establishment document. [optional]  # noqa: E501
            business_shops_est_link_password (str): Shop establishment document password. [optional]  # noqa: E501
            business_factory_regn_number (str): Factory riegistration number. [optional]  # noqa: E501
            business_factory_regn_link ([str]): Factory riegistration document. [optional]  # noqa: E501
            business_factory_regn_link_password (str): Factory riegistration document password. [optional]  # noqa: E501
            business_trade_license_number (str): Trade license number. [optional]  # noqa: E501
            business_trade_license_link ([str]): Trade license document. [optional]  # noqa: E501
            business_trade_license_link_password (str): Trade license document password. [optional]  # noqa: E501
            business_place_photo_link ([str]): Business place photo image. [optional]  # noqa: E501
            business_place_photo_link_password (str): Business place photo image. [optional]  # noqa: E501
            business_continuity_proof_link ([str]): Business continuity proof document. [optional]  # noqa: E501
            business_continuity_proof_link_password (str): Business continuity proof document password. [optional]  # noqa: E501
            other_business_address_proof_number (str): any other adddress proof number. [optional]  # noqa: E501
            other_business_address_proof_link ([str]): any other adddress proof image. [optional]  # noqa: E501
            other_business_address_proof_link_password (str): any other adddress proof image password. [optional]  # noqa: E501
            no_of_business_authorised_persons (int): Number of authorized person for business. [optional]  # noqa: E501
            partnerships ([BodyCreateLoanBusinessPartnerships]): Refer table Partnerships for attributes. [optional]  # noqa: E501
            partnership_detail (BodyCreateLoanBusinessPartnershipDetail): [optional]  # noqa: E501
            private_entity_detail (BodyCreateLoanBusinessPrivateEntityDetail): [optional]  # noqa: E501
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