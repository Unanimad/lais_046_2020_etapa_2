from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import HealthCenter
from .forms import HealthCenterForm, AddressForm


@login_required
def health_centers(request):
    template_name = 'panel/list.html'

    context = {
        'head_title': HealthCenter._meta.verbose_name_plural,
        'instances': HealthCenter.objects.all(),
        'breadcrump': [{'name': HealthCenter._meta.verbose_name_plural, 'link': 'panel:vaccination:vaccines'}],
        'add_url': 'panel:logistic:add_health_center',
        'view_url': 'panel:vaccination:vaccine',
        'edit_url': 'panel:vaccination:edit_vaccine',
        'del_object_url': 'panel:vaccination:del_vaccine',
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
            razao_social = form.cleaned_data['razao_social']

            if HealthCenter.objects.filter(razao_social=razao_social).exists():
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
