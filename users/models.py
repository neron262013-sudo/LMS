from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from materials.models import Course, Lesson
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, verbose_name="Почта", help_text="Введите адрес почты", unique=True)
    telephone = models.CharField(
        max_length=50, verbose_name="Телефон", help_text="Введите телефон", null=True, blank=True
    )
    city = models.CharField(max_length=100, verbose_name="Город", help_text="Введите город", null=True, blank=True)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", help_text="Загрузите ваш аватар", blank=True, null=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHODS = (
        ("cash", "Наличные"),
        ("transfer", "Перевод на счет"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Укажите пользователя"
    )
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Курс", help_text="Укажите курс"
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Урок", help_text="Укажите урок"
    )
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты", help_text="Укажите дату оплаты")
    payment_sum = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма оплаты", help_text="Укажите сумму оплаты"
    )
    payment_method = models.CharField(
        max_length=10, choices=PAYMENT_METHODS, verbose_name="Способ оплаты", help_text="Укажите способ оплаты"
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(course__isnull=False, lesson__isnull=True)
                    | models.Q(course__isnull=True, lesson__isnull=False)
                ),
                name="только курс или урок",
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.payment_sum} руб."
