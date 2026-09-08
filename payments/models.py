from django.db import models

from materials.models import Course
from users.models import User


class Payment(models.Model):
    amount = models.PositiveIntegerField(verbose_name="Сумма платежа", help_text="Укажите сумму платежа")
    session_id = models.CharField(
        max_length=255, blank=True, null=True, unique=True, verbose_name="Id сессии", help_text="Укажите Id сессии"
    )
    link = models.URLField(
        max_length=1000, blank=True, null=True, verbose_name="Ссылка на оплату", help_text="Укажите ссылку на оплату"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="stripe_payments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Курс",
        help_text="Укажите курс",
        related_name="stripe_payments",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.amount} — {self.course}"
