from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList),
    path('users/<int:pk>/', views.UserDetail),
    ]