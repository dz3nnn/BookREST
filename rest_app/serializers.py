from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Author, Book,  Review


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
