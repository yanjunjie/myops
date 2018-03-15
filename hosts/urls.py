
from django.conf.urls import include, url
import views

urlpatterns = [
    url("^$", views.host_mgr, name="hosts"),
    url("^hosts_index/$", views.hosts_index, name="hosts_index"),
    url("^host_mgr/$", views.host_mgr, name="host_mgr"),
    url("^hosts_list/$", views.hosts_list, name="hosts_list"),
    url("^file_upload/$", views.file_upload, name="file_upload"),
    url(r'^upload_script/$', views.uploadify_script),
    url(r'^handle_uploaded_file/$', views.handle_uploaded_file),
    url(r'^upload_list/$', views.upload_list),
    url(r'^file_del/$', views.file_del),
    url(r'^file_send/$', views.file_send),
    url(r'^file_push/$', views.file_push),
    url(r'^file_manage', views.file_manage,name='file_manage'),
    url("^multi_cmd/$", views.multi_cmd, name="multi_cmd"),
    url("^submit_task/$", views.submit_task, name="submit_task"),
    url("^command/$", views.command, name="command"),

]
