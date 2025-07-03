from django.urls import path
from . import views
from .views import UserAPI,UpdateUserAPI,RegisterUserAPI,LoginUserAPI

urlpatterns = [
    # path('', views.user, name = 'user')
    path('', UserAPI.as_view(), name = 'user'),
    path('update/<str:id>/', UpdateUserAPI.as_view(), name='Update User'),
    path('register/', RegisterUserAPI.as_view(), name = 'Register User'),
    path('login/', LoginUserAPI.as_view(), name = 'Login User')
]