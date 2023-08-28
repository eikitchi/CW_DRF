from datetime import timedelta
from django.core.exceptions import ValidationError


def validate_related_habit_and_reward(value):
    """Валидатор - "Нельзя одновременно выбрать связанную привычку и указание вознаграждения."""
    if value.associated_habit and value.reward:
        raise ValidationError(
            'Нельзя выбрать связанную привычку и указать вознаграждение одновременно.')

def validate_execution_time(execution_time):
    """Валидатор Время выполнения не может быть больше 120 секунд."""
    max_execution_time = timedelta(seconds=120)
    execution_time_timedelta = timedelta(
        hours=execution_time.hour,
        minutes=execution_time.minute,
        seconds=execution_time.second,
    )

    if execution_time_timedelta > max_execution_time:
        raise ValidationError("Время выполнения не может быть больше 120 секунд.")

def validate_related_habit(value):
    """Валидатор - В связанные привычки могут попадать только привычки с признаком приятной привычки"""
    if value.is_pleasant and not value.relted_habbit.good_habit_sign:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


def validate_good_habit(habit):
    """Валидатор - У приятной привычки не может быть вознаграждения или связанной привычки"""
    if habit.is_pleasant and habit.associated_habit or habit.reward:
        raise ValidationError('Приятная привычка не может иметь связанной привычки или вознаграждения.')


def validate_periodicity(frequency):
    """Валидатор -Привычку нельзя выполнять реже, чем 1 раз в 7 дней."""
    min_periodicity_days = 7
    if frequency > min_periodicity_days:
        raise ValidationError('Привычку нельзя выполнять реже, чем 1 раз в 7 дней.')



