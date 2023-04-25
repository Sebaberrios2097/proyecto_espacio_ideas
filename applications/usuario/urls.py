from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, login_view, logout_view

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('registrate/', UserCreateView.as_view(), name='user_register'),
    path('login/', login_view, name='user_login'),
    path('logout/', logout_view, name='user_logout'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
