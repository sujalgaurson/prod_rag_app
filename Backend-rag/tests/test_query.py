def test_query_after_upload(client):
    # Upload file
    file_content = b"LangChain is used to build RAG systems."

    upload_response = client.post(
        "/upload",
        files={"file": ("doc.txt", file_content, "text/plain")}
    )

    assert upload_response.status_code == 200

    # Query
    response = client.post(
        "/query",
        params={"question": "What is LangChain?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert isinstance(data["answer"], str)
    assert len(data["answer"]) > 0
