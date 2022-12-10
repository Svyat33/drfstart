from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from frontend.models import News


# Create your views here.
def news_list(request):

    ret = []

    for n in News.objects.filter(approved=True):
        ret.append({
            "id": n.id,
            "title": n.title.capitalize(),
            "anons": n.anons
        })

    return JsonResponse({"ok": True, "data": ret})


def news_one(request, news_id):
    n = get_object_or_404(News, pk=news_id, approved=True)
    return JsonResponse({"success": True, "data": {
            "id": n.id,
            "title": n.title.capitalize(),
            "anons": n.anons
        }})
