import argparse
import os
from pathlib import Path
from typing import Final

from lxml import etree

from util.digital_currency_address import DigitalCurrencyAddress
from util.writers import CSVWriter, JSONWriter, TextWriter, TOMLWriter

NS: Final[dict[str, str]] = {
    "ofac": "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/ENHANCED_XML"
}
DIGITAL_CURRENCY_ADDRESS: Final[str] = "Digital Currency Address"


def parse_ofac_xml(path: Path) -> list[DigitalCurrencyAddress]:
    """
    Parse out all cryptocurrency addresses from OFAC's SDN XML list.

    Params
    ------
        path (Path): Path to the XML file

    Returns
    -------
        list[DigitalCurrencyAddress]: List of parsed cryptocurrency addresses

    """
    tree = etree.parse(path)
    root = tree.getroot()
    entities_parent = root.find("ofac:entities", NS)
    entities = entities_parent.findall("ofac:entity", NS)

    results = []

    for entity in entities:
        features_parent = entity.find("ofac:features", NS)

        if features_parent is None:
            continue

        features = features_parent.findall("ofac:feature", NS)

        for feature in features:
            feature_type = feature.find("ofac:type", NS)
            feature_data = feature.find("ofac:value", NS)

            if (
                feature_type is not None
                and DIGITAL_CURRENCY_ADDRESS in (address_type := feature_type.text)
                and feature_data is not None
            ):
                address = feature_data.text
                # print(f"{address_type}: {address}")
                results.append(DigitalCurrencyAddress(address_type, address))

    return results


def parse_args() -> argparse.Namespace:
    """
    Get cli args.

    Returns
    -------
        argparse.Namespace: Args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--xml",
        required=True,
        help="Path to OFAC SDN XML file",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output directory",
    )

    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_args()

    xml_file = Path(args.xml)
    if not xml_file.exists():
        print(f"{args.xml} does not exist")
        exit(1)

    # Ensure output directory exists
    export_dir = Path(args.out)
    os.makedirs(export_dir, exist_ok=True)

    results = parse_ofac_xml(xml_file)

    writers = {
        "sdn.json": JSONWriter(),
        "sdn.toml": TOMLWriter(),
        "sdn.csv": CSVWriter(),
        "sdn.txt": TextWriter(),
    }

    for filename, writer in writers.items():
        writer.write(results, export_dir / filename)


if __name__ == "__main__":
    main()
