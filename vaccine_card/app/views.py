from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def patient_index(request):
    template_name = 'patient_app/index.html'

    return render(request, template_name)


@login_required
def patient_vaccine_card(request):
    template_name = 'patient_app/vaccine_card.html'

    return render(request, template_name)
