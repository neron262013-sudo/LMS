from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("payments", PaymentViewSet, basename="payments")

urlpatterns = []

urlpatterns += router.urls
