from django.urls import path

from photos.views import HomeView, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView, like_unlike, \
    unfavor

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('photo_create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo_detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo_update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo_delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/confirm_delete/', PhotoDeleteView.as_view(), name='confirm_delete'),
    path('favor/<int:pk>/', like_unlike, name='like_unlike'),
    path('favor/<int:pk>/', unfavor, name='unfavor'),
]