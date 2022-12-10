from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def news_list(request):
    return JsonResponse({"ok": True})


def news_one(request, news_id):
    return JsonResponse({"success": True})
