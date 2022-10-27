from django.shortcuts import render
from .models import Record


# Create your views here.
def index(request):
    records_list = Record.objects.all()
    return render(request, 'records/index.html', {'records': records_list})
