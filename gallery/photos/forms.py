from django import forms

from photos.models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', 'description')
        labels = {
            'photo': 'Фото',
            'description': 'Описание',
        }