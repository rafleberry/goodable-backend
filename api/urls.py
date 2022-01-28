# backend/api/urls.py

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView, PostView, TopicView
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'topics', TopicView)
router.register(r'posts', PostView)

urlpatterns = [
    path('auth/login',
         obtain_auth_token,
         name='auth_user_login'),
    path('auth/register',
         CreateUserAPIView.as_view(),
         name='auth_user_create'),
    path('auth/logout',
         LogoutUserAPIView.as_view(),
         name='auth_user_logout'),
    path('', include(router.urls))
    # path('users', UsersAPIView.as_view(), name='users')

]
