from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookSerializer, UserSerializer, GroupSerializer, AuthorSerializer, ReviewSerializer
from rest_framework.response import Response
from .models import Author, Book, Review


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """

    def list(self, request):
        queryset = Review.objects.filter()
        serializer = ReviewSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
