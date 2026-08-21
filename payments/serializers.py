from rest_framework import serializers

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            "id",
            "course",
            "amount",
            "session_id",
            "link",
        )
        read_only_fields = (
            "id",
            "amount",
            "session_id",
            "link",
        )
        ref_name = "StripePaymentSerializer"