from django.shortcuts import render


def graphic(request):
    return render(request, 'users/graphic.html')
