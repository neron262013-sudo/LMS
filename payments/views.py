from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from payments.models import Payment
from payments.serializers import PaymentSerializer
from payments.services import create_payment_session


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        course = serializer.validated_data["course"]
        session_id, payment_link = create_payment_session(course)
        serializer.save(
            user=self.request.user,
            amount=course.price,
            session_id=session_id,
            link=payment_link,
        )