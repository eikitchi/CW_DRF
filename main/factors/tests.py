from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.test import APITestCase

from main.factors.models import Factors, Habit
from main.factors.views import FactorsUpdateAPIView
from main.users.models import User


class FactorsTestCase(APITestCase):
    def setUp(self) -> None:
        """Общие данные"""

        self.user = User.objects.create(
            email="bebra@mail.ru", password="123", is_active=True
        )
        self.user.save()
        self.habit = Habit.objects.create(
            sign_pleasant_habit="болят ноги", is_pleasant=True
        )
        self.habit.save()
        self.client.force_authenticate(user=self.user)
        self.factors_test = Factors.objects.create(
            id=10,
            plases="Пляж",
            action="Пресс",
            time="00:00",
            sign_pleasant_habit=self.habit,
            associated_habit="Тренировка рук",
            execution_time="00:01:00",
            owner=self.user
        )

    def test_create_factors(self):
        """Создание урока тест"""
        data = {
            "plases": "Пляж",
            "action": "Пресс",
            "time": "00:00",
            "sign_pleasant_habit": 1,
            "associated_habit": "Тренировка рук",
            "execution_time": "00:01:00",
            "owner": 1
        }

        response = self.client.post("/factors/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # status code
        self.assertTrue(Factors.objects.all().exists())  # нахождение в базе

    def test_list_lesson(self):
        """Вывод всех уроков тест"""
        response = self.client.get("/factors/")
        data = {'count': 1,
                'next': None,
                'previous': None,
                'results': [{'action': 'Пресс',
                             'associated_habit': 'Тренировка рук',
                             'execution_time': '00:01:00',
                             'frequency': 1,
                             'id': 10,
                             'owner': 1,
                             'plases': 'Пляж',
                             'published': True,
                             'reward': None,
                             'sign_pleasant_habit': 1,
                             'time': '00:00:00'}]}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

    def test_detail_factors(self):
        """Тест вывода инфрмании об одном уроке"""
        response = self.client.get("/factors/detail/10/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_factors(self):
        """Тест обновления урока"""
        data = {
            "plases": "Пляж",
            "action": "Пресс",
            "time": "00:00",
            "sign_pleasant_habit": 1,
            "associated_habit": "Тренировка рук",
            "execution_time": "00:02:00",
            "owner": 1,
            "frequency": 3
        }

        # Временно изменяем разрешения на AllowAny
        original_permissions = FactorsUpdateAPIView.permission_classes
        FactorsUpdateAPIView.permission_classes = [AllowAny]

        response = self.client.put("/factors/update/10/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_factors(self):
        """Тест удаления урока"""
        response = self.client.delete("/factors/delete/10/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
