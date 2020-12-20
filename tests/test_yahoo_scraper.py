import pytest
from scraper import get_rate_regex, get_rate, CcyPairNotFound
from validators import validate_input, ValidationError


@pytest.mark.parametrize(
    "from_ccy, to_ccy",
    [
        ("GBP", "USD"),
        ("GBP", "EUR"),
        ("EUR", "USD"),
        ("GBP", "JPY"),
        ("USD", "JPY"),
        ("USD", "GBP"),
        ("GBP", "AUD"),
        ("GBP", "BRL"),
        ("GBP", "CAD"),
        ("GBP", "CHF"),
        ("GBP", "CNY"),
        ("GBP", "INR"),
        ("GBP", "NOK"),
        ("GBP", "QAR"),
        ("GBP", "ZAR"),
        ("EUR", "CHF"),
        ("EUR", "CAD"),
        ("EUR", "JPY"),
        ("EUR", "SEK"),
        ("EUR", "HUF"),
        ("USD", "CAD"),
        ("USD", "HKD"),
        ("USD", "SGD"),
        ("USD", "INR"),
        ("USD", "MXN"),
        ("EUR", "JPY"),
        ("USD", "CNY"),
        ("USD", "CHF"),
    ]
)
def test_get_rate(from_ccy, to_ccy):
    result = get_rate(from_ccy=from_ccy, to_ccy=to_ccy)
    assert result is not None
    value = float(result)
    assert value > 0
    print(f"{from_ccy}/{to_ccy}: {value}")


@pytest.mark.parametrize(
    "from_ccy, to_ccy",
    [
        ("GBP", "RUB"),
        ("ABC", "DEF"),
    ]
)
def test_get_rate_invalid(from_ccy, to_ccy):
    with pytest.raises(CcyPairNotFound) as exc:
        get_rate_regex(from_ccy=from_ccy, to_ccy=to_ccy)
        assert "Currency pair not found" in str(exc.value)


@pytest.mark.parametrize(
    "user_input, expected_error",
    [
        ("", "Input must contain colon character"),
        (":", "Currency symbol must have a length of 3"),
        ("A:B", "Currency symbol must have a length of 3"),
        ("AA:BB", "Currency symbol must have a length of 3")
    ]
)
def test_validate_input_invalid(user_input, expected_error):
    with pytest.raises(ValidationError) as exc:
        validate_input(user_input)
        assert expected_error in exc



@pytest.mark.skip
@pytest.mark.parametrize(
    "from_ccy, to_ccy",
    [
        ("GBP", "USD"),
        ("GBP", "EUR"),
        ("EUR", "USD"),
        ("GBP", "JPY"),
        ("USD", "JPY"),
        ("USD", "GBP"),
        ("GBP", "AUD"),
        ("GBP", "BRL"),
        ("GBP", "CAD"),
        ("GBP", "CHF"),
        ("GBP", "CNY"),
        ("GBP", "INR"),
        ("GBP", "NOK"),
        ("GBP", "QAR"),
        ("GBP", "ZAR"),
        ("EUR", "CHF"),
        ("EUR", "CAD"),
        ("EUR", "JPY"),
        ("EUR", "SEK"),
        ("EUR", "HUF"),
        ("USD", "CAD"),
        ("USD", "HKD"),
        ("USD", "SGD"),
        ("USD", "INR"),
        ("USD", "MXN"),
        ("EUR", "JPY"),
        ("USD", "CNY"),
        ("USD", "CHF"),
    ]
)
def test_get_rate_regex(from_ccy, to_ccy):
    result = get_rate_regex(from_ccy=from_ccy, to_ccy=to_ccy)
    assert result is not None
    value = float(result)
    assert value > 0
    print(f"{from_ccy}/{to_ccy}: {value}")
