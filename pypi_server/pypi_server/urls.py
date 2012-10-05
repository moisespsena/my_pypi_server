from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypi_server.views.home', name='home'),
    # url(r'^pypi_server/', include('pypi_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pypi/.+/dists/(?P<file_name>.+)$', 'distsapp.views.dist_download'),
    url(r'', include("djangopypi.urls")),
)
