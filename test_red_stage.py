import pytest
from sales_validation import FilenameFormatRule

def test_filename_pattern_validation_red():

    rule = FilenameFormatRule()
    
    errors = rule.validate("/tmp", "THIS_IS_TOTALLY_WRONG.csv")

    assert "Incorrect filename format." in errors

