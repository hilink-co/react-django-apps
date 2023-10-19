import pytest
from django.http import JsonResponse


def test_healthcheck(client):
    response: JsonResponse = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
