from django.conf.urls import include, url
from . import views
urlpatterns = [
    url("^$", views.monitor_mgr, name="monitor"),
    url("^monitor_mgr/$", views.monitor_mgr, name="monitor_mgr"),
    url("^dashboard/$", views.dashboard, name="dashboard"),
    url("^app_mon/$", views.app_mon, name="app_mon"),
    url("^process_mon/$", views.process_mon, name="process_mon"),
    url("^module_mon/$", views.module_mon, name="module_mon"),
    url("^host_mon/$", views.host_mon, name="host_mon"),
    url("^host_mon/data/$", views.hosts_list, name="hosts_list"),
    #url("^host_mon/(?P<hostname>.+)/(?P<timing>\d+)/$", views.host_info, name="host_info"),
    url(r'host_mon/(\d+)/$',views.host_detail ,name='host_detail'),
    url(r'load_server_data/(\d+)/$', views.load_server_data, name='load_server_data'),
    url("^process_mon/port_status/$", views.port_status, name="port_status"),

]
