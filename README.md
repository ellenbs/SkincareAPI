# NLP APS1

Skincare API

## Description

O objetivo do projeto é fornecer uma maneira eficiente de buscar e classificar reviews de produtos, retornando os mais relevantes de acordo com a consulta fornecida pelo usuário. Isso pode ser útil, por exemplo, para analisar feedbacks de clientes e tomar decisões informadas com base em suas opiniões.

## Project Stricture

O projeto foi dividido em 3 partes:

1. **app**: Contém o código da API, que é responsável por receber a query do usuário e retornar os resultados mais relevantes.
2. **data**: Contém a base de dados utilizada no projeto.
3. **tests**: Contém os testes unitários do projeto.

## API

A API foi desenvolvida utilizando a biblioteca FastAPI, que é uma estrutura moderna e rápida para criar APIs com Python 3.6+ baseada em padrões de digitação de tipo Python padrão. A API possui um endpoint que recebe uma query do usuário e retorna os resultados mais relevantes de acordo com a consulta.

## DataBase

A base de dados foi retirada via web scraping do site https://www.sephora.com.br/ e contém informações sobre produtos de skincare, como nome, marca, review e relevância.

## Installation

```bash
git clone https://github.com/ellenbs/SkincareAPI
```

## Running the Project

```bash
pip install -r requirements.txt
```

```bash
pyhton ./app/main.py
```

## Usage

A API possui um único endpoint que recebe uma query do usuário e retorna os resultados mais relevantes de acordo com a consulta.

### Request

```bash
http://0.0.0.0:8000/query?query=acne

```
## Output

```bash

{
  "results": [
    {
      "Produto": "ÓLEO FACIAL HIDRATANTE DRUNK ELEPHANT VIRGIN MARULA LUXURY FACIAL OIL",
      "Marca": "DRUNK ELEPHANT",
      "Review": "Não deixa a pele oleosa (tenho acne). Fica bem sequinho, diminui linhas finas, hidrata e senti que ajuda na cicatrização da acne! Show!!!",
      "Relevancia": 0.442796484433295
    },
    {
      "Produto": "LOÇÃO TONIFICANTE HIDRATANTE CLARINS",
      "Marca": "CLARINS",
      "Review": "FINALMENTE ACHEI MEU HIDRATANTE PARA ACNE FUNGICA",
      "Relevancia": 0.369487849782322
    },
    {
      "Produto": "DOUBLE SÉRUM AVANÇADO GUERLAIN ABEILLE ROYALE",
      "Marca": "GUERLAIN",
      "Review": "De todos os cremes p/ hidratação do rosto foi o que mais me adaptei, além de não desenvolver acne",
      "Relevancia": 0.279610596580202
    },
    {
      "Produto": "BEE GLOW - HIDRATAÇÃO COM EFEITO DEWY - ABEILLE ROYALE",
      "Marca": "GUERLAIN",
      "Review": "Pele madura e oleosa, podendo ter acne Este serum me deixa hidratada sem ficar oleosa Eu adoro, uso faz uns 4 meses",
      "Relevancia": 0.234945548696429
    },
    {
      "Produto": "GEL DE LIMPEZA FACIAL ANTI-IMPERFEIÇÕES SEPHORA COLLECTION FACE & BODY CLEANSER",
      "Marca": "SEPHORA COLLECTION",
      "Review": "Não é irritante, não resseca, não queima a pele, não tem cheiro e faz seu trabalho. Ajuda com a acne e tira bem a maquiagem. Recomendo.",
      "Relevancia": 0.227490441217988
    },
    {
      "Produto": "DOUBLE SÉRUM AVANÇADO GUERLAIN ABEILLE ROYALE",
      "Marca": "GUERLAIN",
      "Review": "Hidrata sem pesar, não causou nenhuma acne e deixa a pele com muito viço. Perfeito antes da make, mesmo em dias quentes. Já estou no meu segundo frasco.",
      "Relevancia": 0.226213531833509
    }
    ]
}
```

## Tests

Para rodar os testes unitários do projeto, utilize o comando abaixo:
```bash
pytest
```

1. test_query_yields_more_10_results: Testa se a query retorna mais de 10 resultados.
2. test_query_yields_less_10_results: Testa se a query retorna menos de 10 resultados.
3. test_query_yields_non_obvious_results: Testa se a query retorna resultados não óbvios.


## Authors

Ellen Shen e Joao Magalhaes