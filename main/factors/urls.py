from django.urls import path
from rest_framework.routers import DefaultRouter

from main.factors.apps import FactorsConfig
from main.factors.views import FactorsDestroyAPIView, FactorsUpdateAPIView, FactorsRetrieveAPIView, FactorsListAPIView, \
    FactorsCreateAPIView

app_name = FactorsConfig.name

router = DefaultRouter()

# все для Generic
urlpatterns = [
    # Factors
    path("factors/create/", FactorsCreateAPIView.as_view(), name="factors_create"),
    path("factors/", FactorsListAPIView.as_view(), name="factors_list"),
    path("factors/detail/<int:pk>/", FactorsRetrieveAPIView.as_view(), name="factors_detail"),
    path("factors/update/<int:pk>/", FactorsUpdateAPIView.as_view(), name="factors_update"),
    path("factors/delete/<int:pk>/", FactorsDestroyAPIView.as_view(), name="factors_delete"),

] + router.urls
