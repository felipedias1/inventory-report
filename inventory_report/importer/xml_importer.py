from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):

    @classmethod
    def import_data(cls, path):
        try:
            if ".xml" not in path:
                raise ValueError("Arquivo inválido")
            else:
                with open(path, 'r') as file:
                    selector = xmltodict.parse(file.read())
                    return selector['dataset']['record']
        except (ValueError, TypeError):
            raise ValueError("Arquivo inválido")
