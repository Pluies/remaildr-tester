from django.db import models


class RemotePoll(models.Model):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    TIMEOUT = "TIMEOUT"
    probe_id = models.CharField(max_length=256, null=True)
    started_at = models.DateTimeField('date started at')
    completed_at = models.DateTimeField('date completed at', null=True)
    status = models.CharField(max_length=256)

    def __str__(self):
        s = 'RemotePoll started at %s, ' % self.started_at
        s += 'completed at %s, ' % self.completed_at
        s += 'status %s' % self.status
        return s
