from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('manage_users', views.manage_users, name="manage_users"),
    path('manage_payment_concept', views.manage_payment_concept, name="manage_payment_concept"),
    path('create_user/', views.create_user, name="create_user"),
    path('show_user/', views.show_user, name="show_user"),
    path('update-user/', views.update_user, name="update_user"),
    path('delete-user/', views.delete_user, name="delete_user"),
]
