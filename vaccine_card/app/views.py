from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vaccine_card.scheduling.forms import EventForm
from vaccine_card.scheduling.models import Event


@login_required
def patient_index(request):
    template_name = 'patient_app/index.html'

    return render(request, template_name)


@login_required
def patient_vaccine_card(request):
    template_name = 'patient_app/vaccine_card.html'

    return render(request, template_name)


@login_required
def add_schedule(request):
    template_name = 'patient_app/schedule.html'

    form = EventForm(auto_id=False)

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Agendado com sucesso.')

    context = {
        'form': form
    }

    return render(request, template_name, context)


@login_required
def patient_schedule(request):
    template_name = 'patient_app/schedules.html'

    instances = Event.objects.all()

    context = {
        'instances': instances
    }

    return render(request, template_name, context)
