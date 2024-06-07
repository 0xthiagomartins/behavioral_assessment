import pytest
from src.business_logic import assess_behavior


def test_assess_behavior():
    result = assess_behavior(60, "Medium", 5)
    assert result["Risk Level"] == "Low"
    assert result["Risk Score"] == 5
    result = assess_behavior(20, "Low", 2)
    assert result["Risk Level"] == "High"
    assert result["Risk Score"] == 9


if __name__ == "__main__":
    pytest.main()
