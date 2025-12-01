import csv
import json
from abc import ABC, abstractmethod
from dataclasses import asdict
from pathlib import Path
from typing import Union

import toml

from .digital_currency_address import DigitalCurrencyAddress

PathOrStrPath = Union[Path, str]


class Writer(ABC):
    @abstractmethod
    def write(
        self, data: list[DigitalCurrencyAddress], output_path: PathOrStrPath
    ) -> None:
        """
        Format content and write file.

        Params
        ------
            data (list[DigitalCurrencyAddress]): List of parsed cryptocurrency address entries
            output_path (PathOrStrPath): Path to file to write formatted content
        """
        ...


class JSONWriter(Writer):
    def write(
        self, data: list[DigitalCurrencyAddress], output_path: PathOrStrPath
    ) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump([asdict(entry) for entry in data], f, indent=2)


class TOMLWriter(Writer):
    def write(
        self, data: list[DigitalCurrencyAddress], output_path: PathOrStrPath
    ) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            toml.dump({"entries": [asdict(entry) for entry in data]}, f)


class CSVWriter(Writer):
    def write(
        self, data: list[DigitalCurrencyAddress], output_path: PathOrStrPath
    ) -> None:
        if not data:
            return

        rows = [asdict(entry) for entry in data]

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)


class TextWriter(Writer):
    def write(
        self, data: list[DigitalCurrencyAddress], output_path: PathOrStrPath
    ) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            for entry in data:
                for key, value in asdict(entry).items():
                    f.write(f"{key}: {value}\n")
                f.write("\n---\n")
