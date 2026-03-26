import requests
from bs4 import BeautifulSoup

def buscar_concursos():
    url = "https://www.pciconcursos.com.br/concursos/distrito-federal/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    dados = []

    links = soup.find_all("a")

    for link in links:
        texto = link.text.strip()
        href = link.get("href")

        if len(texto) > 30 and "concurso" in texto.lower():

            if href:
                if href.startswith("http"):
                    link_completo = href
                else:
                    link_completo = f"https://www.pciconcursos.com.br{href}"
            else:
                link_completo = None

            dados.append({
                "titulo": texto,
                "link": link_completo,
                "fonte": "PCI Concursos",
                "local": "DF"
            })

    return dados