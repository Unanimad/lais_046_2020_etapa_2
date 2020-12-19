from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from vaccine_card.core.utils import dump_json

from .forms import HealthCenterForm, AddressForm
from .models import HealthCenter


@login_required
def health_centers(request):
    template_name = 'panel/list.html'

    context = {
        'head_title': HealthCenter._meta.verbose_name_plural,
        'instances': HealthCenter.objects.all(),
        'breadcrump': [{'name': HealthCenter._meta.verbose_name_plural, 'link': 'panel:vaccination:vaccines'}],
        'add_url': 'panel:logistic:add_health_center',
        'view_url': 'panel:logistic:health_center',
        'edit_url': 'panel:vaccination:edit_vaccine',
        'del_object_url': 'panel:logistic:del_health_center',
    }

    return render(request, template_name, context)


@login_required
def add_health_center(request):
    template_name = 'panel/add.html'

    form = HealthCenterForm(auto_id=False)
    form_aux = AddressForm(auto_id=False)

    if request.method == 'POST':
        form = HealthCenterForm(request.POST)
        form_aux = AddressForm(request.POST)

        if form.is_valid() and form_aux.is_valid():
            name = form.cleaned_data['name']

            if HealthCenter.objects.filter(name=name).exists():
                messages.error(request, 'Já existe um objeto com este nome.')

            else:
                address = form_aux.save()
                heath_center = form.save()

                heath_center.address.add(address)
                messages.success(request, 'Cadastrado com sucesso.')

    context = {
        'form': form,
        'form_aux': form_aux,
        'form_aux_title': 'Endereço',
        'head_title': 'Novo Estabelecimento de Saúde',
        'title': HealthCenter._meta.verbose_name
    }

    return render(request, template_name, context)


@login_required
def health_center(request, pk):
    template_name = 'panel/add.html'

    instance = HealthCenter.objects.get(pk=pk)

    context = {
        'title': instance.name,
        'head_title': instance.name,
    }

    return render(request, template_name, context)


@login_required
def del_health_center(request):
    if request.method == 'POST':
        pk = request.POST['pk']

        try:
            HealthCenter.objects.filter(pk=pk).delete()

        except:
            return dump_json({'err': True, 'text': 'Não foi possível deletar o objeto.'})

        else:

            context = {
                'err': False,
                'text': 'Objeto deletado com sucesso.'
            }

        return dump_json(context)
