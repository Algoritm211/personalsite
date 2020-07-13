from django import forms

from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Такая ссылка не может быть создана')
        # if Tag.objects.filter(slug__iexact=new_slug).count():  # Не отличная от нуля длина списка по фильтру
        #     raise ValidationError('Такая ссылка уже существует на сайте, введите другую')
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-group'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Такая ссылка не может быть создана')
        # if Post.objects.filter(slug__iexact=new_slug).count():  # Не отличная от нуля длина списка по фильтру
        #     raise ValidationError('Такая ссылка уже существует на сайте, введите другую')
        return new_slug


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('title', 'file', 'subject')

        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': False})
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = UniversitySubject
        fields = ('title', 'slug')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Такая ссылка не может быть создана')
        # if Post.objects.filter(slug__iexact=new_slug).count():  # Не отличная от нуля длина списка по фильтру
        #     raise ValidationError('Такая ссылка уже существует на сайте, введите другую')
        return new_slug
