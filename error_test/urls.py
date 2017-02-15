from django.conf.urls import url

from . import views

app_name = 'error_test'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^quiz/$', views.quiz, name='quiz'),
    url(r'^result/$', views.result, name='result'),
    #url(r'^quiz/$', views.DetailView.as_view(), name='quiz'),
]
