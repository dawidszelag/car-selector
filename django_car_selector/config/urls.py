"""CarSelector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.importer.views import ajax_check_upload_data_status, import_data

urlpatterns = [
    # path('api/v1/car/<int:pk>', CarAPIView.as_view()),
    # path('api/v1/cars-list', CarListAPIView.as_view()),
    # path('api/v1/models', CarModelAPIView.as_view()),
    # path('api/v1/brand', BrandCarAPIView.as_view()),
    # path('api/v1/budget', BudgetAPIView.as_view()),
    # path('api/v1/body', BodyCarAPIView.as_view()),
    path('admin/ajax/upload-data-status', ajax_check_upload_data_status, name='ajax-check-status'),
    path('admin/import-data', import_data, name='import-cars-data'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
