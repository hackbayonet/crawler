from django.conf.urls import include, url
from django.contrib import admin
from lagou import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^detail/(.*?)$', views.detail),
    url(r'^key', views.index),
    url(r'^demand_all/(.*?)$', views.demand_all),
    url(r'^index', views.index),
    url(r'.*', views.home)
]
