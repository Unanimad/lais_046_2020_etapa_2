from django.contrib import messages
from django.shortcuts import render

from .forms import VaccineForm
from .models import Vaccine


def vaccines(request):
    template_name = 'panel/list.html'

    context = {
        'head_title': Vaccine._meta.verbose_name_plural,
        'instances': Vaccine.objects.all(),
        'add_url': 'panel:vaccination:add_vaccine',
        'view_url': 'panel:vaccination:add_vaccine',
        'edit_url': 'panel:vaccination:add_vaccine',
        'del_object_url': 'panel:vaccination:add_vaccine',
    }

    return render(request, template_name, context)


def add_vaccine(request):
    template_name = 'panel/add.html'

    form = VaccineForm(auto_id=False)

    if request.method == 'POST':
        form = VaccineForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            if Vaccine.objects.filter(name=name).exists():
                messages.error(request, 'Já existe um objeto com este nome.')

            else:
                form.save()
                messages.success(request, 'Cadastrado com sucesso.')

    context = {
        'form': form,
        'head_title': 'Nova vacina',
        'title': 'Vacina'
    }
    return render(request, template_name, context)


def vaccine(request):
    template_name = 'panel.add.html'
    return render(request, template_name)
