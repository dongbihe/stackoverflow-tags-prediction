import pytest

from api.preprocessing import (
    clean_html_tags,
    clean_text,
    replace_programming_language_name,
)


@pytest.mark.parametrize(
    "text, expected",
    [("c++", "cplusplus"), ("c#", "csharp"), ("node.js", "nodejs"), ("", "")],
)
def test_replace_programming_language_name(text, expected):
    assert replace_programming_language_name(text) == expected


def test_clean_html_tags():
    assert clean_html_tags("<p></>") == ""
    assert clean_html_tags("") == ""


raw_text = "How to exit in Node.js <p>What is the command that is used to exit? (i.e terminate the Node.js process)</p>"
cleaned_test = "exit nodejs command use exit e terminate nodejs process"


def test_clean_test():
    assert clean_text(raw_text) == cleaned_test
