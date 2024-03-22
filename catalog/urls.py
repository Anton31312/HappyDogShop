from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
     path('', views.home_page, name='home'),
     path('contact/', views.contact_page, name='contact'),
     path('product_info/<int:pk>', views.product_info, name='product_info'),
]