import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from app.models import ReadHistory

def index(request):
    context = {}
    return render(request, "app/index.html", context)

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

@csrf_exempt
def read_log(request):
    qs = ReadHistory.objects.filter(is_public=True).order_by("-id")
    d = [{
        "id": obj.id,
        "name": obj.name,
        "category": obj.category,
        "title": obj.title,
        "price": obj.price,
        "readAt": obj.read_at.strftime("%Y-%m-%d"),
        "isFavorite": obj.is_favorite,
    } for obj in qs]
    return JsonResponse({"result": d})