import arrow
import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from email.utils import formatdate
from website.models import RemotePoll

import logging
logger = logging.getLogger(__name__)


class SMTPConnection:
    def __init__(self):
        # Send the message via our preferred SMTP server.
        self.conn = smtplib.SMTP("smtp.gmail.com", 587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(settings.EMAIL_ACCOUNT, settings.EMAIL_PASSWORD)

    def __enter__(self):
        return self.conn

    def __exit__(self, t, value, traceback):
        self.conn.quit()


class Sender:
    def generate_probe():
        now = arrow.utcnow()
        started_at = now.datetime
        probe_id = now.timestamp
        probe = RemotePoll(started_at=started_at,
                           status=RemotePoll.PENDING,
                           probe_id=probe_id)
        probe.save()
        return probe

    def email_from_probe(probe):
        timestamp = probe.probe_id
        msg = MIMEText('This is a probe for remaildr.' +
                       'Hi remaildr! Timestamp: %s' % timestamp)
        msg['From'] = 'florent.potato@gmail.com'
        msg['To'] = 'test@remaildr.com'
        msg['Subject'] = 'Probe: %s' % timestamp
        msg['Date'] = formatdate()
        return msg

    def send():
        probe = Sender.generate_probe()
        msg = Sender.email_from_probe(probe)
        logger.info('Sending email:')
        logger.info(msg)
        with SMTPConnection() as S:
            S.send_message(msg)
            logger.info('Email sent successfully ' +
                        'with probe_id %s' % probe.probe_id)
