from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('project.views',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/$', 'my_view'),
    url(r'^project/detail/$', 'detail'),
    url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/image/favicon.ico'})
)
#
urlpatterns += patterns('ctr.views',
                        url(r'^ctr/$', 'my_view'),
                        url(r'^ctr/detail/$', 'detail')
                        )
