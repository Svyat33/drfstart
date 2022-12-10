from rest_framework import serializers
from .models import News, Comment


class SmallNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title']

class CommentsSerializer(serializers.ModelSerializer):
    news_link = serializers.HyperlinkedIdentityField(many=False, read_only=True, view_name='news-detail')
    class Meta:
        model=Comment
        fields = ['text', 'news_link']

class DetailNewsSerializer(serializers.ModelSerializer):
    cnt = serializers.SerializerMethodField()
    information = serializers.SerializerMethodField()
    comments = CommentsSerializer()
    def get_cnt(self, obj: News):
        return obj.number_of_subscribers

    def get_information(self, obj: News):
        return "some additional data"
    class Meta:
        model = News
        fields = ['id', 'title','anons', 'cnt', 'information']

