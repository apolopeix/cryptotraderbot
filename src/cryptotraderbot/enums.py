"""
Mapping of crypto currencies (3 characters codes) with aliases"
"""
from enum import Enum, unique


@unique
class CryptoApis(Enum):
    """
    List of supported crypto apis
    """
    KRAKEN = "kraken"


@unique
class Assets(Enum):
    """
    List of supported crypto currencies with a dict with crypto api and
    string values.
    """
    BTC = {CryptoApis.KRAKEN: "XXBT", "str": "Bitcoin"}
    ETH = {CryptoApis.KRAKEN: "XETH", "str": "Ethereum"}
    LTC = {CryptoApis.KRAKEN: "XLTC", "str": "Litecoin"}
    EUR = {CryptoApis.KRAKEN: "ZEUR", "str": "Euro"}
    XRP = {CryptoApis.KRAKEN: "XXRP", "str": "Ripple"}
