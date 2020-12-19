from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vaccine_card.scheduling.forms import EventForm


@login_required
def patient_index(request):
    template_name = 'patient_app/index.html'

    return render(request, template_name)


@login_required
def patient_vaccine_card(request):
    template_name = 'patient_app/vaccine_card.html'

    return render(request, template_name)


@login_required
def schedule(request):
    template_name = 'patient_app/schedule.html'

    form = EventForm(auto_id=False)

    context = {
        'form': form
    }

    return render(request, template_name, context)
