from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса", help_text="Укажите название курса")
    preview = models.ImageField(
        upload_to="materials/course_previews",
        verbose_name="Превью",
        help_text="Загрузите превью",
        blank=True,
        null=True,
    )
    description = models.TextField(verbose_name="Описание", help_text="Укажите описание курса", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название урока", help_text="Укажите название урока")
    preview = models.ImageField(
        upload_to="materials/lessons_previews",
        verbose_name="Превью",
        help_text="Загрузите превью",
        blank=True,
        null=True,
    )
    description = models.TextField(verbose_name="Описание", help_text="Укажите описание урока", blank=True, null=True)
    video_url = models.URLField(
        verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео", blank=True, null=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Укажите из какого курса урок",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
