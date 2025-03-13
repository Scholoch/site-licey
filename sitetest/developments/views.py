from django.shortcuts import get_object_or_404, render
from .models import LabTheme


def theme(request, id):
    theme = get_object_or_404(LabTheme, id=id)
    return render(request, 'theme.html', dict([('theme', theme)]))