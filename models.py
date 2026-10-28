from django.db import models


class Order(models.Model):

    ORDER_STATUS = [
        ("Pending", "Pending"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready"),
        ("Served", "Served"),
    ]

    order_id = models.AutoField(primary_key=True)

    table_number = models.IntegerField()

    customer_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    items = models.TextField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"Order #{self.order_id} | "
            f"Table {self.table_number} | "
            f"{self.status}"
        )