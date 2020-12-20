from django.shortcuts import render

from .models import Event


def schedules(request):
    template_name = 'schedule/list.html'

    instances = Event.objects.all()

    context = {
        'head': 'Agendamentos',
        'head_title': 'Agendamentos',
        'instances': instances
    }
    return render(request, template_name, context)
