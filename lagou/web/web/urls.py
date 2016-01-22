from django.conf.urls import include, url
from django.contrib import admin
from lagou import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^home/$', views.home),
    url(r'^detail/(.*?)$', views.detail),
    url(r'^demand_all/(.*?)$', views.demand_all),
    url(r'.*', views.home)
]
