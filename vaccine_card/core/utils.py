from json import dumps

from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


def dump_json(json_list):

    json_data = dumps(json_list, cls=DjangoJSONEncoder)

    return HttpResponse(json_data, content_type='application/json')
