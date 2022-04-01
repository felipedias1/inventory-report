from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, path):
        try:
            if not path.endswith(".json"):
                raise ValueError("Arquivo inválido")
            else:
                with open(path) as file:
                    return json.load(file)
        except (ValueError, TypeError):
            raise ValueError("Arquivo inválido")
