from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


# Register your models here.
@admin.register(MainInfo)
class MainAdmin(admin.ModelAdmin):
    list_display = ('desc_rus', 'desc_eng', 'phone', 'email', 'telegram_nick')
    search_fields = ('desc_rus', 'desc_eng')


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'body', 'get_tags', 'date_pubs')
    search_fields = ('title', 'body')
    summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')


@admin.register(UniversitySubject)
class UniversitySubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'date_upload', 'subject')
    search_fields = ('title',)
