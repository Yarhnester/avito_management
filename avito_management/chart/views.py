from django.shortcuts import render, get_object_or_404, redirect
from .models import Chart, User
from .forms import DateChartForm


def chart(request):
    user = get_object_or_404(User, username=request.user)
    charts = Chart.objects.all()
    form = DateChartForm(request.POST or None)
    context = {
        'charts': user.charts.all(),
        'form': form,
    }
    if not request.method == 'POST':
        return render(request, 'chart/chart.html', context)
    if not form.is_valid():
        return render(request, 'chart/chart.html', context)
    new_date = form.save(commit=False)
    new_date.name = request.user
    new_date.save()
    return render(request, 'chart/chart.html', context)
