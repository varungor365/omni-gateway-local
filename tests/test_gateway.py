from unittest.mock import patch

from fastapi.testclient import TestClient

from omni_gateway.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch("omni_gateway.main.litellm.completion")
def test_chat_completions(mock_completion):
    # Mock the return value of litellm
    class MockResponse:
        def model_dump(self):
            return {"choices": [{"message": {"content": "Hello!"}}]}
    mock_completion.return_value = MockResponse()
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "Hi"}]
    }
    
    response = client.post("/v1/chat/completions", json=payload)
    assert response.status_code == 200
    assert response.json() == {"choices": [{"message": {"content": "Hello!"}}]}
    mock_completion.assert_called_once()
