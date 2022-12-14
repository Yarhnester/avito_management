from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecordForm
from .models import Record


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
    return redirect('records:index')


def contract_edit(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('records:index')

    context = {
        'records': record,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'records/contract_add.html', context)
