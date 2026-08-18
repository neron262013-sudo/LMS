from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group

from materials.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="admin@sky.pro", password="password123")
        self.course = Course.objects.create(name="Курс 1", owner=self.user)
        self.lesson = Lesson.objects.create(name="Урок 1", owner=self.user,
                                            video_url="https://youtube.com")
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "name": "Тест 2",
            "description": "Описание тест 2",
            "video_url": "https://youtube.com"  # Добавили валидный URL
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "Тест апдейт",
            "description": "Описание апдейт",
            "video_url": "https://youtube.com"
        }
        response = self.client.put(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Тест апдейт"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lessons_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "description": self.lesson.description,
                    "video_url": self.lesson.video_url,
                    "name": self.lesson.name,
                    "preview": None,
                    "course": None,
                    "owner": self.lesson.owner.pk,
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_course_create_by_moderator_forbidden(self):
        moder_group = Group.objects.create(name="moders")
        moder_user = User.objects.create_user(email="moder@sky.pro", password="password123")
        moder_user.groups.add(moder_group)

        self.client.force_authenticate(user=moder_user)

        url = reverse("materials:course-list")
        data = {
            "name": "Курс от модератора",
            "description": "Описание курса"
        }

        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_course_delete_by_moderator_forbidden(self):
        moder_group = Group.objects.create(name="moders")
        moder_user = User.objects.create_user(email="moder_del@sky.pro", password="password123")
        moder_user.groups.add(moder_group)

        self.client.force_authenticate(user=moder_user)

        url = reverse("materials:course-detail", args=(self.course.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_course_delete_by_not_owner_forbidden(self):
        other_user = User.objects.create_user(email="other@sky.pro", password="password123")

        self.client.force_authenticate(user=other_user)
        url = reverse("materials:course-detail", args=(self.course.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND
        )


    def test_course_subscription(self):
        url = reverse("materials:course_subscribe")
        data = {
            "course_id": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json().get("message"), "подписка добавлена"
        )
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json().get("message"), "подписка удалена"
        )
