from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_mail_about_course_update(course_id):
    """Отправляет сообщение подписанным на курс пользователям о его обновлении."""
    course = Course.objects.get(pk=course_id)
    subscriptions = Subscription.objects.filter(course=course)

    message = f'Курс "{course.name}" был обновлён.'

    for subscription in subscriptions:
        send_mail(
            subject="Обновление курса",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
        )


@shared_task
def check_inactive_users():
    today = timezone.localdate()
    users = User.objects.all()
    for user in users:
        if user.last_login and user.is_active:
            inactive = today - user.last_login.date()
            if inactive > timedelta(days=30):
                user.is_active = False
                user.save()
