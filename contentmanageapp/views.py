from django.shortcuts import render


def top(request):
    return render(request, 'contentmanageapp/top.html')


def external(request):
    return render(request, 'contentmanageapp/external.html')


def internal(request):
    return render(request, 'contentmanageapp/internal.html')
