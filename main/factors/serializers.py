from rest_framework import serializers

from main.factors.models import Factors


class FactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factors
        fields = "__all__"


class FactorsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factors
        fields = "__all__"

    def create(self, validated_data):
        factors_item = Factors.objects.create(**validated_data)
        return factors_item

