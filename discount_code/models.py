import uuid

from django.db import models
from django.core.exceptions import ValidationError


class DiscountCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=36)
    modified_by = models.CharField(max_length=36)
    code = models.CharField(max_length=12)
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    customer_id = models.CharField(max_length=36)
    limited_usage_count = models.IntegerField(default=1)
    usage_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        db_table = 'discount_codes'

    def clean(self):
        if self.start_date >= self.expire_date:
            raise ValidationError('expire date must be after start date')
