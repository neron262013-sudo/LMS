from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    http_method_names = ["get", "put", "patch", "delete", "head", "options"]

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Используйте эндпоинт /register/ для регистрации."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    ordering_fields = ("payment_date",)
    filterset_fields = ("course", "lesson", "payment_method")


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        AllowAny,
    ]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
