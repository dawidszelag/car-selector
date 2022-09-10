from rest_framework import serializers

from core.models import Car, CarOnTheMarket, CarImage, CarModel, CarBrand, CarBody


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ('pk', 'image')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOnTheMarket
        fields = ['price', 'market']
        depth = 1


class CarSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True)
    images = CarImageSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'
        depth = 2


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.Serializer):
    id = serializers.CharField(source='model__id')
    brand = serializers.CharField(source='model__brand__name')
    name = serializers.CharField(source='model__name')
    image = serializers.URLField(source='model__image')
    number_of_cars = serializers.IntegerField(allow_null=True)


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBody
        fields = '__all__'


class FuelTypeSerializer(serializers.Serializer):
    name = serializers.CharField(source='fuel_type')
