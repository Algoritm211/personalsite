from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_to_main(request):
    return redirect('main_page', permanent=True)
