from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freenasUI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','reporting.views.index',name="reportingindex"),
    url(r'^storage/$','storage.views.index',name="storageindex"),
    url(r'^storage/pool/$','storage.views.pool',name="storagepool"),
    url(r'^storage/pool/makepool/$','storage.views.makepool',name="storagemakepool"),
)
