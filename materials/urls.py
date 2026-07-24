from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView, LessonDestroyApiView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateApiView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"),
]

urlpatterns += router.urls
