from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from vaccine_card.core.utils import dump_json

from .forms import VaccineForm, ReinforcementForm
from .models import Vaccine


@login_required
def vaccines(request):
    template_name = 'default/list.html'

    context = {
        'head_title': Vaccine._meta.verbose_name_plural,
        'instances': Vaccine.objects.all(),
        'breadcrump': [{'name': 'Vacinas', 'link': 'panel:vaccination:vaccines'}],
        'add_url': 'panel:vaccination:add_vaccine',
        'view_url': 'panel:vaccination:vaccine',
        'edit_url': 'panel:vaccination:edit_vaccine',
        'del_object_url': 'panel:vaccination:del_vaccine',
    }

    return render(request, template_name, context)


@login_required
def add_vaccine(request):
    template_name = 'default/add.html'

    form = VaccineForm(auto_id=False)
    form_aux = ReinforcementForm(auto_id=False)

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
        'form_aux': form_aux,
        'form_aux_title': 'Reforços',
        'head_title': 'Nova vacina',
        'title': 'Vacina'
    }
    return render(request, template_name, context)


@login_required
def edit_vaccine(request, pk):
    template_name = 'default/add.html'

    instance = Vaccine.objects.get(pk=pk)

    form = VaccineForm(auto_id=False, instance=instance)

    if request.method == 'POST':
        form = VaccineForm(request.POST or None, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(
                request, f'Classe {instance.name.lower()} atualizado com sucesso!')

        else:
            messages.error(request, 'Não foi possível atualizar.')

    context = {
        'head_title': instance.name,
        'title': instance.name,
        'form': form
    }

    return render(request, template_name, context)


@login_required
def vaccine(request, pk):
    template_name = 'default/list.html'

    instance = Vaccine.objects.get(pk=pk)

    context = {
        'title': instance.name,
        'head_title': instance.name,
    }

    return render(request, template_name, context)


@login_required
def del_vaccine(request):
    if request.method == 'POST':
        pk = request.POST['pk']

        try:
            Vaccine.objects.filter(pk=pk).delete()

        except:
            return dump_json({'err': True, 'text': 'Não foi possível deletar o objeto.'})

        else:

            context = {
                'err': False,
                'text': 'Objeto deletada com sucesso.'
            }

        return dump_json(context)
