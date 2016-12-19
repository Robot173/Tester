from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^answer/$', views.answer, name='answer'),
    url(r'^exit/$', views.exit, name='exit')
]