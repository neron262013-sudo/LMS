from django.urls import path

from payments.views import PaymentCreateAPIView
from payments.apps import PaymentsConfig


app_name = PaymentsConfig.name

urlpatterns = [
    path('', PaymentCreateAPIView.as_view(), name='payment_create'),
]