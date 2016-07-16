import arrow
import email
import imaplib
import sys
import traceback
from django.conf import settings
from website.models import RemotePoll

import logging
logger = logging.getLogger(__name__)


class IMAPConnection:
    def __init__(self):
        self.conn = imaplib.IMAP4_SSL("imap.gmail.com")
        self.conn.login(settings.EMAIL_ACCOUNT,
                        settings.EMAIL_PASSWORD)
        self.conn.select("INBOX")

    def __enter__(self):
        return self.conn

    def __exit__(self, t, value, traceback):
        self.conn.close()
        self.conn.logout()


class Receiver:
    def receive():
        with IMAPConnection() as M:
            M.select('inbox')
            typ, data = M.search(None, 'ALL')
            for num in data[0].split():
                try:
                    typ, msg_data = M.fetch(num, '(RFC822)')
                    if not msg_data or not msg_data[0] or not msg_data[0][1]:
                        return
                    raw_msg = msg_data[0][1]
                    msg = email.message_from_string(raw_msg.decode('utf-8'))
                    subject = msg['subject']
                    if subject.startswith('Remaildr: Probe: '):
                        probe_id = subject.replace('Remaildr: Probe: ', '')
                        logger.info("Found probe #%s" % probe_id)
                        try:
                            probe = RemotePoll.objects.get(probe_id=probe_id)
                            probe.status = RemotePoll.SUCCESS
                            probe.completed_at = arrow.utcnow().datetime
                            probe.save()
                        except:
                            logger.error("Probe %s not found in db - skipping" %
                                         probe_id)
                except:
                    e = sys.exc_info()[0]
                    logger.error("Uncaught exception: %s" % e)
                    traceback.print_exc(file=sys.stdout)
                finally:
                    M.store(num, '+FLAGS', '\\Deleted')
                    M.expunge()
