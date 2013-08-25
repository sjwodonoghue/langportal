from django.conf.urls import patterns, url

from french import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^wordtest/', views.wordtest, name='wordtest'),
    url(r'^checkanswers/', views.checkanswers, name='checkanswers'),
    url(r'^auth/',  views.auth_view, name='auth'),    
    url(r'^logout/', views.logout, name='logout'),
    url(r'^loggedin/', views.loggedin, name='loggedin'),
    url(r'^invalid/', views.invalid_login, name='invalid_login'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)