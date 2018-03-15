from django.conf.urls import include, url
from . import views
urlpatterns = [
    url("^$", views.app_mgr, name="apps"),
    url("^app_mgr/$", views.app_mgr, name="app_mgr"),
    url("^app_mgr_data/$", views.app_mgr_data, name="app_mgr_data"),
    url("^deploy_info/$", views.deploy_info, name="app_deploy"),
    url("^getlog_deploy_log/$", views.getlog_deploy_log, name="getlog_deploy_log"),
    url("^deploy_run/$", views.deploy_run, name="deploy_run"),
    url("^process_ops/$", views.process_ops, name="process_ops"),
    url("^wlsprocess_ops/$", views.wlsprocess_ops, name="wlsprocess_ops"),
    url("^instance_ops/$", views.instance_ops, name="instance_ops"),
    url("^wlsinstance_ops/$", views.wlsinstance_ops, name="wlsinstance_ops"),
    url("^service_ops/$", views.service_ops, name="service_ops"),
    url("^file_del/$", views.file_del, name="file_del"),
    url("^demo/$", views.demo, name="demo"),
    url("^demo/demo_data/$", views.java_data, name="java_data"),
    url("^demo/demo_data_sub/$", views.java_data_sub, name="java_data_sub"),
    url("^deploy_info/demo_data_test/$", views.demo_data_test, name="demo_data_test"),
    url("^deploy_info/wls_data/$", views.wls_data, name="wls_data"),
    url("^deploy_info/wls_data_sub/$", views.wls_data_sub, name="wls_data_sub"),
    url("^deploy_info/java_data/$", views.java_data, name="java_data"),
    url("^deploy_info/java_data_sub/$", views.java_data_sub, name="java_data_sub"),
    url("^services/services_data/$", views.services_data, name="services_data"),
    url("^services/$", views.services, name="services"),

]
