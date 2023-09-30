from django.urls import path

from accounts.views import GalleryUserRegisterView, LoginView, LogoutView, ProfileView, AvatarUpdateView, \
    PasswordUpdateView

urlpatterns = [
    path('accounts/register', GalleryUserRegisterView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/<int:pk>/profile', ProfileView.as_view(), name='profile_view'),
    path('accounts/<int:pk>/avatar_update', AvatarUpdateView.as_view(), name='avatar_update'),
    path('accounts/<int:pk>/password_update', PasswordUpdateView.as_view(), name='password_update'),
]