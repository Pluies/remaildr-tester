from django.http import JsonResponse
from django.views.generic import TemplateView
from website.polls import status_summary, all_polls_as_dicts


class IndexView(TemplateView):
    template_name = 'index.html'


def status(request):
    return JsonResponse({"status": status_summary()})


def remote_polls(request):
    return JsonResponse({"polls": all_polls_as_dicts()})
