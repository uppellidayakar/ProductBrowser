from django.db import models

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"),
        ("Books", "Books"),
        ("Clothing", "Clothing"),
        ("Home", "Home"),
        ("Sports", "Sports"),
        ("Beauty", "Beauty"),
    ]

    name = models.CharField(max_length=255)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField()

    updated_at = models.DateTimeField()

    class Meta:
        ordering = ["-created_at", "-id"]
        indexes = [
            models.Index(fields=["-created_at", "-id"]),
            models.Index(fields=["category"]),
            models.Index(fields=["category", "-created_at", "-id"]),
        ]

    def __str__(self):
        return self.name