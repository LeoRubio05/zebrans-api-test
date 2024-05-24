import uuid
from django.db import models


class Products(models.Model):
    product_id = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)