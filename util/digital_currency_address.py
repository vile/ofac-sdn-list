from dataclasses import dataclass


@dataclass
class DigitalCurrencyAddress:
    type: str
    address: str
