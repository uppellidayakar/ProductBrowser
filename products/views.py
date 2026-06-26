from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductCursorPagination


class ProductListView(generics.ListAPIView):

    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination

    def get_queryset(self):

        queryset = Product.objects.only(
            "id",
            "name",
            "category",
            "price",
            "created_at",
            "updated_at",
        ).order_by("-created_at", "-id")

        category = self.request.query_params.get("category")

        if category:
            queryset = queryset.filter(category=category)

        return queryset