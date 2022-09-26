from django.urls import path
from apps.users.api.api import UserAPIView, user_api_view, user_detail_view

urlpatterns = [
    path('usuario', UserAPIView.as_view(), name='usuario_api'),
    path('api_funtion', user_api_view, name='usuario_api_function'),
    path('usuario/api_detail_funtion/<int:pk>/', user_detail_view, name='usuario_api_detail_function'),
]
