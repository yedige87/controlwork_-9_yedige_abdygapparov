from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from accounts.forms import GalleryUserCreationForm, LoginForm, GalleryUserUpdateForm, GalleryUserChangePasswordForm
from photos.models import Photo


# Create your views here.
class GalleryUserRegisterView(CreateView):
    template_name = 'registration.html'
    form_class = GalleryUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            galleryuser = form.save()
            galleryuser.save()
            login(request, galleryuser)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class LoginView(SuccessMessageMixin, TemplateView):
    template_name = 'login.html'
    form = LoginForm
    success_message = 'Вы успешно зашли в систему'

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        galleryuser = authenticate(request=request, username=username, password=password)

        if not galleryuser:
            return redirect('login')

        # Login User(GalleryUser)
        login(request, galleryuser)

        return redirect('home')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile_view.html'

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        CustUser = get_user_model()
        prof_user = CustUser.objects.get(pk=id)
        self.extra_context = {'profile_owner': prof_user, 'photos': Photo.objects.all()}
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class AvatarUpdateView(UpdateView):
    model = get_user_model()
    form_class = GalleryUserUpdateForm
    template_name = 'change_avatar.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile_view', kwargs={'pk': self.object.pk})


class PasswordUpdateView(UpdateView):
    model = get_user_model()
    form_class = GalleryUserChangePasswordForm
    template_name = 'change_password.html'
    context_object_name = 'user_obj'
    # success_url = '/'

    def get_success_url(self):
        return reverse('profile_view', kwargs={'pk': self.object.pk})