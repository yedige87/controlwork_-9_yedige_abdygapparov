from django.urls import path

from photos.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]