from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions

from frontend.forms import NewsForm
from frontend.models import News, Comment
from frontend.permissions import OnlyAdminCanModify
from frontend.serializers import SmallNewsSerializer, DetailNewsSerializer, CommentsSerializer


# Create your views here.
@csrf_exempt
def news_list(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.session['step1'] = data

    ret = []
    if 'cnt' not in request.session:
        request.session['cnt'] = 1
    else:
        request.session['cnt'] += 1

    all_news = News.objects.filter(approved=True).order_by('-title')
    return JsonResponse({"ok": True, "data": SmallNewsSerializer(all_news, many=True).data})


def news_one(request, news_id):
    n = get_object_or_404(News, pk=news_id, approved=True)
    if request.method == 'GET':
        return JsonResponse({"success": True, "data": DetailNewsSerializer(n, many=False).data})
    if request.method == 'DELETE':
        n.delete()
        return JsonResponse(status=HTTPStatus.NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [OnlyAdminCanModify, ]

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(approved=True).order_by('id')
    serializer_class = DetailNewsSerializer
    permission_classes = [OnlyAdminCanModify,]

    def get_queryset(self):
        # self.request.GET
        # self.request.user
        return News.objects.filter()

    def get_serializer_class(self):
        return DetailNewsSerializer

    # def get_serializer(self, *args, **kwargs):
