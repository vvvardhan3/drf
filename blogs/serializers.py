from rest_framework import serializers
from .models import Blog, Comment


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class Blogserializer(serializers.ModelSerializer):

    comments = Commentserializer(many=True, read_only = True)

    class Meta:
        model = Blog
        fields = '__all__'