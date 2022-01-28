from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.decorators import action, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, permissions
from rest_framework.views import APIView
from api.serializers import CreateUserSerializer, PostSerializer, TopicSerializer
from .models import Topic, Post
import logging

logger = logging.getLogger(__name__)


class TopicView(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all().order_by('name')
    serializer_class = TopicSerializer

    @action(detail=False)
    def my_list(self, request):
        user = request.user
        queryset = user.topic_set
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)


class PostView(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by('-posted_date')
    serializer_class = PostSerializer


class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        token = Token.objects.create(user=serializer.instance)
        token_data = {"token": token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
