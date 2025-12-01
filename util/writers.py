import csv
import json
from abc import ABC, abstractmethod

import toml
from .digital_currency_address import DigitalCurrencyAddress
from dataclasses import asdict


class Writer(ABC):
    @abstractmethod
    def write(self, data: list[DigitalCurrencyAddress], output_path: str) -> None: ...


class JSONWriter(Writer):
    def write(self, data: list[DigitalCurrencyAddress], output_path: str) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump([asdict(entry) for entry in data], f, indent=2)


class TOMLWriter(Writer):
    def write(self, data: list[DigitalCurrencyAddress], output_path: str) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            toml.dump({"entries": [asdict(entry) for entry in data]}, f)


class CSVWriter(Writer):
    def write(self, data: list[DigitalCurrencyAddress], output_path: str) -> None:
        if not data:
            return

        rows = [asdict(entry) for entry in data]

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)


class TextWriter(Writer):
    def write(self, data: list[DigitalCurrencyAddress], output_path: str) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            for entry in data:
                for key, value in asdict(entry).items():
                    f.write(f"{key}: {value}\n")
                f.write("\n---\n")
