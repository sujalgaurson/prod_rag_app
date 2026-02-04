def test_app_running(client):
    response = client.get("/docs")
    assert response.status_code == 200
