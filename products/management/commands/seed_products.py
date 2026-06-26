from django.core.management.base import BaseCommand
from django.utils import timezone
from products.models import Product

import random
from decimal import Decimal
from datetime import timedelta


class Command(BaseCommand):
    help = "Generate 200,000 sample products"

    def handle(self, *args, **kwargs):

        # Delete existing products
        self.stdout.write("Deleting existing products...")
        Product.objects.all().delete()

        categories = [
            "Electronics",
            "Books",
            "Clothing",
            "Home",
            "Sports",
            "Beauty",
        ]

        total_products = 200000
        batch_size = 5000
        now = timezone.now()

        self.stdout.write("Generating products...")

        for start in range(0, total_products, batch_size):

            products = []

            for i in range(start, min(start + batch_size, total_products)):

                created_time = now - timedelta(
                    days=random.randint(0, 365)
                )

                updated_time = created_time + timedelta(
                    days=random.randint(0, 30)
                )

                price = Decimal(random.randint(100, 100000)) / 100

                products.append(
                    Product(
                        name=f"Product {i + 1}",
                        category=random.choice(categories),
                        price=price,
                        created_at=created_time,
                        updated_at=updated_time,
                    )
                )

            Product.objects.bulk_create(
                products,
                batch_size=batch_size
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Inserted {start + len(products)} / {total_products}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully generated 200,000 products!"
            )
        )