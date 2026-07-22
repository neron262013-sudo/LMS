from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.object.all()
    serializer_class = CourseSerializer


class LessonCreateApiView(CreateAPIView):
    queryset = Course.object.all()
    serializer_class = LessonSerializer


class LessonListAPIView(CreateAPIView):
    queryset = Course.object.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(CreateAPIView):
    queryset = Course.object.all()
    serializer_class = LessonSerializer


class LessonUpdateApiView(CreateAPIView):
    queryset = Course.object.all()
    serializer_class = LessonSerializer


class LessonDestroyApiView(CreateAPIView):
    queryset = Course.object.all()
    serializer_class = LessonSerializer
