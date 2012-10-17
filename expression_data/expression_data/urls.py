'''This package is the master urlconf for this project.

All URL requests are first routed through here, then if necessary delegated to other modules.'''

from django.conf.urls import patterns, include, url

from researchers.views import ResearcherDetail
from genes.views import GeneDetail
from expression_data.views import SearchView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expression_data.views.home', name='home'),
    url(r'^search/?$', SearchView.as_view(), name='search'),
    url(r'^researcher/(?P<pk>[\d]+)/?$', ResearcherDetail.as_view(), name='researcher-details'),
    url(r'^genes?/(?P<slug>[\d\w-]+)/?$', GeneDetail.as_view(), name='gene-details'),    
    # url(r'^expression_data/', include('expression_data.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
