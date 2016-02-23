from django.http import HttpResponse, JsonResponse
from website.polls import all_polls_as_dicts


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def remote_polls(request):
    return JsonResponse({"polls": all_polls_as_dicts()})
