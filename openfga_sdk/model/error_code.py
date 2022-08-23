"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""


import re  # noqa: F401
import sys  # noqa: F401

from openfga_sdk.model_utils import (  # noqa: F401
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
    OpenApiModel
)
from openfga_sdk.exceptions import ApiAttributeError


class ErrorCode(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'NO_ERROR': "no_error",
            'VALIDATION_ERROR': "validation_error",
            'AUTHORIZATION_MODEL_NOT_FOUND': "authorization_model_not_found",
            'AUTHORIZATION_MODEL_RESOLUTION_TOO_COMPLEX': "authorization_model_resolution_too_complex",
            'INVALID_WRITE_INPUT': "invalid_write_input",
            'CANNOT_ALLOW_DUPLICATE_TUPLES_IN_ONE_REQUEST': "cannot_allow_duplicate_tuples_in_one_request",
            'CANNOT_ALLOW_DUPLICATE_TYPES_IN_ONE_REQUEST': "cannot_allow_duplicate_types_in_one_request",
            'CANNOT_ALLOW_MULTIPLE_REFERENCES_TO_ONE_RELATION': "cannot_allow_multiple_references_to_one_relation",
            'INVALID_CONTINUATION_TOKEN': "invalid_continuation_token",
            'INVALID_TUPLE_SET': "invalid_tuple_set",
            'INVALID_CHECK_INPUT': "invalid_check_input",
            'INVALID_EXPAND_INPUT': "invalid_expand_input",
            'UNSUPPORTED_USER_SET': "unsupported_user_set",
            'INVALID_OBJECT_FORMAT': "invalid_object_format",
            'WRITE_FAILED_DUE_TO_INVALID_INPUT': "write_failed_due_to_invalid_input",
            'AUTHORIZATION_MODEL_ASSERTIONS_NOT_FOUND': "authorization_model_assertions_not_found",
            'LATEST_AUTHORIZATION_MODEL_NOT_FOUND': "latest_authorization_model_not_found",
            'TYPE_NOT_FOUND': "type_not_found",
            'RELATION_NOT_FOUND': "relation_not_found",
            'EMPTY_RELATION_DEFINITION': "empty_relation_definition",
            'INVALID_USER': "invalid_user",
            'INVALID_TUPLE': "invalid_tuple",
            'UNKNOWN_RELATION': "unknown_relation",
            'STORE_ID_INVALID_LENGTH': "store_id_invalid_length",
            'ASSERTIONS_TOO_MANY_ITEMS': "assertions_too_many_items",
            'ID_TOO_LONG': "id_too_long",
            'AUTHORIZATION_MODEL_ID_TOO_LONG': "authorization_model_id_too_long",
            'TUPLE_KEY_VALUE_NOT_SPECIFIED': "tuple_key_value_not_specified",
            'TUPLE_KEYS_TOO_MANY_OR_TOO_FEW_ITEMS': "tuple_keys_too_many_or_too_few_items",
            'PAGE_SIZE_INVALID': "page_size_invalid",
            'PARAM_MISSING_VALUE': "param_missing_value",
            'DIFFERENCE_BASE_MISSING_VALUE': "difference_base_missing_value",
            'SUBTRACT_BASE_MISSING_VALUE': "subtract_base_missing_value",
            'OBJECT_TOO_LONG': "object_too_long",
            'RELATION_TOO_LONG': "relation_too_long",
            'TYPE_DEFINITIONS_TOO_FEW_ITEMS': "type_definitions_too_few_items",
            'TYPE_INVALID_LENGTH': "type_invalid_length",
            'TYPE_INVALID_PATTERN': "type_invalid_pattern",
            'RELATIONS_TOO_FEW_ITEMS': "relations_too_few_items",
            'RELATIONS_TOO_LONG': "relations_too_long",
            'RELATIONS_INVALID_PATTERN': "relations_invalid_pattern",
            'OBJECT_INVALID_PATTERN': "object_invalid_pattern",
            'QUERY_STRING_TYPE_CONTINUATION_TOKEN_MISMATCH': "query_string_type_continuation_token_mismatch",
            'EXCEEDED_ENTITY_LIMIT': "exceeded_entity_limit",
            'INVALID_CONTEXTUAL_TUPLE': "invalid_contextual_tuple",
            'DUPLICATE_CONTEXTUAL_TUPLE': "duplicate_contextual_tuple",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """ErrorCode - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): if omitted defaults to "no_error", must be one of ["no_error", "validation_error", "authorization_model_not_found", "authorization_model_resolution_too_complex", "invalid_write_input", "cannot_allow_duplicate_tuples_in_one_request", "cannot_allow_duplicate_types_in_one_request", "cannot_allow_multiple_references_to_one_relation", "invalid_continuation_token", "invalid_tuple_set", "invalid_check_input", "invalid_expand_input", "unsupported_user_set", "invalid_object_format", "write_failed_due_to_invalid_input", "authorization_model_assertions_not_found", "latest_authorization_model_not_found", "type_not_found", "relation_not_found", "empty_relation_definition", "invalid_user", "invalid_tuple", "unknown_relation", "store_id_invalid_length", "assertions_too_many_items", "id_too_long", "authorization_model_id_too_long", "tuple_key_value_not_specified", "tuple_keys_too_many_or_too_few_items", "page_size_invalid", "param_missing_value", "difference_base_missing_value", "subtract_base_missing_value", "object_too_long", "relation_too_long", "type_definitions_too_few_items", "type_invalid_length", "type_invalid_pattern", "relations_too_few_items", "relations_too_long", "relations_invalid_pattern", "object_invalid_pattern", "query_string_type_continuation_token_mismatch", "exceeded_entity_limit", "invalid_contextual_tuple", "duplicate_contextual_tuple", ]  # noqa: E501

        Keyword Args:
            value (str): if omitted defaults to "no_error", must be one of ["no_error", "validation_error", "authorization_model_not_found", "authorization_model_resolution_too_complex", "invalid_write_input", "cannot_allow_duplicate_tuples_in_one_request", "cannot_allow_duplicate_types_in_one_request", "cannot_allow_multiple_references_to_one_relation", "invalid_continuation_token", "invalid_tuple_set", "invalid_check_input", "invalid_expand_input", "unsupported_user_set", "invalid_object_format", "write_failed_due_to_invalid_input", "authorization_model_assertions_not_found", "latest_authorization_model_not_found", "type_not_found", "relation_not_found", "empty_relation_definition", "invalid_user", "invalid_tuple", "unknown_relation", "store_id_invalid_length", "assertions_too_many_items", "id_too_long", "authorization_model_id_too_long", "tuple_key_value_not_specified", "tuple_keys_too_many_or_too_few_items", "page_size_invalid", "param_missing_value", "difference_base_missing_value", "subtract_base_missing_value", "object_too_long", "relation_too_long", "type_definitions_too_few_items", "type_invalid_length", "type_invalid_pattern", "relations_too_few_items", "relations_too_long", "relations_invalid_pattern", "object_invalid_pattern", "query_string_type_continuation_token_mismatch", "exceeded_entity_limit", "invalid_contextual_tuple", "duplicate_contextual_tuple", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "no_error"

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """ErrorCode - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): if omitted defaults to "no_error", must be one of ["no_error", "validation_error", "authorization_model_not_found", "authorization_model_resolution_too_complex", "invalid_write_input", "cannot_allow_duplicate_tuples_in_one_request", "cannot_allow_duplicate_types_in_one_request", "cannot_allow_multiple_references_to_one_relation", "invalid_continuation_token", "invalid_tuple_set", "invalid_check_input", "invalid_expand_input", "unsupported_user_set", "invalid_object_format", "write_failed_due_to_invalid_input", "authorization_model_assertions_not_found", "latest_authorization_model_not_found", "type_not_found", "relation_not_found", "empty_relation_definition", "invalid_user", "invalid_tuple", "unknown_relation", "store_id_invalid_length", "assertions_too_many_items", "id_too_long", "authorization_model_id_too_long", "tuple_key_value_not_specified", "tuple_keys_too_many_or_too_few_items", "page_size_invalid", "param_missing_value", "difference_base_missing_value", "subtract_base_missing_value", "object_too_long", "relation_too_long", "type_definitions_too_few_items", "type_invalid_length", "type_invalid_pattern", "relations_too_few_items", "relations_too_long", "relations_invalid_pattern", "object_invalid_pattern", "query_string_type_continuation_token_mismatch", "exceeded_entity_limit", "invalid_contextual_tuple", "duplicate_contextual_tuple", ]  # noqa: E501

        Keyword Args:
            value (str): if omitted defaults to "no_error", must be one of ["no_error", "validation_error", "authorization_model_not_found", "authorization_model_resolution_too_complex", "invalid_write_input", "cannot_allow_duplicate_tuples_in_one_request", "cannot_allow_duplicate_types_in_one_request", "cannot_allow_multiple_references_to_one_relation", "invalid_continuation_token", "invalid_tuple_set", "invalid_check_input", "invalid_expand_input", "unsupported_user_set", "invalid_object_format", "write_failed_due_to_invalid_input", "authorization_model_assertions_not_found", "latest_authorization_model_not_found", "type_not_found", "relation_not_found", "empty_relation_definition", "invalid_user", "invalid_tuple", "unknown_relation", "store_id_invalid_length", "assertions_too_many_items", "id_too_long", "authorization_model_id_too_long", "tuple_key_value_not_specified", "tuple_keys_too_many_or_too_few_items", "page_size_invalid", "param_missing_value", "difference_base_missing_value", "subtract_base_missing_value", "object_too_long", "relation_too_long", "type_definitions_too_few_items", "type_invalid_length", "type_invalid_pattern", "relations_too_few_items", "relations_too_long", "relations_invalid_pattern", "object_invalid_pattern", "query_string_type_continuation_token_mismatch", "exceeded_entity_limit", "invalid_contextual_tuple", "duplicate_contextual_tuple", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "no_error"

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
