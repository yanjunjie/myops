#-*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response,HttpResponse, redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from hosts import models
from hosts.views import *
import os,json,time
import time
import datetime
from os.path import splitext
from hosts.utils import *
from time import sleep
from datetime import date, datetime
today = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
def demo(request):
  return render_to_response('applications/demo.html')

def services_demo(request):
  data=[{"id": 1,"instance":"apche1","type":"Apache","project":"前置一区","path": "/apache","host": "192.168.1.2","status": "1"},{"id": 1,"instance":"apche2","type":"Apache","project":"前置一区","path": "/apache","host": "192.168.1.2","status": "1"},{"id": 1,"instance":"java","type":"Java","project":"前置一区","path": "/midware/jdk1.7","host": "192.168.1.2","status": "1"},{"id": 1,"instance":"zookeeper","type":"zookeeper","project":"前置一区","path": "/apache","host": "192.168.1.2","status": "0"}]
  return HttpResponse(json.dumps(data,ensure_ascii=False))

def demo_data_test(request):
  #data=[{"pid": 2222,"path": "/midware/app/01","host": "192.168.1.2","CPU": "0.1 0.2 0.3","status": "Down"},{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.3","CPU": "0.1 0.2","status": "RUNNING"},{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.4","cpu": "0.1 0.2 0.3","status": "RUNNING"},{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.5","CPU":"1 0.2 0.3","status": "Down"}]
  #data=[{"id": 1,"name": "服务受理","adminServer": "AdminServer","adminPort":"7140","clusterName":"dispatch_cluster","subsys":"服务受理子系统","host":"20.8.100.1","status": "部分启动"},{"id": 2,"name": "服务受理","adminServer": "AdminServer","adminPort":"7140","clusterName":"dispatch_cluster","subsys":"服务受理子系统","host":"20.8.100.1","status": "部分启动"}]
  return HttpResponse(json.dumps(data,ensure_ascii=False))


#部署类型-java父表数据
@login_required
def java_data(request):
  #data=[{"id": 1,"project": "个人加载服务","package": "collt-ntr-loader","subsys": "金融类个人加载子系统","status": "部分启动"},{"id": 0,"project": "个人加载服务","package": "collt-ntr-loader","subsys": "金融类个人加载子系统","status": "部分启动"}]

  server_id = models.java_server.objects.all();
  for id in server_id:
      status = []
      sid = id.id
      print "sid=================",sid
      process = id.process.all()
      for item in process:
          status.append(item.status)
      print "==========status=========",status
      leng = len(status)
      if status.count('0') == leng:
         models.java_server.objects.filter(id=sid).update(status='0')
      elif status.count('1') == leng:
         models.java_server.objects.filter(id=sid).update(status='1')
      else:
         models.java_server.objects.filter(id=sid).update(status='2')

  server = models.java_server.objects.all().values('id','name','app_id','status').order_by('id');
  print server
  data = []
  for id in server:
     app_id = id['app_id']
     print "app_id:",app_id
     app = models.App.objects.filter(id = app_id).values('id','name','subsys_id','package').order_by('id');
     subsys_id = app[0]['subsys_id']
     subsys_name = models.Subsys.objects.all().filter(id = subsys_id).distinct().values('name')
     print "subsys_name:",subsys_name
     data.append({'id':id['id'],'project':id['name'],'package':app[0]['package'],'subsys':subsys_name[0]['name'],'status':id['status']})
  print data
  return HttpResponse(json.dumps(data,ensure_ascii=False))
'''
#部署类型-weblogic父表数据
def wls_data(request):
  data = []
  adminserver = models.weblogic_admin.objects.all().values('id','name','console_port','cluster','server_status','primary_id').order_by('id');
  print adminserver
  for item in adminserver:
    id = item['id']
    admin_host_id = item['primary_id']
    host = models.Host.objects.filter(id = admin_host_id).values('ip_addr','hostname')
    #server_id = models.weblogic_admin.objects.get(id=id)
    #server = server_id.serverhost.all()
    #for i in server:
    #  appsid = i.apps_id_id
    #  print "appsid=========",appsid
    #  apps_id = models.App.objects.filter(id=appsid).values('id','subsys_id').order_by('id');
    #  subsys_id = apps_id[0]['subsys_id']
    #  subsys_name = models.Subsys.objects.all().filter(id = subsys_id).distinct().values('name')
    #  print "subsys_name:========",subsys_name
    #print server
    data.append({'id':id,'name':item['name'],'adminServer':'AdminServer','adminPort':item['console_port'],'clusterName':item['cluster'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr'],'status':item['server_status']})
  print data
  return HttpResponse(json.dumps(data,ensure_ascii=False))
'''
#部署类型-weblogic父表数据

