from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('/<str:pk>', views.api_update_view, name="taskUpdate"),
    path('', views.api_details_view, name="detail"),
    ]