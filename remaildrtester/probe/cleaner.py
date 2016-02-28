import arrow
from website.models import RemotePoll

import logging
logger = logging.getLogger(__name__)


class Cleaner:
    def clean():
        # Set all probes that are older than cutoff to "Timeout"
        now = arrow.utcnow()
        cutoff = now.replace(hours=-1)
        updated = (RemotePoll.objects
                   .filter(status=RemotePoll.PENDING)
                   .filter(started_at__lt=cutoff.datetime)
                   .update(status=RemotePoll.TIMEOUT,
                           completed_at=now.datetime))
        if updated:
            logger.info("Found and set timeout on %s probes" % updated)
