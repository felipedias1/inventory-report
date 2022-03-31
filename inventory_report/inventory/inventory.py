from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory(CompleteReport, SimpleReport):
    @classmethod
    def import_data(cls, path, type):
        with open(path) as file:
            reports = csv.DictReader(file, delimiter=",", quotechar='"')
        read = [report for report in reports]
        if type == 'simples':
            return SimpleReport.generate(read)
        else:
            return CompleteReport.generate(read)
