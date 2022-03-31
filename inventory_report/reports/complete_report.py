from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        companies = Counter(item["nome_da_empresa"] for item in list)
        result = super().generate(list)
        product_qty = ""
        for key, value in companies.items():
            product_qty += f"- {key}: {value}\n"

        return (
          f"{result}\n"
          "Produtos estocados por empresa: \n"
          f"{product_qty}"
        )


print(CompleteReport.generate(list))
