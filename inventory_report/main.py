from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    terminalInputs = sys.argv
    if len(terminalInputs) < 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        path, type = sys.argv[1], sys.argv[2]
        extension = path.rsplit('.', 1)[1]
        importers = {
            "csv": CsvImporter,
            "xml": XmlImporter,
            "json": JsonImporter
        }
        obj = InventoryRefactor(importers[extension])
        print(obj.import_data(path, type), end="")
