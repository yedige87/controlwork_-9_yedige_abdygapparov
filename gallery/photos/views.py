from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from photos.forms import PhotoForm
from photos.models import Photo


# Create your views here.
class HomeView(ListView):
    model = Photo
    template_name = 'index.html'
    context_object_name = 'photos'
    ordering = ('-created_at',)


class PhotoCreateView(CreateView):
    model = Photo  # Указываем модель
    form_class = PhotoForm
    template_name = 'photo_create.html'  # Путь к шаблону формы создания
    success_url = reverse_lazy('home')  # URL, на который будет перенаправление после успешного создания объекта

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if 'blank' in form.instance.photo:
            return redirect('home')
        form.instance.author = self.request.user  # Устанавливаем текущего пользователя как автора
        return super().form_valid(form)


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'
    context_object_name = 'photo'


class PhotoUpdateView(UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    success_message = 'Фото обновлено!'

    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=kwargs['pk'])
        if request.user != photo.author:
            return reverse('photo_detail', kwargs={'pk': photo.pk})
        if not request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    success_url = reverse_lazy('home')
    success_message = 'Фото удалено!'


def like_unlike(request, pk):
    curr_user = request.user
    if not curr_user.is_authenticated:
        return redirect('home')
    photo = Photo.objects.get(pk=pk)
    if curr_user in photo.likers.all():
        photo.likers.remove(curr_user)
    else:
        photo.likers.add(curr_user)
    photo.save()
    return redirect('home')


def unfavor(request, pk):
    curr_user = request.user
    if not curr_user.is_authenticated:
        return redirect('home')
    photo = Photo.objects.get(pk=pk)
    if curr_user in photo.likers.all():
        photo.likers.remove(curr_user)
        photo.save()
    return reverse('profile_view', kwargs={'pk': curr_user.pk})