from django.conf.urls import url

from . import views

app_name = 'movieapp'
urlpatterns = [
    # ex: /movieapp/
    url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /movieapp/signup/
	url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    # ex: /movieapp/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /movieapp/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /movieapp/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]