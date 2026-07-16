<div align="center">

# 🏛️ Concursos DF Scraper

### Automação em Python para coleta e organização de concursos públicos do Distrito Federal

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/BeautifulSoup-43A047?style=for-the-badge">
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white">

</div>

---

## 📖 Sobre o projeto

O **Concursos DF Scraper** é uma automação desenvolvida em Python para coletar informações sobre concursos públicos disponíveis no Distrito Federal.

O sistema consulta páginas de concursos, identifica oportunidades publicadas, extrai informações relevantes e organiza os resultados automaticamente em uma planilha Excel.

O objetivo do projeto é facilitar a visualização e comparação das oportunidades, evitando a necessidade de acessar e analisar cada publicação manualmente.

## ⚙️ Como funciona

O scraper acessa a página de concursos públicos do Distrito Federal no portal PCI Concursos e coleta os links relacionados às oportunidades encontradas.

Em seguida, o sistema acessa cada publicação individualmente para identificar informações salariais. Os valores são tratados e convertidos para um formato numérico, permitindo que as oportunidades sejam organizadas do maior para o menor salário.

```text
Portal de concursos
        ↓
Coleta das oportunidades
        ↓
Extração de títulos e links
        ↓
Busca dos salários
        ↓
Tratamento e organização dos dados
        ↓
Geração da planilha Excel
```

## ✨ Recursos principais

- Coleta automatizada de concursos públicos do Distrito Federal.
- Extração de títulos e links das oportunidades.
- Identificação automática de salários nas publicações.
- Remoção de resultados duplicados.
- Conversão e tratamento dos valores salariais.
- Ordenação das oportunidades pelo maior salário.
- Exportação dos dados para uma planilha Excel.
- Exibição das principais oportunidades diretamente no terminal.

## 📊 Informações geradas

A planilha final apresenta informações como:

| Campo | Descrição |
| --- | --- |
| `titulo` | Título da publicação ou concurso |
| `link` | Endereço da página da oportunidade |
| `fonte` | Portal onde a informação foi encontrada |
| `local` | Localidade da oportunidade |
| `salario` | Remuneração identificada na publicação |
| `salario_num` | Valor convertido para ordenação dos resultados |

## 🛠️ Tecnologias utilizadas

- Python
- Requests
- Beautiful Soup
- Pandas
- OpenPyXL
- Expressões Regulares
- Web Scraping
- Microsoft Excel

## 📁 Resultado

Após a execução, o sistema gera automaticamente o arquivo:

```text
data/concursos_df.xlsx
```

A planilha contém as oportunidades encontradas, organizadas em ordem decrescente de salário.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar e demonstrar conhecimentos em:

- Automação com Python.
- Coleta de dados na web.
- Manipulação e limpeza de dados.
- Expressões regulares.
- Organização de informações com Pandas.
- Geração automatizada de planilhas.
- Separação de responsabilidades entre módulos.

## ⚠️ Observação

Os dados apresentados dependem das informações disponíveis no portal consultado.

Como a estrutura das páginas pode ser alterada ao longo do tempo, ajustes no scraper podem ser necessários para manter a coleta funcionando corretamente.

Este projeto não possui vínculo oficial com o portal utilizado como fonte ou com os órgãos responsáveis pelos concursos publicados.

## 🚧 Status

Projeto funcional e aberto para futuras melhorias.

### Possíveis evoluções

- Coleta de datas de inscrição.
- Identificação de vagas disponíveis.
- Filtro por nível de escolaridade.
- Filtro por faixa salarial.
- Suporte a outros estados.
- Coleta de bancas organizadoras.
- Interface gráfica para consulta.
- Atualização automática programada.
- Envio de alertas sobre novas oportunidades.

---

<div align="center">

Desenvolvido por **Emanuel FHX**

</div>
