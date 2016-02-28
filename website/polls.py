from django.forms.models import model_to_dict
from website.models import RemotePoll
import arrow


def uptime(array):
    (ok, fail) = (0, 0)
    for poll in array:
        if poll.status == RemotePoll.SUCCESS:
            ok += 1
        elif poll.status == RemotePoll.PENDING:
            # Ignore
            ok += 0
        elif poll.status == RemotePoll.FAILURE:
            fail += 1
        elif poll.status == RemotePoll.TIMEOUT:
            fail += 1
    if ok == 0 and fail == 0:
        return None
    return {
            "uptime": 100 * (ok / (ok + fail)),
            "datapoints": (ok + fail),
            }

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

def status_summary():
    a_day_ago = arrow.utcnow().replace(days=-1)
    a_month_ago = arrow.utcnow().replace(months=-1)
    a_year_ago = arrow.utcnow().replace(years=-1)
    o = RemotePoll.objects
    day = o.filter(started_at__gt=a_day_ago.datetime)
    month = o.filter(started_at__gt=a_month_ago.datetime)
    year = o.filter(started_at__gt=a_year_ago.datetime)
    return {
            "day": uptime(day),
            "month": uptime(month),
            "year": uptime(year),
            }
