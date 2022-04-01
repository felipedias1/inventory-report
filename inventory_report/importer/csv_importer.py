from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path):
        try:
            if not path.endswith(".csv"):
                raise ValueError("Arquivo inválido")
            else:
                with open(path) as file:
                    reports = DictReader(file, delimiter=",", quotechar='"')
                    return [report for report in reports]
        except ValueError:
            raise ValueError("Arquivo inválido")
