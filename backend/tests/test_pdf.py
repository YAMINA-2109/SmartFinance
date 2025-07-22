# from fastapi.testclient import TestClient
# import sys
# import os

# # Ajoute le chemin vers le dossier contenant main.py
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from main import app

# client = TestClient(app)

# sample_pdf = "tests/adh.pdf" 

# def test_status_check():
#     response = client.get("/pdf/status")
#     assert response.status_code == 200
#     assert response.json()["status"] == "ok"

# def test_upload_pdf():
#     with open(sample_pdf, "rb") as f:
#         response = client.post("/pdf/upload", files={"file": ("tests/adh.pd", f, "application/pdf")})
#     assert response.status_code == 200
#     assert "uploaded" in response.json()["message"].lower()

# def test_extract_pdf():
#     response = client.get("/pdf/extract", params={"file_name": "tests/adh.pd"})
#     assert response.status_code == 200
#     assert "content" in response.json()

# def test_summarize_pdf():
#     response = client.post("/pdf/summarize", params={"file_name": "tests/adh.pd"})
#     assert response.status_code == 200
#     assert "summary" in response.json()

# def test_qa_on_pdf():
#     payload = {
#         "filename": "tests/adh.pd",
#         "question": "Who is Yamina?",
#         "chat_history": []
#     }
#     response = client.post("/pdf/pdf/qa", json=payload)
#     assert response.status_code == 200
#     assert "answer" in response.json()

# def test_get_history():
#     response = client.get("/pdf/pdf/history")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# def test_export_history_csv():
#     response = client.get("/pdf/pdf/history/export")
#     assert response.status_code == 200
#     assert response.headers["content-type"] == "text/csv"

# def test_delete_history():
#     response = client.delete("/pdf/pdf/history")
#     assert response.status_code == 200
