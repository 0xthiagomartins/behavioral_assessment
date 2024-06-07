# tests/test_app.py
import pytest
from data_processing import validate_inputs
from business_logic import assess_behavior


def test_validate_inputs():
    assert validate_inputs(60, "Medium", 5) == True
    assert validate_inputs(-1, "Medium", 5) == False
    assert validate_inputs(60, "Invalid", 5) == False
    assert validate_inputs(60, "Medium", 11) == False


def test_assess_behavior():
    result = assess_behavior(60, "Medium", 5)
    assert result["Risk Level"] == "Low"
    assert result["Risk Score"] == 5
    result = assess_behavior(20, "Low", 2)
    assert result["Risk Level"] == "High"
    assert result["Risk Score"] == 9


if __name__ == "__main__":
    pytest.main()
