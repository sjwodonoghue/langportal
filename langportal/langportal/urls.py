from django.conf.urls import patterns, include, url
from french import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'langportal.views.home', name='home'),
    # url(r'^langportal/', include('langportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', french.index, name='index'),
    #url(r'^french/', 'french.views.index', name='index'),
    url(r'^wordtest/', 'french.views.wordtest', name='wordtest'),
    url(r'^checkanswers/', 'french.views.checkanswers', name='checkanswers'),


)
