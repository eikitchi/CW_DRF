from django.conf import settings
from django.db import models
from django.utils import timezone

from main.factors.validators import (
    validate_related_habit_and_reward,
    validate_execution_time,
    validate_related_habit,
    validate_good_habit,
    validate_periodicity
)
from main.users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    sign_pleasant_habit = models.CharField(max_length=100, verbose_name="Признак привычки")
    is_pleasant = models.BooleanField(default=True, verbose_name="Приятная привычка")

    def __str__(self):
        return f"{self.sign_pleasant_habit}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"


class Factors(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")
    plases = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(default=timezone.now, verbose_name="Время выполнения привычки")
    action = models.CharField(max_length=100, verbose_name="Действие")
    sign_pleasant_habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    associated_habit = models.CharField(max_length=100, verbose_name="Связанная привычка")
    frequency = models.IntegerField(default=1, verbose_name="Периодичность")
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    execution_time = models.TimeField(default="00:03", verbose_name="Время на выполнение")
    published = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"Я буду {self.action} в {self.execution_time} в {self.plases}"

    def clean(self):
        """Проверка данных перед сохранением"""
        validate_related_habit_and_reward(self)
        validate_execution_time(self.execution_time)
        validate_related_habit(self)
        validate_good_habit(self)
        validate_periodicity(self.frequency)

    class Meta:
        verbose_name = "Фактор"
        verbose_name_plural = "Факторы"
