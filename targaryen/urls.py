from django.conf.urls.defaults import *
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'targaryen.views.home', name='home'),
    # url(r'^targaryen/', include('targaryen.foo.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(PROJECT_ROOT, "../static")}),
    url(r'^write$', 'composer.views.home'),
    url(r'^$', 'composer.views.landing'),
    url(r'^publish$', 'composer.views.publish'),
    url(r'^posts$', 'composer.views.posts'),
    url(r'^posts/(?P<post_id>\d+)$', 'composer.views.post'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )
