from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory(CompleteReport, SimpleReport):
    @classmethod
    def import_data(cls, path, type):
        read = []
        if path.lower().endswith('.csv'):
            with open(path) as file:
                reports = csv.DictReader(file, delimiter=",", quotechar='"')
                read = [report for report in reports]
        elif path.lower().endswith('.json'):
            with open(path) as file:
                read = json.load(file)
        elif path.lower().endswith('.xml'):
            with open(path) as file:
                read = file.read()

        if type == 'simples':
            return SimpleReport.generate(read)
        else:
            return CompleteReport.generate(read)
