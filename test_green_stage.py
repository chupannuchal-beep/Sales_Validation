from sales_validation import FilenameFormatRule


def test_valid_filename_returns_no_errors():
    rule = FilenameFormatRule()

    errors = rule.validate(
        filepath="",
        filename="SALES_DATA_20260920110617.csv"
    )

    assert errors == []


def test_invalid_filename_returns_error():
    rule = FilenameFormatRule()

    errors = rule.validate(
        filepath="",
        filename="THIS_IS_TOTALLY_WRONG.csv"
    )

    assert errors == ["Incorrect filename format."]