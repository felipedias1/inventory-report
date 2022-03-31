from datetime import datetime
from collections import Counter


class SimpleReport():
    @classmethod
    def generate(cls, list):
        today = datetime.today().strftime("%Y-%m-%d")
        older_fab = min(item["data_de_fabricacao"] for item in list)
        upcoming_val = min(
          item["data_de_validade"]
          for item in list
          if item["data_de_validade"] >= today
        )

        comp_name = max(Counter(item["nome_da_empresa"] for item in list))

        return (
          f"Data de fabricação mais antiga: {older_fab}\n"
          f"Data de validade mais próxima: {upcoming_val}\n"
          f"Empresa com maior quantidade de produtos estocados: {comp_name}\n"
        )
