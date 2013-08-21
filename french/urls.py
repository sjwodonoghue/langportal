from django.conf.urls import patterns, url

from french import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^wordtest/', views.wordtest, name='wordtest'),
    url(r'^checkanswers/', views.checkanswers, name='checkanswers'),

    
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)