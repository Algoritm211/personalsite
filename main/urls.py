from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static, serve

from .views import *

# settings.MEDIA_URL = 'media/'
urlpatterns = [
    path('', index, name='main_page'),
    path('myblog/', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('subjects/', subjects_list, name='subjects_list'),
    path('subjects/upload/', UploadSubjectFiles.as_view(), name='upload_subject_files'),
    path('subjects/create/', UniversitySubjectCreate.as_view(), name='create_subject'),
    path('subjects/<str:slug>/', UniversitySubjectDetail.as_view(), name='subject_post_detail_url'),
    path('subjects/<str:slug>/update', UniversitySubjectUpdate.as_view(), name='subject_update'),
    path('subjects/<str:slug>/delete', UniversitySubjectDelete.as_view(), name='subject_delete'),
    path('myworks/', myworks_list, name='my_works_list'),
    # path('<path:filepath>/', download_file, name='download_subject_file')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

