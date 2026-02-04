import os
from app.core.config import FAISS_INDEX_PATH

def test_session_end_deletes_faiss_index(client):
    # Upload first
    client.post(
        "/upload",
        files={"file": ("doc.txt", b"FAISS is a vector database", "text/plain")}
    )

    assert os.path.exists(FAISS_INDEX_PATH)

    # End session
    response = client.delete("/session/end")

    assert response.status_code == 200
    assert not os.path.exists(FAISS_INDEX_PATH)
