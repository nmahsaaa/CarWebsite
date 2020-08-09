from . import views
from django.urls import path
from .views import(
    index,
    checkout,
    product,
    store
)
app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('store', views.store, name='store'),

]