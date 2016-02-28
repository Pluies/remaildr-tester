from __future__ import absolute_import

from celery import shared_task
from remaildrtester.probe.sender import Sender
from remaildrtester.probe.receiver import Receiver
from remaildrtester.probe.cleaner import Cleaner


@shared_task
def send_probe():
    Sender.send()


@shared_task
def receive_probe():
    Receiver.receive()


@shared_task
def cleanup():
    Cleaner.clean()
