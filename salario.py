import requests
from bs4 import BeautifulSoup
import re

def extrair_salario(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        texto = soup.get_text()

        salarios = re.findall(r"R\$\s?[\d\.\,]+", texto)

        return salarios[0] if salarios else "Não informado"

    except:
        return "Erro"