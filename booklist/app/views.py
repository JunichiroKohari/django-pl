import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import ReadHistory

@csrf_exempt
def insert_log(request):
    d = json.loads(request.body)
    ReadHistory.objects.create(
        name=d["name"],
        category=d["category"],
        title=d["title"],
        price=d["price"],
        read_at=d["readAt"],
        is_public=d["isPublic"],
        is_favorite=d["isFavorite"],
    )
    return JsonResponse({})