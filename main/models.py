from django.db import models
from django.shortcuts import reverse


# Create your models here.

class MainInfo(models.Model):
    desc_rus = models.TextField(blank=True, verbose_name='Описание на русском')
    desc_eng = models.TextField(blank=True, verbose_name='Описание на английском')
    phone = models.CharField(max_length=25, blank=True, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    telegram_nick = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Данные о владельце'
        verbose_name_plural = 'Данные о владельце'


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок поста')
    slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name='Ссылка')
    body = models.TextField(blank=True, db_index=True, verbose_name='Тело поста')
    date_pubs = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Тэг')

    def get_tags(self):
        return ','.join([str(item) for item in self.tags.all()])

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Заголовок тэга')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


# class WorkPost(models.Model):
#     title = models.CharField(max_length=90, db_index=True, verbose_name='Заголовок поста')
#     slug = models.SlugField(max_length=90, blank=True, unique=True, verbose_name='Ссылка')
#     date_pubs = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
#     files = models.ManyToManyField('File', blank=True, related_name='posts', verbose_name='Привязанные файлы')
#
#     class Meta:
#         verbose_name = 'Запись KPIWORK'
#         verbose_name_plural = 'Записи KPIWORK'
#
#
# class File(models.Model):
#     title = models.CharField(max_length=90, verbose_name='Название файла')
#     file = models.FileField(upload_to='', verbose_name='Файл', null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Файл'
#         verbose_name_plural = 'Файлы'

class Files(models.Model):
    title = models.CharField(max_length=90, db_index=True, verbose_name='Название файла')
    file = models.FileField(upload_to='subjects/files', verbose_name='Файл')
    date_upload = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    subject = models.ForeignKey('UniversitySubject', null=True, on_delete=models.PROTECT, verbose_name='Предмет', related_name='files')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class UniversitySubject(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название предмета')
    slug = models.SlugField(max_length=90, unique=True, verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse('subject_post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('subject_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('subject_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

