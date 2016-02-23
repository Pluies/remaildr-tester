from __future__ import absolute_import

from celery import shared_task
from remaildrtester.probe_sender import Sender
from remaildrtester.probe_receiver import Receiver


@shared_task
def send_probe():
    Sender.send()


@shared_task
def receive_probe():
    Receiver.receive()
