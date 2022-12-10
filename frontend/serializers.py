from rest_framework import serializers
from .models import News

class SmallNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title']

class DetailNewsSerializer(serializers.ModelSerializer):
    cnt = serializers.SerializerMethodField()
    information = serializers.SerializerMethodField()
    def get_cnt(self, obj: News):
        return obj.number_of_subscribers

    def get_information(self, obj: News):
        return "some additional data"
    class Meta:
        model = News
        fields = ['id', 'title','anons', 'cnt', 'information']

