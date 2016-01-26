from django.conf.urls import include, url
from django.contrib import admin
from lagou import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^job/(.*?)$', views.job),
    url(r'.*', views.home)
]