def wls_data(request):
  data = []
  status = []
  server_id = models.weblogic_admin.objects.all();
  for id in server_id:
      sid = id.id
      server = id.serverhost.all()
      for item in server:
          status.append(item.server_status)
      leng = len(status)
      if status.count('0') == leng:                                                                                                                                                
         models.weblogic_admin.objects.filter(id=sid).update(server_status='0')                                                                                                   
      elif status.count('1') == leng:                                                                                                                                              
         models.weblogic_admin.objects.filter(id=sid).update(server_status='1')                                                                                                   
      else:                                                                                                                                                                    
         models.weblogic_admin.objects.filter(id=sid).update(server_status='2') 
  adminserver = models.weblogic_admin.objects.all().values('id','name','console_port','cluster','server_status','primary_id').order_by('id');
  print adminserver
  for item in adminserver:
      id = item['id']
      admin_host_id = item['primary_id']
      host = models.Host.objects.filter(id = admin_host_id).values('ip_addr','hostname')
      data.append({'id':id,'name':item['name'],'adminServer':'AdminServer','adminPort':item['console_port'],'clusterName':item['cluster'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr'],'status':item['server_status']})
  return HttpResponse(json.dumps(data,ensure_ascii=False))



#部署类型-weblogic子表数据
def wls_data_sub(request):
  id = request.GET.get('id')
  data=[]
  status=[]
  server_id = models.weblogic_admin.objects.get(id=id)
  server = server_id.serverhost.all()
  for item in server:
      status.append(item.server_status)
      appsid = item.apps_id_id
      managed_host_id = item.managed_server_id_id
      host = models.Host.objects.filter(id = managed_host_id).values('ip_addr','hostname')
      print "appsid=========",appsid
      apps_id = models.App.objects.filter(id=appsid).values('id','name','subsys_id','package','path').order_by('id');
      subsys_id = apps_id[0]['subsys_id']
      subsys_name = models.Subsys.objects.all().filter(id = subsys_id).distinct().values('name')
      print "subsys_name:========",subsys_name
      data.append({'id':item.id,'managedServer':item.server_name,'managed_port':item.server_port,'server_status':item.server_status,'project_name':apps_id[0]['name'],'package':apps_id[0]['package'],'path':apps_id[0]['path'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr']})
  print data
  leng = len(status)
  if status.count('0') == leng:                                                                                                                          
       models.weblogic_admin.objects.filter(id=id).update(server_status='0')                                                                                         
  elif status.count('1') == leng:                                                                                                                        
       models.weblogic_admin.objects.filter(id=id).update(server_status='1')                                                                                         
  else:                                                                                                                                                  
       models.weblogic_admin.objects.filter(id=id).update(server_status='2')                                                                                         
  return HttpResponse(json.dumps(data,ensure_ascii=False))

#部署类型-java子表数据
@login_required
def java_data_sub(request):
    #data=[{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.2","CPU": "0.1 0.2 0.3","status": "Down"},{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.3","CPU": "0.1 0.2 0.3","status": "RUNNING"},{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.4","cpu": "0.1 0.2 0.3","status": "RUNNING"},{"pid": 1234,"path": "/midware/app/01","host": "192.168.1.5","CPU": "0.1 0.2 0.3","status": "Down"}]
    id = request.GET.get('id')
    data = []
    status = []
    #process_id =  models.java_server_process.objects.filter(java_server_id = id).values('name').order_by('id');
    process_id = models.java_server.objects.get(id=id) 
    print "888888888888888888888888888",process_id
    #process = process_id.process.all().values('id','name','pid','path','port','cpu','date','status','host_id')
    process = process_id.process.all()
    for item in process:
        status.append(item.status)
        host = models.Host.objects.filter(id = item.host_id).values('ip_addr')
        data.append({'id':item.id,'name':item.name,'pid':item.pid,'path':item.path,'port':item.port,'cpu':item.cpu,'last_date':item.date,'status':item.status,'host':host[0]['ip_addr']})
    print "ddddddddddddddddddddddddddddddddddddddddddddddddddd",data
    return HttpResponse(json.dumps(data,ensure_ascii=False,default=json_serial))



#启动Java单个进程
@csrf_exempt
def process_ops(request):
    print "=================equest.POST=======",request.POST                                                         
    
    id = request.POST.get('ID')
    host = request.POST.get('HOST')
    path = request.POST.get('PATH')
    ops = request.POST.get('OPS')
    #status='0'
    list = []
    message = ''
    if ops == "start":
       cmd = 'cd '+path+ ';' + 'sh cmd.sh start'
       ssh2(host,cmd)     
       models.java_process.objects.filter(id=id).update(status='0',date=today)
       status = models.java_process.objects.all().values('status')
       message = u'操作成功'
    else:
       cmd = 'cd '+path+ ';' + 'sh cmd.sh stop'
       ssh2(host,cmd)     
       models.java_process.objects.filter(id=id).update(status='1',date=today)
       message = u'操作成功'

    return HttpResponse(message) 
     
#启动weblogic实例
@csrf_exempt
def wlsprocess_ops(request):
    print "=================equest.POST=======",request.POST
    path = "/midware/applications"
    id = request.POST.get('ID')
    host = request.POST.get('HOST')
    #path = request.POST.get('PATH')
    server = request.POST.get('SRV')
    ops = request.POST.get('OPS')
    print "11111111111111",today
    message = ''
    if ops == "start":
       cmd = 'cd '+path+ ';' + 'sh '+'start-'+server+'.sh'
       result_cmd = ssh2(host,cmd)
       result = ssh2(host, r"ps -ef|grep top |grep -v grep |awk '{print $2}';")
       print result
       if (len(result)>0):
          result = result[0]
          models.weblogic_server.objects.filter(id=id).update(server_status='0',date=today)
          message = u'操作成功,运行实例为: '+server+'(PID '+result+')'
       else:
          message = u'操作失败'
    else:
       cmd = 'cd '+path+ ';' + 'sh '+'stop-'+server+'.sh'
       ssh2(host,cmd)                                                                                                                                      
       result = ssh2(host, r"ps -ef|grep top1 |grep -v grep |awk '{print $2}';")
       if (len(result)>0):
          result = result[0]
          message = u'操作失败,运行实例为: '+server+'(PID '+result+')'
       else:
          models.weblogic_server.objects.filter(id=id).update(server_status='1',date=today)                                                                                        
          message = u'操作成功'
    return HttpResponse(message)

@login_required
def app_mgr_data(request):
    selected_gid = request.GET.get('selected_gid')
    subsys = models.Subsys.objects.all().values('id','name','memo').order_by('id');
    hosts = [] 
    if selected_gid:
       if selected_gid == 'all':
          app_list = models.App.objects.all().values('id','name','package','path','memo','subsys_id').order_by('id');
       else:
          #app_list = models.App.objects.filter(subsys_id =selected_gid).values('name','memo').order_by('id');
          app_list = models.App.objects.filter(subsys__id = selected_gid).values('id','name','package','path','memo','subsys_id').order_by('id');
    else:
        #app_list = models.App.objects.all().values('name','memo').order_by('id');
        app_list = models.App.objects.all().values('id','name','package','path','memo','subsys_id').order_by('id');
    print "================app_list===================",app_list
    for app in app_list:
        app_id = app['id']
        app_name = app['name']
        subsys_id = app['subsys_id']
        print "app_id:",app_id
        print "subsys_id:",subsys_id
        subsys_name = models.Subsys.objects.all().filter(id = subsys_id).distinct().values('name')
        print "subsys_name:",subsys_name
        app_host_id = models.App_host.objects.all().filter(app_id = app_id).distinct().values('host_id')
        print "app_host_id:",app_host_id
        for id in app_host_id:
           app_host_id = id['host_id']
           app_host = models.Host.objects.all().filter(id = app_host_id).distinct().values('ip_addr')
           print "app_host:",app_host
           hosts.append({'app_name':app['name'],'app_package':app['package'],'app_path':app['path'],'subsys_name': subsys_name[0]['name'],'app_host':app_host[0]['ip_addr']})
    #data = {'app_list':app_list}
    print "hosts==",hosts
    return HttpResponse(json.dumps(hosts,ensure_ascii=False))
    #return render(request,"applications/app_mgr.html",{'app_list':hosts,'subsys':subsys})

def app_mgr(request):
  subsys = models.Subsys.objects.all().values('id','name','memo').order_by('id');
    
  return render_to_response('applications/app_mgr.html',locals())


@csrf_exempt
def file_del(request):
	filename = request.POST.get('filename')
        Local_Dir = '/srv/salt/upload'
        print filename
	try:
		r_filename = os.path.join(Local_Dir,filename)
		os.system('rm -rf %s' %r_filename)
		return HttpResponse('%s del success' %filename)
	except Exception as e:
		return HttpResponse('%s del failed,%s' %(filename,e))

#程序部署-状态标签页
def deploy_info(request):
  server_list_status = []
  status=[]
  data=[]
  adminserver = models.weblogic_admin.objects.all().values('id','name','console_port','cluster','server_status','admin_status','primary_id','create_date').order_by('id');                    
  path = '/srv/salt/upload'
  remote_file_list =  ssh2('192.168.91.132','ls %s' %path)
  for file in remote_file_list:                                                                                                                                              
        f = file.strip()                                                                                                                                                       
        mtime = time.ctime(os.path.getmtime(path+"/"+f))                                                                                                                       
        #print "Last modified : %s" % (mtime)                                                                                                                                  
        data.append({'file':file,'mtime':mtime})            
  for item in adminserver:                                                                                                                                                     
    id = item['id']                                                                                                                                                            
    admin_host_id = item['primary_id']                                                                                                                                         
    host = models.Host.objects.filter(id = admin_host_id).values('ip_addr','hostname')                                                                                         
    server_id = models.weblogic_admin.objects.get(id=id)
    server = server_id.serverhost.all()                                                                                                                                       
    status.append(item['admin_status'])
    server_list_status.append({'id':id,'name':item['name'],'ServerName':'AdminServer','Port':item['console_port'],'project_name':item['name'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr'],'admin_status':item['admin_status'],'last_date':item['create_date']})
    for item in server:                                                                                                                                                          
       status.append(item.server_status)
       appsid = item.apps_id_id
       managed_host_id = item.managed_server_id_id
       host = models.Host.objects.filter(id = managed_host_id).values('ip_addr','hostname')
       apps_id = models.App.objects.filter(id=appsid).values('id','name','subsys_id','package','path').order_by('id');
       server_list_status.append({'id':item.id,'ServerName':item.server_name,'Port':item.server_port,'server_status':item.server_status,'project_name':apps_id[0]['name'],'package':apps_id[0]['package'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr'],'last_date':item.date})
  count = len(server_list_status)
  running = status.count('0')
  stopped = status.count('1')
  server_status = [{'count':count,'running':running,'stopped':stopped}]
  
  print "======================data============",server_list_status
  return render(request,"applications/deploy_info.html",locals())

'''
def deploy_info(request,*args,**kw):
    selected_gid = request.GET.get('selected_gid')
    s = SSH('192.168.91.132','22','root','rootroot')
    path = '/srv/salt/upload'
    data = []
    hosts = []
    server_hosts = {}
    server_list_status = []
    remote_file_list =  s.exec_command_list('ls %s' %path)                                                           
    for file in remote_file_list:                                                                                    
        f = file.strip()                                                                                             
        mtime = time.ctime(os.path.getmtime(path+"/"+f))                                                             
        #print "Last modified : %s" % (mtime)                                                                        
        data.append({'file':file,'mtime':mtime})
    if selected_gid:                                                                                                
        host_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)                             
    else:                                                                                                           
        host_list = models.BindHostToUser.objects.all()                      
    admin_info = models.weblogic_admin.objects.all().distinct().values('id','name','console_port','cluster','primary_id').order_by('id');
    for _id in admin_info:
        primary_id = _id['primary_id']
        admin_id = _id['id']
        print "44444444444444444444444",primary_id
        admin_host_ip = models.Host.objects.all().filter(id = primary_id).distinct().values('ip_addr','hostname')
        print "3333333333333333333333333",admin_host_ip
         
        server_id = models.weblogic_admin_serverhost.objects.all().filter(weblogic_admin_id = admin_id).distinct().values('weblogic_server_id')
        print "5555555555555555555555555555",server_id
        serverhost_dic=[]
        for id in server_id:
            server_id = id['weblogic_server_id']
            server_name = models.weblogic_server.objects.all().filter(id = server_id).distinct().values('server_name')
            print "66666666666666666666666666",server_name
            name = server_name[0]                                                                             
            name_values = name.values()                                                                         
            values = ','.join(name_values)                                                                           
            serverhost_dic.append(values)                                                                          
            host_dic = ','.join(serverhost_dic)                                                                     
        server_hosts[admin_id] = host_dic       
        print "7777777777777777777777777",server_hosts
        hosts.append({'hostname':admin_host_ip[0]['hostname'],'ip_addr':admin_host_ip[0]['ip_addr'],'admin_port':_id['console_port'],'cluster_name':_id['cluster'],'server_name':host_dic,'name':_id['name']})
        print "88888888888888888888888888888888",hosts
    server_info = models.weblogic_server.objects.all().distinct().values('server_name','server_port','server_status','managed_server_id_id','apps_id_id','date')
    for server_id in server_info:
        host_id = server_id['managed_server_id_id']
        apps_id = server_id['apps_id_id']
        host_ip =  models.Host.objects.all().filter(id = host_id).distinct().values('ip_addr','hostname')
        print "9999999999999999999999999999999999",host_ip
        ip_addr = host_ip[0]['ip_addr'] 
        app_list = models.App.objects.all().filter(id = apps_id).distinct().values('name','package')
        print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",app_list
        server_list_status.append({'server_name':server_id['server_name'],'project_name':app_list[0]['name'],'apps_name':app_list[0]['package'],'server_status':server_id['server_status'],'server_date':server_id['date'],'managed_server':host_ip[0]['ip_addr']})
        print "======================server_list_status[]==================",server_list_status
        
    return render(request,"applications/deploy_info.html",locals())
'''

@csrf_exempt
def deploy_run(request):
    
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day
    Date = '%d-%d-%d'% (year,month,day)

    local_filename = request.POST.get('local_files')
    host_ip_req = request.POST.get('host_ip[]')
    host_name_req = request.POST.get('host_name[]')
    admin_port = request.POST.get('admin_port[]')
    cluster_name = request.POST.get('cluster_name[]')
    vhost_id_req = request.POST.get('host_ip[]', '').split(',')
    #remote_path = request.POST.get('remote_path','')
    jremote_path = "/java/applications" 
    path = "/tmp" 
    app_path = "/midware/applications" 
    bak_path = "/midware/applications_backup" 
    file_name = local_filename.strip()
    files_sp = splitext(file_name)[0]
    upload_path = "/srv/salt/upload"
    print "=================equest.POST=======",request.POST
    
    
    selected_hosts_name = request.POST.getlist("host_name[]")
    saltkey = ','.join(selected_hosts_name)
    selected_hosts_ip = request.POST.getlist("host_ip[]")
    host_ip = ','.join(selected_hosts_ip)
    #upload_files = request.POST.getlist("local_files")
    salt_filename = "salt://upload/"+local_filename
    print "====================================="
    print saltkey
    select_type = request.POST.get('select_type').strip()
    dep_type = request.POST.get('dep_type').strip()
    cmd = ''
    path = "/tmp"
    tmp_path = '%s/apps/%s' %(path,Date)
    f = os.path.exists(tmp_path)                                                                                                                                             
    if f == False:                                                                                                                                                           
       os.system('%s %s' %('mkdir -p',tmp_path)) 

    if select_type == "java":
      print "exc java shell"
      #ret = SALTAPI.remote_noarg_execution1(saltkey,'cp.get_file',jarg)
      sftp2(host_ip,upload_path +"/"+ file_name,'/tmp/applications/java/'+file_name)
      cmd = r'cd /tmp/applications/java;tar xf '+file_name+';cp -Rf '+files_sp+'  /java/applications/'
      ssh2_deploy(host_ip,cmd)
    elif select_type == "weblogic":
      if dep_type == "update":
         print "exc weblogic update shell"
         cmd = r'cd '+app_path+';tar cvf '+bak_path+'/'+files_sp+'_'+Date+'.tar '+files_sp+''
         ssh2_deploy(host_ip,cmd)
      else:
         print "exc weblogic deploy shell"
      sftp2(host_ip,upload_path +"/"+ file_name,tmp_path+"/"+file_name)
      #cmd = r'cd '+app_path+';tar cvf '+bak_path+'/'+files_sp+'.tar-'+Date+' '+files_sp+''
      cmd = r'cd '+tmp_path+';unzip -o -d '+files_sp+' '+file_name+';cp -Rf '+files_sp+'  '+app_path+''
      ssh2_deploy(host_ip,cmd)
      #autodeploy.py 192.168.91.132 8000 helloworld Cluster1 deploy
      cmd_deploy = r'cd /midware/script/weblogic/deploy_all/;sh autodeploy.sh '+host_ip+' '+admin_port+' '+files_sp+' '+cluster_name+' deploy >> deploy.log;'
      ssh2_deploy(host_ip,cmd_deploy)
      while True:
          result = ssh2_deploy(host_ip, r'cd /midware/script/weblogic/deploy_all/;grep completed deploy.log;')
          if (len(result)>0):
              break;
          else:
             sleep(10)
      
      ssh2_deploy(host_ip,r'cd /midware/script/weblogic/deploy_all/;sh my_weblogic.sh stop > stop-server-all.log;')

      while True:
            result = ssh2_deploy(host_ip, r'cd /midware/script/weblogic/deploy_all/;grep stopped stop-server-all.log;')
            if (len(result)>0):
                break;
            else:
                sleep(10)
        
      ssh2_deploy(host_ip,r'cd /midware/script/weblogic/deploy_all/;sh my_weblogic.sh start > start-server-all.log; ')
      while True:
            #result = ssh2_deploy_log(host_ip, r"cd /midware/logs/;awk 'NF{a=$0}END{print a}' "+module+"-?01-srv01-"+(datetime.now().date()).strftime('%Y%m%d')+".log|grep -i RUNNING ;")
            result = ssh2_deploy_log(host_ip, r"cd /midware/logs/;awk 'NF{a=$0}END{print a}' Server-0-"+(datetime.now().date()).strftime('%Y%m%d')+".log|grep -i RUNNING ;")
            if (len(result)>0):
                break;
            else:
                sleep(5) 
    else:
      print "xxxxx"
    return HttpResponse('部署成功!')
    #return render_to_response('applications/deploy_info.html',locals())
@csrf_exempt
def getlog_deploy_log(request):
    
    line_req = request.POST.get('linenumber','1')
    selected_hosts_ip = request.POST.getlist("host_ip[]")
    host_ip = ','.join(selected_hosts_ip)
    logfile_req = '/midware/script/weblogic/deploy_all/deploy.log'
    #result = ssh2_deploy_log(host_ip, r"cd /tmp/applications/java;set a=`wc -l deploy.log | awk '{print $1}'`;echo ${a};sed -n "+str(linenumber)+",${a}p deploy.log")
    #result = ssh2_deploy_log(host_ip, r"cd /tmp/applications/java;set a=`wc -l deploy.log | awk '{print $1}'`;echo ${a};sed -n "+linenumber+",${a}p deploy.log")
    result = ssh2_deploy_log(host_ip, r"line=`wc -l "+logfile_req+"|awk '{print $1}'`;echo ${line};sed -n "+str(line_req)+",${line}p "+logfile_req+"")
    #print result
    print "######################result########################################"                                                                                               
    result = result.split('\n')                                                                                                                                                
    linenumber = int(result[0])                                                                                                                                                
    linetxt = result[1:]
    data = {'linenumber':linenumber,'log':linetxt}
    print data
    return HttpResponse(json.dumps(data,ensure_ascii=False))



#批量启动Java进程
@csrf_exempt
def instance_ops(request):
    print "=================equest.POST=======",request.POST
     
    id = request.POST.get('ID')
    ops = request.POST.get('OPS')
    message = ''
      
    process_id = models.java_server.objects.get(id=id)
    process = process_id.process.all()

    for item in process:
        print item.name
        id = item.id
        host = models.Host.objects.filter(id = item.host_id).values('ip_addr')
        host = host[0]['ip_addr']
        path = item.path
         
        if ops == "start":
           cmd = 'cd '+path+ ';' + 'sh cmd.sh start'
           ssh2(host,cmd)
           models.java_process.objects.filter(id=id).update(status='0',date=today)
           message = u'操作成功'
        else:
           cmd = 'cd '+path+ ';' + 'sh cmd.sh stop'
           ssh2(host,cmd)
           models.java_process.objects.filter(id=id).update(status='1',date=today)
           message = u'操作成功'

    return HttpResponse(message)
    
#启动weblogic实例
@csrf_exempt
def wlsinstance_ops(request):
    print "=================equest.POST=======",request.POST
    id = request.POST.get('ID')
    ops = request.POST.get('OPS')
    message = ''
     
    server_id = models.weblogic_admin.objects.get(id=id)
    server = server_id.serverhost.all()
    for item in server:                                                                                                                                      
        id = item.id
        appsid = item.apps_id_id
        managed_host_id = item.managed_server_id_id
        server = item.server_name
        hostid = models.Host.objects.filter(id = managed_host_id).values('ip_addr','hostname')
        apps_id = models.App.objects.filter(id=appsid).values('id','name','subsys_id','package','path').order_by('id');
        host = hostid[0]['ip_addr']
        path = apps_id[0]['path']
        print id,host,path
        if ops == "start":                                                                                                                                 
           cmd = 'cd '+path+ ';' + 'sh '+'start-'+server+'.sh'                                                                                             
           ssh2(host,cmd)                                                                                                                                  
           models.weblogic_server.objects.filter(id=id).update(server_status='0',date=today)                                                                          
           message = u'操作成功'                                                                                                                           
        else:                                                                                                                                              
           cmd = 'cd '+path+ ';' + 'sh '+'stop-'+server+'.sh'                                                                                             
           ssh2(host,cmd)                                                                                                                                  
           models.weblogic_server.objects.filter(id=id).update(server_status='1',date=today)                                                                          
           message = u'操作成功'                                                                                                                           
    return HttpResponse(message)

def services(request):
  middleware_type = models.middleware.objects.all().values('id','name','version').order_by('id');

  server_list_status = []
  status=[]
  data=[]
  adminserver = models.weblogic_admin.objects.all().values('id','name','console_port','cluster','server_status','admin_status','primary_id','create_date').order_by('id');                    
  path = '/srv/salt/upload'
  remote_file_list =  ssh2('192.168.91.132','ls %s' %path)
  for file in remote_file_list:                                                                                                                                              
        f = file.strip()                                                                                                                                                       
        mtime = time.ctime(os.path.getmtime(path+"/"+f))                                                                                                                       
        #print "Last modified : %s" % (mtime)                                                                                                                                  
        data.append({'file':file,'mtime':mtime})            
  for item in adminserver:                                                                                                                                                     
    id = item['id']                                                                                                                                                            
    admin_host_id = item['primary_id']                                                                                                                                         
    host = models.Host.objects.filter(id = admin_host_id).values('ip_addr','hostname')                                                                                         
    server_id = models.weblogic_admin.objects.get(id=id)
    server = server_id.serverhost.all()                                                                                                                                       
    status.append(item['admin_status'])
    server_list_status.append({'id':id,'name':item['name'],'ServerName':'AdminServer','Port':item['console_port'],'project_name':item['name'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr'],'admin_status':item['admin_status'],'last_date':item['create_date']})
    for item in server:                                                                                                                                                          
       status.append(item.server_status)
       appsid = item.apps_id_id
       managed_host_id = item.managed_server_id_id
       host = models.Host.objects.filter(id = managed_host_id).values('ip_addr','hostname')
       apps_id = models.App.objects.filter(id=appsid).values('id','name','subsys_id','package','path').order_by('id');
       server_list_status.append({'id':item.id,'ServerName':item.server_name,'Port':item.server_port,'server_status':item.server_status,'project_name':apps_id[0]['name'],'package':apps_id[0]['package'],'hostname':host[0]['hostname'],'host':host[0]['ip_addr'],'last_date':item.date})
  count = len(server_list_status)
  running = status.count('0')
  stopped = status.count('1')
  server_status = [{'count':count,'running':running,'stopped':stopped}]
  
  print "======================data============",server_list_status
  return render_to_response('applications/services.html',locals())

def services_data(request):
  print "=================equest.POST=======",request.GET
  type = request.GET.get('Type')
  print "==========type:",type
  data = []
  if type == "Apache":
  	web_server = models.web_server.objects.all().values('id','name','project','path','date','host_id','type_id','status').order_by('id');
  	for id in web_server:
    		host_id = id['host_id']
    		type_id = id['type_id']
    		host = models.Host.objects.filter(id = host_id).values('ip_addr','hostname')
    		type = models.middleware.objects.filter(id = type_id).values('name','version')
    		data.append({'id':id['id'],'instance':id['name'],'type':type[0]['name'],'project':id['project'],'path':id['path'],'host':host[0]['ip_addr'],'status':id['status']})
  elif type == 'zookeeper': 
        zk_server = models.zk_server.objects.all().values('id','name','project','path','date','host_id','type_id','status').order_by('id');
  	for id in zk_server:
    		host_id = id['host_id']
    		type_id = id['type_id']
    		host = models.Host.objects.filter(id = host_id).values('ip_addr','hostname')
    		type = models.middleware.objects.filter(id = type_id).values('name','version')
  		data.append({'id':id['id'],'instance':id['name'],'type':type[0]['name'],'project':id['project'],'path':id['path'],'host':host[0]['ip_addr'],'status':id['status']})
  elif type == 'all':
        web_server = models.web_server.objects.all().values('id','name','project','path','date','host_id','type_id','status').order_by('id');
        for id in web_server:
                host_id = id['host_id']
                type_id = id['type_id']
                host = models.Host.objects.filter(id = host_id).values('ip_addr','hostname')
                type = models.middleware.objects.filter(id = type_id).values('name','version')
                data.append({'id':id['id'],'instance':id['name'],'type':type[0]['name'],'project':id['project'],'path':id['path'],'host':host[0]['ip_addr'],'status':id['status']})
        zk_server = models.zk_server.objects.all().values('id','name','project','path','date','host_id','type_id','status').order_by('id');
        for id in zk_server:
                host_id = id['host_id']
                type_id = id['type_id']
                host = models.Host.objects.filter(id = host_id).values('ip_addr','hostname')
                type = models.middleware.objects.filter(id = type_id).values('name','version')
                data.append({'id':id['id'],'instance':id['name'],'type':type[0]['name'],'project':id['project'],'path':id['path'],'host':host[0]['ip_addr'],'status':id['status']})
  else:
      print "==="
  print "===========data:",data
  return HttpResponse(json.dumps(data,ensure_ascii=False))


    

@csrf_exempt
def service_ops(request):
    print "=================equest.POST=======",request.POST

    id = request.POST.get('ID')
    host = request.POST.get('HOST')
    path = request.POST.get('PATH')
    ops = request.POST.get('OPS')
    type = request.POST.get('TYPE')
    #status='0'
    list = []
    
    message = ''
    if type == 'Apache':
       if ops == "start":
          print "apsche start"
          cmd = 'cd '+path+ ';' + 'sh start_script.sh'
          ssh2(host,cmd)
          models.web_server.objects.filter(id=id).update(status='0',date=today)
          message = u'操作成功'
       else:
          print "apache stop"
          cmd = 'cd '+path+ ';' + 'sh stop_script'
          ssh2(host,cmd)
          models.web_server.objects.filter(id=id).update(status='1',date=today)
          message = u'操作成功'
    elif type == 'zookeeper':
       if ops == "start":                                                                                                                                                      
          print "zookeeper start"
          cmd = 'cd '+path+ ';' + 'sh start_script.sh'                                                                                                                            
          ssh2(host,cmd)                                                                                                                                                       
          models.zk_server.objects.filter(id=id).update(status='0',date=today)
          status = models.java_process.objects.all().values('status')                                                                                                          
          message = u'操作成功'                                                                                                                                                
       else:                                                                                                                                                                   
          print "zookeeper stop"
          cmd = 'cd '+path+ ';' + 'sh stop_script'                                                                                                                             
          ssh2(host,cmd)                                                                                                                                                       
          models.zk_server.objects.filter(id=id).update(status='1',date=today)                                                                                                         
          message = u'操作成功'                
    else:
         print "==="
    return HttpResponse(message)





def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime)):
        serial = obj.strftime('%Y-%m-%d %H:%M:%S')
        return serial
    elif isinstance(obj, date):
        serial = obj.strftime('%Y-%m-%d')
        return serial
    raise TypeError ("Type %s not serializable" % type(obj))

