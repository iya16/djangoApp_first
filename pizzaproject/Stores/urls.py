from django.urls import path
from .import views

urlpatterns=[
    path('', views.pizzeriaListAPIView.as_view(), name="pizzeria_list" ),
    path('<int:id>/', views.pizzeriaRetrieveAPIView.as_view(), name='pizzeria_detail'),
    path('create/', views.pizzeriaCreateAPIView.as_view(), name="pizzeria_create"),
    path('update/<int:id>/', views.pizzeriaRetrieveUpdateAPIView.as_view(), name='pizzeria_update'),
    path('delete/<int:id>/', views.pizzeriaDestroyAPIView.as_view(), name='pizzeria_delete'),


    ]