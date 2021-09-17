import pytest


@pytest.mark.dependency(depends=[
    # see https://github.com/RKrahl/pytest-dependency/issues/55
    'tests/test_0001_html.py::TestAttributeDict::test_get_initial_values',
    'tests/test_0001_html.py::TestAttributeDict::test_set_attributes',
    'tests/test_0001_html.py::TestAttributeDict::test_value_cant_be_dict',
    'tests/test_0001_html.py::TestAttributeDict::test_cant_use_id_key',
    'tests/test_0001_html.py::TestAttributeDict::test_empty_dict_is_false',
    'tests/test_0001_html.py::TestAttributeDict::test_non_empty_dict_is_true',
    'tests/test_0001_html.py::TestAttributeDict::test_pop_existing_key',
    'tests/test_0001_html.py::TestAttributeDict::test_pop_unknown_key',
    'tests/test_0001_html.py::TestAttributeDict::test_pop_unknown_key_with_default',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeDict::test_pop_existing_key_with_default',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeDict::test_pop_expects_at_most_2_arguments',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeDict::test_del_existing_key',
    'tests/test_0001_html.py::TestAttributeDict::test_del_unknown_key',
    'tests/test_0001_html.py::TestAttributeList::test_add_existing_element_does_nothing',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_add_one_element',
    'tests/test_0001_html.py::TestAttributeList::test_cant_add_dict',
    'tests/test_0001_html.py::TestAttributeList::test_cant_set_dict',
    'tests/test_0001_html.py::TestAttributeList::test_cant_set_list_with_dict',
    'tests/test_0001_html.py::TestAttributeList::test_clear',
    'tests/test_0001_html.py::TestAttributeList::test_clear_empty_list',
    'tests/test_0001_html.py::TestAttributeList::test_default_class_list_is_empty',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_default_id_list_is_empty',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_default_list_has_zero_len',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_empty_list_is_false',
    'tests/test_0001_html.py::TestAttributeList::test_equality_ignored_duplicates',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_equality_ignores_order',
    'tests/test_0001_html.py::TestAttributeList::test_extend',
    'tests/test_0001_html.py::TestAttributeList::test_extend_ignores_duplicates',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_in_keyword',
    'tests/test_0001_html.py::TestAttributeList::test_initial_class_can_be_list',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_initial_class_can_be_passed_via_kwargs',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_initial_class_can_be_space_separated_str',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_initial_id_can_be_list',
    'tests/test_0001_html.py::TestAttributeList::test_initial_id_can_be_passed_via_kwargs',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_initial_id_can_be_space_separated_str',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_initial_id_cant_be_dict',
    'tests/test_0001_html.py::TestAttributeList::test_len_returns_number_of_elements',  # NOQA: E501
    'tests/test_0001_html.py::TestAttributeList::test_non_empty_list_is_true',
    'tests/test_0001_html.py::TestAttributeList::test_non_equality',
    'tests/test_0001_html.py::TestAttributeList::test_remove_existing_element',
    'tests/test_0001_html.py::TestAttributeList::test_remove_unknown_element',
    'tests/test_0001_html.py::TestAttributeList::test_set_class_list',
    'tests/test_0001_html.py::TestAttributeList::test_set_id_list',
    'tests/test_0001_html.py::TestAttributeList::test_toggle_existing_element',
    'tests/test_0001_html.py::TestAttributeList::test_toggle_unknown_element',
], scope='session')
def test_node_api():
    pass
