from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('manage_users', views.manage_users, name="manage_users"),
    path('manage_payment_concept', views.manage_payment_concept, name="manage_payment_concept"),
    path('create-user/', views.createUser, name="create-user"),
]
