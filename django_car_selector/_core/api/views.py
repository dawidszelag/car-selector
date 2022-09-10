from django.db.models import Min, Max, Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import CarFilter
from .serializers import CarSerializer, CarModelSerializer, BrandSerializer, BodySerializer, FuelTypeSerializer
from core.models import Car, CarOnTheMarket, CarBrand, CarBody


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CarAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend,)


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all().order_by('name')
    serializer_class = CarSerializer
    filterset_class = CarFilter
    filter_backends = (DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination


class CarModelAPIView(generics.ListAPIView):
    serializer_class = CarModelSerializer
    filterset_class = CarFilter
    filter_backends = (DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Car.objects.all().order_by('name')
        queryset = queryset.order_by('model__pk').values('model__id', 'model__name', 'model__brand__name',
                                                         'model__image').annotate(number_of_cars=Count('pk'))
        return queryset


class BrandCarAPIView(generics.ListAPIView):
    queryset = CarBrand.objects.all().order_by('name')
    serializer_class = BrandSerializer


class BodyCarAPIView(generics.ListAPIView):
    queryset = CarBody.objects.all().order_by('name')
    serializer_class = BodySerializer


class BudgetAPIView(APIView):
    """Return max and min car price"""
    permission_classes = (AllowAny,)

    def get(self, request):
        min_max_price = CarOnTheMarket.objects.aggregate(max_price=Max('price'), min_price=Min('price'))
        return Response(min_max_price)
