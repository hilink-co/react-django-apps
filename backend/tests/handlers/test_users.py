import pytest
from django.http import JsonResponse
from backend.models import User


@pytest.mark.django_db
def test_get_user(client):
    user = User.objects.create(
        first_name="Barack",
        last_name="Obama",
        email="barack.obama@gmail.com",
        status=1,
    )

    response: JsonResponse = client.get("/users/{}".format(user.id))
    json: dict = response.json()

    assert json.get("first_name") == "Barack"
