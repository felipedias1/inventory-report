from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    @classmethod
    def import_data(cls, path):
        try:
            if ".xml" not in path:
                raise ValueError("Arquivo inválido")
            else:
                pass  # function to read XML
        except (ValueError, TypeError):
            raise ValueError("Arquivo inválido")
