from django.shortcuts import render, redirect
from .forms import RecordForm
from .models import Record


# Create your views here.
def index(request):
    records_list = Record.objects.all()
    return render(request, 'records/index.html', {'records': records_list})


def contract_add(request):
    form = RecordForm(request.POST or None)
    if not request.method == 'POST':
        return render(request, 'records/contract_add.html', {'form': form})
    if not form.is_valid():
        return render(request, 'records/contract_add.html', {'form': form})
    record = form.save(commit=False)
    record.save()
    return redirect('')



