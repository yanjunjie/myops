#-*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response,HttpResponse, redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from hosts import models
from hosts.views import *
import os,json,time
from os.path import splitext
from time import sleep
from hosts.utils import *
from datetime import datetime
from django.http import JsonResponse

import urllib2
import sys
import json
import argparse
from zabbix.login import *
from zabbix.function1 import *
today = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def demo(request):
  return render_to_response('monitor/monitor_mgr.html')

def demo_data_test(request):
  return HttpResponse(json.dumps(data,ensure_ascii=False))

@login_required
def host_data(request):
    data = []
    return HttpResponse(json.dumps(data,ensure_ascii=False))

@login_required
def hosts_list(request):
    hosts = []
    selected_gid = request.GET.get('selected_gid')
    if selected_gid:
       if selected_gid == 'all':
          host_list = models.Host.objects.all().values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')
       else:
          #host_list = models.Host.objects.all().values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')     
          h_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)
          host_list = []
          for h in h_list:
              h_id = h.host_id
              host = models.Host.objects.all().filter(id = h_id).values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')
              host_list.extend(host)
    else:
        host_list = models.Host.objects.all().values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')
    for host in host_list:
        h_id = host['id']
        idc_id = host['idc_id']
        dt = host['date']                                                                                                                                                      
        dat = dt.strftime("%Y-%m-%d %X")
        hostToUser = models.BindHostToUser.objects.select_related('host_user').filter(host_id=h_id)
        users = []
        for h in hostToUser:
            u = h.host_user.username
            users.append(u)
        #print "==================================",host_user,name
        idc = models.IDC.objects.all().filter(id = idc_id).distinct().values('id','name')
        hosts.append({'id':host['id'],'hostname':host['hostname'],'ipaddr':host['ip_addr'],'port': host['port'],'systemtype':host['system_type'],'dat':dat,'idc':idc[0]['name'],'status':host['enabled'],'hostuser':users})
    return HttpResponse(json.dumps(hosts,ensure_ascii=False))


@login_required
def monitor_mgr(request):
    return render(request,"monitor/monitor_mgr.html") 

@login_required
def dashboard(request):
    return render(request,"monitor/index.html")



#从zabbix中获取进程的状态

@login_required                                                                                                                                                                                            
def port_status(request):                                                                                                                                                                                

    data = []
    process = models.java_process.objects.all().values('id','name','port','host_id').order_by('id');
    for item in process:                                                                                                                                                                                   
        port = item['port']
        host_id = item['host_id']
        
        itemsname='java.mon.port['+ str(port) + ']'
        auth = authenticate(url, username, password)
        
        host = models.Host.objects.filter(id = host_id).values('ip_addr')                                                                                                                             
        hostip = host[0]['ip_addr']
        
        hostids=ipgetHostsid(hostip,url,auth)       
        hostid=hostids[0]['hostid']
        itemid = getHostsitemsid(hostid,itemsname,url,auth)
        value = getHostsitemsvalue(itemid,url,auth)
        data.append(value)
        if value == '1':
           models.java_process.objects.filter(port=port).update(status='0',date=today)
        elif value =='0':
           models.java_process.objects.filter(port=port).update(status='1',date=today)
        else:
           print value
        
        #data.append({'id':item.id,'name':item.name,'pid':item.pid,'path':item.path,'port':item.port,'cpu':item.cpu,'last_date':item.date,'status':item.status,'host':host[0]['ip_addr']})
        print "=========",value                                                                                                                           
    return HttpResponse(json.dumps(data,ensure_ascii=False))                                                                                                                           
                                                                                                                                                                                                           
  

@login_required
def app_mon(request):

    return render(request,"monitor/app_mon.html")


@login_required
def process_mon(request):

    return render(request,"monitor/process_mon.html")


@login_required
def module_mon(request):
    return render(request,"monitor/module_mon.html")

@login_required
def host_mon(request):
    group_list = models.HostGroup.objects.all().values('id','name')
    host_list = models.Host.objects.all()
    print("hosts:=========================",host_list)
    print("group_list:=========================",group_list)
    return render(request,"monitor/host_info.html", {'group_list':group_list,'host_list':host_list})

@login_required
def host_detail(request,host_id):
    #server = models.Host.objects.get(id=host_id)
    #server = models.Host.objects.filter(id = host_id).all()
    #platform = models.platform.objects.filter(server_id = host_id).all()
    server = models.Platform.objects.filter(server_id = host_id).all()
    update_period = 360
    '''
    server = {"id":1,"update_period":60,"cpu_wait":0.00847601288352903,                                                                                                                                                "cpu_user":2.98355653500492,                                                                                                                                                   
"load_avg15":0.35,                                                                                                                                                             
"load_avg01":0.02,                                                                                                                                                             
"date":1507457822,                                                                                                                                                             
"cpu_system":2.96660450923786,                                                                                                                                                 
"memory_percent":75.0,                                                                                                                                                         
"swap_percent":0.0,                                                                                                                                                            
"swap_megabyte":0.0,                                                                                                                                                           
"memory_megabyte":1535.6,                                                                                                                                                      
"load_avg05":0.27 }
'''
    print "=======host_list======:",server
    return render(request,'monitor/host_detail.html',{'server':server,'update_period': update_period})
    #return render(request,'monitor/host_detail.html',locals())

@login_required

def load_server_data(request, server_id):
    #server = Server.objects.get(id=server_id)
    #processes = server.process_set.all().order_by('name')
    #table_html = render_to_string('djangovisor/includes/server_table.html',{'server': server, 'processes': processes})
    #data = {'table_html': table_html, 'date': server.date_last, 'load_avg01': server.load_avg01_last,
    #        'load_avg05': server.load_avg05_last, 'load_avg15': server.load_avg15_last, 'cpu_user': server.cpu_user_last,
    #        'cpu_system': server.cpu_system_last, 'cpu_wait': server.cpu_wait_last, 'memory_percent': server.memory_percent_last,
    #        'memory_megabyte': server.memory_megabyte_last, 'swap_percent': server.swap_percent_last, 'swap_megabyte': server.swap_megabyte_last}

    data = {
"cpu_wait":0.00847601288352903,
"cpu_user":2.98355653500492,
"load_avg15":0.35,
"load_avg01":0.02,
"date":1507457822,
"cpu_system":2.96660450923786,
"memory_percent":75.0,
"swap_percent":0.0,
"swap_megabyte":0.0,
"memory_megabyte":1535.6,
"load_avg05":0.27
}
    return JsonResponse(data)

@login_required
def host_info(request, hostname, timing):
    temp_name = "monitor/index.html"
    # 传递磁盘号给前端JS,用以迭代分区图表
    '''
    disk = GetSysData(hostname, "disk", 3600, 1)
    disk_data = disk.get_data()
    partitions_len = []
    for d in disk_data:
        p = len(d["disk"])
        for x in range(p):
            partitions_len.append(x)
    # 传递网卡号给前端,用以迭代分区图表
    net = GetSysData(hostname, "net", 3600, 1)
    nic_data = net.get_data()
    nic_len = []
    for n in nic_data:
        p = len(n["net"])
        for x in range(p):
            nic_len.append(x)
    '''
    return render(request, "monitor/host_info_{}.html".format(timing), locals())

