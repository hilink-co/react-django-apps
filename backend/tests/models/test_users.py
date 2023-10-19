from django.test import TestCase
from backend.models import User


class TestUser(TestCase):
    def test_user(self):
        user = User.objects.create(
            first_name="Barack",
            last_name="Obama",
            email="barack.obama@gmail.com",
            status=1,
        )

        assert user.first_name == "Barack"
