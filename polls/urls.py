from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^addQuestion/$', views.addQuestion, name='addQuestion'),
    url(r'^addQuestion/success/$', views.addQuestionSuccess, name='addquestionsuccess'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
