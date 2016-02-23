from django.forms.models import model_to_dict
from website.models import RemotePoll


def last_ok():
    return (RemotePoll
            .objects
            .filter(status=RemotePoll.SUCCESS)
            .order_by('-started_at')
            .first())


def all_polls_as_dicts():
    all_polls = RemotePoll.objects.order_by('-started_at')
    dicts = [model_to_dict(x) for x in all_polls]
    return dicts
