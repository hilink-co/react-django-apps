from django.http import JsonResponse
from backend.models import User


def get_user(request, user_id: int) -> JsonResponse:
    user = User.objects.get(id=user_id)
    return JsonResponse({"first_name": user.first_name, "last_name": user.last_name})
