import base64
import json

# Комментарий: проверка claims ловит баги в точке выпуска токена
# (type=refresh, exp в прошлом, пустой sub) — до того, как /protected
# упадёт на них с непонятной 401 в другом тесте.

def test_access_token_payload(client, valid_credentials):
    response = client.post("/auth/login", json=valid_credentials)
    access_token = response.json()["access_token"]

    part = access_token.split(".")[1]
    part += "=" * (-len(part) % 4)
    payload = json.loads(base64.urlsafe_b64decode(part))

    assert payload["type"] == "access"
    assert payload["exp"] > payload["iat"]
    assert payload["sub"] 
    assert response.status_code == 200, response.text