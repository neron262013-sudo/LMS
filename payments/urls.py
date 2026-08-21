from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import PaymentCreateAPIView

app_name = PaymentsConfig.name

urlpatterns = [
    path("", PaymentCreateAPIView.as_view(), name="payment_create"),
]
