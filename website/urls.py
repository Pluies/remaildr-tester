from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^api/status$', views.status),
        url(r'^api/updown$', views.updown),
        url(r'^raw_all_statuses$', views.remote_polls),
]
