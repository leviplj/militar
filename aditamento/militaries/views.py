from django.shortcuts import render
from aditamento.militaries.models import Military


def military_list(request):
    militaries = Military.objects.all()
    return render(request, 'militaries/military_list.html', {'militaries': militaries})