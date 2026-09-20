import pytest

from sales_validation import FilenameFormatRule


@pytest.mark.parametrize(
    "filename, expected_errors",
    [
        ("SALES_DATA_20260920143000.csv", []),
        ("WRONG_DATA_20260920143000.csv",
         ["Incorrect filename format."]),
        ("SALES_DATA_20260920.csv",
         ["Incorrect filename format."]),
        ("sales_data_20260920143000.csv",
         ["Incorrect filename format."]),
        ("SALES_DATA_ABCDEFGHIJKLMN.csv",
         ["Incorrect filename format."]),
        ("SALES_DATA_20260920143000.txt",
         ["Incorrect filename format."]),
        ("", ["Incorrect filename format."]),
    ]
)
def test_filename_format_rule(filename, expected_errors):
    rule = FilenameFormatRule()

    result = rule.validate(
        filepath="",
        filename=filename
    )

    assert result == expected_errors
    