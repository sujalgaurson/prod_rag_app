import os
from app.core.config import FAISS_INDEX_PATH

def test_file_upload_creates_faiss_index(client):
    file_path = "tests/sample.txt"

    with open(file_path, "w") as f:
        f.write("RAG stands for Retrieval Augmented Generation.")

    with open(file_path, "rb") as f:
        response = client.post(
            "/upload",
            files={"file": ("sample.txt", f, "text/plain")}
        )

    assert response.status_code == 200

    assert os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.faiss"))
    assert os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.pkl"))

    os.remove(file_path)
