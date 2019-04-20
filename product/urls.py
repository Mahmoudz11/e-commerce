from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_list, name ='category-list'),
    path('<str:slug>/', views.category_detail, name='category-detail'),
    path('<str:slug>/<str:local_slug>/', views.local_category_detail, name='local-category-detail'),
    path('<str:slug>/<str:local_slug>/<str:local_type>/', views.local_types, name='local-types-detail'),
    path('<str:slug>/<str:local_slug>/<str:local_type>/<str:product_slug>/', views.product_detail, name='product-detail'),

]
