from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class ObjectDetailMixin:
    model = None
    template_name = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {
            self.model.__name__.lower(): obj,
            'admin_object': obj,
            'detail': True,
        }
        return render(request, self.template_name, context=context)
