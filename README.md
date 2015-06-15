What is this
============

A test suite/healthcheck for [Remaildr](http://remaildr.com)

What does it do
===============

It sends emails to test@remaildr.com containing a timestamp of the time it was
sent at, then when polled, consults the answers from remaildr and infers the
state of the app from the last seen timstamp:
- Less than 10mn old: probably ok
- Less than 30mn old: probably ok, but may have network/load issues?
- Over 30mn old: something is probably wrong

What is it used for
===================

Two main goals:
- Provide a health indicator on [Remaildr's website](http://remaildr.com)
- Send alerts when Remaildr is down so that I can fix it
