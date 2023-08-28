from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from main.users.apps import UsersConfig
from main.users.views import UserDestroyAPIView, UserCreateAPIView, UserListAPIView, UserUpdateAPIView, \
    UserRetrieveAPIView

app_name = UsersConfig.name
"""
Создание урлов для авторизации
"""
urlpatterns = [
    #Users
    path("factors/create/", UserCreateAPIView.as_view(), name="factors_create"),
    path("factors/", UserListAPIView.as_view(), name="factors_list"),
    path("factors/detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="factors_detail"),
    path("factors/update/<int:pk>/", UserUpdateAPIView.as_view(), name="factors_update"),
    path("factors/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="factors_delete"),

    #Token
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
