from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import validate_forbidden_links


class LessonSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validate_forbidden_links])
    video_url = serializers.URLField(validators=[validate_forbidden_links])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons_in_course = LessonSerializer(source="lesson_set", many=True, read_only=True)
    description = serializers.CharField(validators=[validate_forbidden_links])

    def get_number_of_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = "__all__"
