"""
Tests for the enums module
"""
from cryptotraderbot import enums


def test_assets_string():
    """
    type checks
    copy and paste checks
    """
    str_values = set()
    for asset in enums.Assets:
        str_value = asset.value["str"]
        assert isinstance(str_value, str)
        assert str_value is not None
        assert str_value not in str_values
        str_values.add(str_value)


def test_assets_kraken():
    """
    type checks
    copy and paste checks
    """
    kraken_names = set()
    for asset in enums.Assets:
        kraken_name = asset.value[enums.CryptoApis.KRAKEN]
        assert kraken_name is not None
        assert kraken_name not in kraken_names
        kraken_names.add(kraken_name)


def test_cryptoapis():
    """
    type checks
    """
    for api in enums.CryptoApis:
        assert isinstance(api.value, str)
