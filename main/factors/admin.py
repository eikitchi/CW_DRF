from django.contrib import admin

from main.factors.models import Factors, Habit


# Register your models here.
@admin.register(Factors)
class FactorsAdmin(admin.ModelAdmin):
    list_display = ("plases", "action", "sign_pleasant_habit", "associated_habit",
                    "reward", "time", "execution_time")  # отображение на дисплее
    list_filter = ("plases", "action", "sign_pleasant_habit", "associated_habit",
                   "reward", "time", "execution_time")  # фильтр
    search_fields = ("plases", "action", "sign_pleasant_habit", "associated_habit",
                     "reward", "time", "execution_time")  # поля поиска


@admin.register(Habit)
class Habitdmin(admin.ModelAdmin):
    list_display = ("sign_pleasant_habit",
                    "is_pleasant")
    list_filter = ("sign_pleasant_habit",
                   "is_pleasant")
    search_fields = ("sign_pleasant_habit",
                     "is_pleasant")

