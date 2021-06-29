from rest_framework import serializers
from .models import DiscountCode
from django.core.exceptions import ValidationError


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = [
            'created_date',
            'modified_date',
            'created_by',
            'modified_by',
            'code',
            'start_date',
            'expire_date',
            'customer_id',
            'limited_usage_count',
            'usage_count',
            'active'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start_date'] >= data['expire_date']:
            raise ValidationError('expire date must be after start date')
        return data
