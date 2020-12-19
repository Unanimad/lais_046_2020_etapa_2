from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from vaccine_card.core.utils import dump_json
from .forms import HealthCenterForm, AddressForm, StockForm
from .models import HealthCenter, VaccineStock, Stock


@login_required
def health_centers(request):
    template_name = 'logistic/list_health_center.html'

    context = {
        'head_title': HealthCenter._meta.verbose_name_plural,
        'instances': HealthCenter.objects.all(),
        'breadcrump': [{'name': HealthCenter._meta.verbose_name_plural, 'link': 'panel:vaccination:vaccines'}],
        'stock_url': 'panel:logistic:health_center_stock',
        'add_url': 'panel:logistic:add_health_center',
        'view_url': 'panel:logistic:health_center',
        'edit_url': 'panel:vaccination:edit_vaccine',
        'del_object_url': 'panel:logistic:del_health_center',
    }

    return render(request, template_name, context)


@login_required
def add_health_center(request):
    template_name = 'default/add.html'

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
    template_name = 'default/add.html'

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


@login_required
def health_center_stock(request, pk):
    template_name = 'logistic/health_center_stock.html'

    instance = HealthCenter.objects.get(pk=pk)

    instances = VaccineStock.objects.filter(stock__health_center=instance)

    form = StockForm(auto_id=False)

    context = {
        'instance': instance,
        'head_title': 'Estoque',
        'instances': instances,
        'form': form
    }

    return render(request, template_name, context)


@login_required
def receive_vaccine(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        # form.fields = HealthCenter.objects.filter(pk=int())

        if form.is_valid():
            health_center = HealthCenter.objects.get(pk=form.cleaned_data['health_center'])
            # vaccine = Vaccine.objects.get(pk=form.cl)
            stock, created = Stock.objects.update_or_create(lot=form.cleaned_data['lot'], health_center=health_center)
            for vaccine in form.cleaned_data['vaccines']:
                VaccineStock.objects.create(amount=form.cleaned_data['amount'], remaining=form.cleaned_data['amount'],
                                            stock=stock, vaccine=vaccine)

            # VaccineStock.objects.get_or_create()

            context = {
                'err': False,
                'text': 'Inserido com sucesso.'
            }
        else:
            context = {
                'err': True,
                'text': 'Falha ao inserir o lote.'
            }

        return dump_json(context)
