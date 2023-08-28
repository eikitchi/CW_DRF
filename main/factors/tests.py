from rest_framework import status
from rest_framework.test import APITestCase

from main.factors.models import Factors, Habit
from main.users.models import User


class LessonTestCase(APITestCase):
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
            id=2,
            plases="Пляж",
            action="Пресс",
            time_of_necessity=4,
            sign_pleasant_habit=self.habit,
            associated_habit="Тренировка рук",
            time_to_execute="75",
            owner=self.user
        )

    def test_create_factors(self):
        """Создание урока тест"""
        data = {
            "plases": "Пляж",
            "action": "Пресс",
            "time_of_necessity": 4,
            "sign_pleasant_habit": 1,
            "associated_habit": "Тренировка рук",
            "time_to_execute": 75,
            "owner": 1
        }

        response = self.client.post("/factors/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # status code
        self.assertTrue(Factors.objects.all().exists())  # нахождение в базе

    # def test_list_lesson(self):
    #     """Вывод всех уроков тест"""
    #     response = self.client.get("/factors/list/")
    #     data = {
    #         "count": 1,
    #         "next": None,
    #         "previous": None,
    #         "results": [
    #             {
    #                 "id": 2,
    #                 "plases": "Пляж",
    #                 "action": "Пресс",
    #                 "time_of_necessity": 4,
    #                 "pleasant_habit": "Боль мышц",
    #                 "associated_habit": "Тренировка рук",
    #                 "frequency": (4, 'Раз в день'),
    #                 "reward": None,
    #                 "time_to_execute": 75,
    #                 "published": True,
    #                 "owner": 1
    #             }
    #         ],
    #     }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

    def test_detail_factors(self):
        """Тест вывода инфрмании об одном уроке"""
        response = self.client.get("/factors/detail/2/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_factors(self):
    #     """Тест обновления урока"""
    #     data = {
    #         "places": "Пляж",
    #         "time_of_necessity": 5,
    #         "action": "Пресс",
    #         "pleasant_habit": "Боль мышц и тренировка рук",
    #         "associated_habit": "Тренировка рук",
    #         "frequency": "(1, 'Раз в день')",
    #         "time_to_execute": "10:22:00",
    #         "published": True,
    #         "owner": 1
    #     }

        # response = self.client.put("/factors/update/2/", data=data)
        #
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_factors(self):
        """Тест удаления урока"""
        response = self.client.delete("/factors/delete/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
