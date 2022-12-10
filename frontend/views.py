from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from frontend.models import News


# Create your views here.
@csrf_exempt
def news_list(request):
    if request.method == "POST":
        if request.POST.get('title', "") == "":
            return JsonResponse({"error": "title must be not empty"},
                                status=HTTPStatus.FORBIDDEN)
        if request.POST.get('anons', "") == "":
            return JsonResponse({"error": "Anons must be not empty"},
                                status=HTTPStatus.FORBIDDEN)
        pass
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
    if request.method == 'GET':
        return JsonResponse({"success": True, "data": {
            "id": n.id,
            "title": n.title.capitalize(),
            "anons": n.anons
        }})
    if request.method == 'DELETE':
        n.delete()
        return JsonResponse(status=HTTPStatus.NO_CONTENT)
