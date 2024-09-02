# NLP APS1

Skincare API

## Description

This project is a simple API that uses NLP to recommend skincare products based on the user's skin type and concerns. The API uses a pre-trained BERT model to classify the user's skin type and concerns and then uses a simple recommendation system to recommend products based on the user's skin type and concerns. The API is built using the FastAPI framework and the Hugging Face Transformers library. 


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
http://0.0.0.0:8000/query?query=acne

## Output

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
## Authors

Ellen Shen e Joao Magalhaes