"""s10ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from hosts import urls as hosts_urls
from applications import urls as apps_urls
from monitor import urls as monitor_urls
from hosts import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name='dashboard'),
    url(r'^hosts/', include(hosts_urls)),
    url(r'^apps/', include(apps_urls)),
    url(r'^monitor/', include(monitor_urls)),

    url("^assets/$", views.assets_index, name="assets"),
    #url("^monitor/$", views.monitor_index, name="monitor"),
    url("^login/$", views.acc_login, name="login"),
    url("^logout/$", views.acc_logout, name="logout")

]
