from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):

    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        data = self.importer.import_data(path)
        for item in data:
            self.data.append(item)

    def __iter__(self):
        return InventoryIterator(self.data)
