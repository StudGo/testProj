from rest_framework import serializers
from rest_framework import fields

from products.models import Product, ProductCategory, Basket


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField()
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum', 'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, instance):
        return Basket.objects.filter(user_id=instance.user.id).total_sum()

    def get_total_quantity(self, instance):
        return Basket.objects.filter(user_id=instance.user.id).total_quantity()

