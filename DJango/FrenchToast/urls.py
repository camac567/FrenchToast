from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FrenchToast.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	('^appFrenchToast/add_dummy_data', 'FrenchToast.appFrenchToast.add_dummy_data')
)
