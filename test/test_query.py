from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_yields_10_results():
    response = client.get("/query?query=acne")
    json_response = response.json()
    
    assert response.status_code == 200
    assert len(json_response["results"]) == 10
    assert json_response["message"] == "OK"

def test_query_yields_few_results():
    response = client.get("/query?query=seco")
    json_response = response.json()
    
    assert response.status_code == 200
    assert 1 < len(json_response["results"]) < 10
    assert json_response["message"] == "OK"

def test_query_yields_non_obvious_results():
    response = client.get("/query?query=manchas na pele")
    json_response = response.json()
    
    assert response.status_code == 200
    assert len(json_response["results"]) > 0
    assert json_response["results"][0]["title"] == "SÉRUM ILUMINADOR ANTIMANCHAS CAUDALIE VINOPERFECT ALTERNATIVA À VITAMINA C"
    assert json_response["results"][1]["title"] == "ESPUMA DE LIMPEZA SHISEIDO DEEP CLEANSING FOAM"
    assert json_response["results"][2]["title"] == "ESSÊNCIA DE TRATAMENTO CLARINS EXTRA-FIRMING"
    assert json_response["results"][3]["title"] == "SÉRUM HIDRATANTE DRUNK ELEPHANT B-HYDRA INTENSIVE HYDRATION SERUM"
    assert json_response["results"][3]["title"] == "CREME HIDRATANTE FACIAL DRUNK ELEPHANT PROTINI POLYPEPTIDE CREAM"
    assert json_response["message"] == "OK"
