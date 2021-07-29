from django.shortcuts import render


def index_html_views(request):
    return render(request, 'index.html')

def about_html_views(request):
    return render(request, 'about.html')