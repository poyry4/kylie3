from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.loginView, name="login"),
    path('category_create', views.category_create, name="category_create"),
    path('adminKylie', views.adminKylie, name="adminKylie"),
    path('logout/', views.logoutView, name="logout"),
]