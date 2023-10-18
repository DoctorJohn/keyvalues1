from keyvalues1 import KeyValues1


def test_pair_with_string():
    text = """
    "key1" "value1"
    """

    assert KeyValues1.parse(text) == {"key1": "value1"}


def test_pair_with_empty_string():
    text = """
    "key1" ""
    """

    assert KeyValues1.parse(text) == {"key1": ""}


def test_pair_with_empty_dict():
    text = """
    "key1"
    {
    }
    """

    assert KeyValues1.parse(text) == {"key1": {}}


def test_pair_with_string_in_dict():
    text = """
    "key1"
    {
        "key2" "value2"
    }
    """

    assert KeyValues1.parse(text) == {"key1": {"key2": "value2"}}


def test_pair_with_strings_in_dict():
    text = """
    "key1"
    {
        "key2" "value2"
        "key3" "value3"
    }
    """

    assert KeyValues1.parse(text) == {"key1": {"key2": "value2", "key3": "value3"}}


def test_pair_with_dict_in_dict():
    text = """
    "key1"
    {
        "key2" {}
    }
    """

    assert KeyValues1.parse(text) == {"key1": {"key2": {}}}


def test_pair_with_dicts_in_dict():
    text = """
    "key1"
    {
        "key2" {}
        "key3" {}
    }
    """

    assert KeyValues1.parse(text) == {"key1": {"key2": {}, "key3": {}}}


def test_pair_with_mixed_dict():
    text = """
    "key1"
    {
        "key2" "value2"
        "key3" {}
    }
    """

    assert KeyValues1.parse(text) == {"key1": {"key2": "value2", "key3": {}}}


def test_ignore_comments():
    text = """
    // First comment
    "key1"
    {
        // Second comment
        "key2" "value2"
        "key3" {} // Third comment
    }
    """

    assert KeyValues1.parse(text) == {"key1": {"key2": "value2", "key3": {}}}
