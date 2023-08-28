from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from main.factors.models import Factors
from main.factors.paginators import FactorsPaginator
from main.factors.serializers import FactorsCreateSerializer, FactorsSerializer


class FactorsCreateAPIView(generics.CreateAPIView):
    """Factors Create"""
    serializer_class = FactorsCreateSerializer
    permission_classes = [AllowAny]  # AllowAny # IsAuthenticated

    def perform_create(self, serializer):  # сохранения нового владельца
        new_foctors = serializer.save()
        new_foctors.owner = self.request.user  # owner - владелец  (нужно добавить в models)
        new_foctors.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Регистрация пользователя успешна'}, status=status.HTTP_200_OK)


class FactorsListAPIView(generics.ListAPIView):
    """Factors List"""
    serializer_class = FactorsSerializer
    queryset = Factors.objects.all()
    permission_classes = [AllowAny]   # AllowAny # IsAuthenticated
    pagination_class = FactorsPaginator

    def get_queryset(self):
        return Factors.objects.filter(owner=self.request.user)


class PublicFactorsAPIView(generics.ListAPIView):
    serializer_class = FactorsSerializer

    def get_queryset(self):
        return Factors.objects.filter(is_public=True)


class FactorsRetrieveAPIView(generics.RetrieveAPIView):
    """Factors Retrive"""
    serializer_class = FactorsSerializer
    queryset = Factors.objects.all()
    permission_classes = [AllowAny]  # AllowAny # IsAuthenticated


class FactorsUpdateAPIView(generics.UpdateAPIView):
    """Factors Updaate"""
    serializer_class = FactorsSerializer
    queryset = Factors.objects.all()
    permission_classes = [AllowAny]   # AllowAny # IsAuthenticated

    def get_queryset(self):
        return Factors.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):
        habit = self.get_object()
        serializer = self.get_serializer(habit, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': "Привычка успешно отредактирована"})


class FactorsDestroyAPIView(generics.DestroyAPIView):
    """Factors Delete"""
    queryset = Factors.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Factors.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        habit = self.get_object()
        self.perform_destroy(habit)
        return Response({'message': 'Привычка успешно удаленна'})


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'access_token': token.key})


