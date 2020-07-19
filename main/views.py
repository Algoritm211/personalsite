from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import MainInfo, Tag, Post, UniversitySubject, Files
from django.views.generic import View
from .forms import TagForm, PostForm, FilesForm, SubjectForm
from django.views.generic.edit import FormView
import mimetypes
from django.http import FileResponse
from .utils import ObjectDetailMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin #Миксин для ограничения доступа
from django.db.models import Q
# Create your views here.

def posts_list(request):
    #Search
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'main/posts_list.html', context=context, )


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template_name = 'main/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template_name = 'main/tag_detail.html'

def index(request):
    info = MainInfo.objects.get(pk=1)
    context = {
        'Maininfo': info,
    }
    return render(request, 'main/main_page.html', context=context, )


def kpiworks_list(request):
    return render(request, 'main/kpiworks_list.html')


def myworks_list(request):
    return render(request, 'main/myworks_list.html')


class TagCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = TagForm()
        context = {
            'form': form,
        }
        return render(request, 'main/tag_create.html', context=context)

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(str(new_tag.get_absolute_url()))
        context = {
            'form': bound_form,
        }
        return render(request, 'main/tag_create.html', context=context)


class PostCreate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'main/post_create.html', context=context)

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(str(new_post.get_absolute_url()))
        context = {
            'form': bound_form,
        }
        return render(request, 'main/post_create.html', context=context)


class TagUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        context = {
            'form': bound_form,
            'tag': tag,
        }
        return render(request, 'main/tag_update_form.html', context=context)

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            updated_tag = bound_form.save()
            return redirect(str(updated_tag.get_absolute_url()))
        context = {
            'form': bound_form,
            'tag': tag,
        }
        return render(request, 'main/tag_update_form.html', context=context)


class PostUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        context = {
            'post': post,
            'form': bound_form,
        }
        return render(request, 'main/post_update_form.html', context=context)

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            updated_post = bound_form.save()
            return redirect(str(updated_post.get_absolute_url()))
        context = {
            'form': bound_form,
            'post': post
        }
        return render(request, 'main/post_update_form.html', context=context)


class TagDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        context = {
            'tag': tag,
        }
        return render(request, 'main/tag_delete_form.html', context=context)

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('posts_list_url'))


class PostDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        context = {
            'post': post,
        }
        return render(request, 'main/post_delete_form.html', context=context)

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))


def subjects_list(request):
    subjects = UniversitySubject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'main/subjects_list.html', context=context)


# def upload_subject_files(request):
#     if request.method == 'POST':
#         form = FilesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('subjects_list')
#     else:
#         form = FilesForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'main/upload_subjects.html', context=context)

class UploadSubjectFiles(LoginRequiredMixin, FormView):
    raise_exception = True

    form_class = FilesForm
    template_name = 'main/upload_subjects.html'
    success_url = '#'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            id = form.save().subject
            print(id)
            subject = UniversitySubject.objects.get(title=id)
            if files:
                for f in files:
                    fl = Files(subject=subject, file=f)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UniversitySubjectDetail(ObjectDetailMixin, View):
    model = UniversitySubject
    template_name = 'main/subject_post_detail.html'

def download_file(request, filepath):
    fl_path = filepath
    # fl_path_repl = fl_path.replace('//', '/')
    response = FileResponse(open(fl_path, 'rb'))
    # mime_type, _ = mimetypes.guess_type(fl_path)
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % 'file_1'
    return response


class UniversitySubjectCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = SubjectForm()
        context = {
            'form': form,
        }
        return render(request, 'main/subject_create.html', context=context)

    def post(self, request):
        bound_form = SubjectForm(request.POST)

        if bound_form.is_valid():
            new_subject = bound_form.save()
            return redirect(str(new_subject.get_absolute_url()))
        context = {
            'form': bound_form,
        }
        return render(request, 'main/subject_create.html', context=context)


class UniversitySubjectDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        subject = UniversitySubject.objects.get(slug__iexact=slug)
        context = {
            'subject': subject,
        }
        return render(request, 'main/subject_delete_form.html', context=context)

    def post(self, request, slug):
        subject = UniversitySubject.objects.get(slug__iexact=slug)
        subject.delete()
        return redirect(reverse('subjects_list'))


class UniversitySubjectUpdate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        subject = UniversitySubject.objects.get(slug__iexact=slug)
        bound_form = SubjectForm(instance=subject)
        context = {
            'subject': subject,
            'form': bound_form,
        }
        return render(request, 'main/subject_update_form.html', context=context)

    def post(self, request, slug):
        subject = UniversitySubject.objects.get(slug__iexact=slug)
        bound_form = SubjectForm(request.POST, instance=subject)

        if bound_form.is_valid():
            updated_subject = bound_form.save()
            return redirect(str(updated_subject.get_absolute_url()))
        context = {
            'form': bound_form,
            'subject': subject,
        }
        return render(request, 'main/subject_update_form.html', context=context)
