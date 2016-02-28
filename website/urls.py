from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^status$', views.status),
        url(r'^raw_all_statuses$', views.remote_polls),
]
