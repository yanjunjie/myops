#-*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response,HttpResponse, redirect,render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import models,task
import os,json
import datetime
import time
from  paging import *
from ssh_api import *
from saltapi import *
from utils import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.

def index(request):
    return render(request,'index.html')

def hosts_index(request):
    return render(request,'hosts/dashboard.html')

def assets_index(request):
    return render(request,'assets/dashboard.html')

def monitor_index(request):
    return render(request,'monitor/dashboard.html')
def acc_logout(request):
    logout(request)

    return  HttpResponseRedirect("/")

def acc_login(requeset):
    login_err = ''
    if requeset.method == 'POST':
        username = requeset.POST.get('email')
        password = requeset.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(requeset,user)

            return HttpResponseRedirect('/')

        else:
            login_err = "Wrong username or password!"
    return  render(requeset,'login.html', {'login_err':login_err})


'''
def host_mgr(request):
   selected_gid = request.GET.get('selected_gid')
    if selected_gid:
        host_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)
    else:
        #host_list = request.user.bind_hosts.select_related()
        host_list = models.BindHostToUser.objects.all()
    data = {'host_list':host_list}
    print data
    return render(request,"hosts/host_mgr.html",data)
'''
def host_mgr(request):
    group_list = models.HostGroup.objects.all().values('id','name')
    #for g in group:
    #    group_list = g['name']
    return render_to_response('hosts/host_mgr.html',locals())


    

def hosts_list(request):
    hosts = []
    selected_gid = request.GET.get('selected_gid')
    if selected_gid:
       if selected_gid == 'all':
          host_list = models.Host.objects.all().values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')
       else:
          #host_list = models.Host.objects.all().values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')     
          h_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)
          #print "=========================",h_list
          host_list = []
          for h in h_list:
              h_id = h.host_id
              #print "hhhhhhhhhhhhhhhhhhhhhhhhhhhh",h_id
              host = models.Host.objects.all().filter(id = h_id).values('id','hostname','ip_addr','port','system_type','enabled','date','idc_id')
              #print "sssssssssssssssssssssssssssssss",host
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


@csrf_exempt
def file_manage(request,*args,**kw):
    selected_gid = request.GET.get('selected_gid')
    if selected_gid:
        host_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)
    else:
        #host_list = request.user.bind_hosts.select_related()
        host_list = models.BindHostToUser.objects.all()
    data = {'host_list':host_list}                                                                                                                      
    path = '/srv/salt/upload'
    s = SSH('192.168.91.132','22','root','rootroot')
    remote_file_list =  s.exec_command_list('ls %s' %path)
    return render(request,"hosts/manage_file.html",locals())
@csrf_exempt
def file_upload(request):
	#username,role_name,usergroup_name = get_session_user(request)
	#session_role_id = request.session['role_id']
	#nav = perm_nav(request)
	return render_to_response('hosts/file_upload.html')

@csrf_exempt
def uploadify_script(request):  
    	'''uploadfify filename is Filedata'''
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	upload_dir = os.path.join(base_dir,'upload')
	if os.path.isdir(upload_dir):
		pass
	else:
		os.mkdir(upload_dir)
    	file_obj = request.FILES.get("Filedata",None)  
    	if file_obj:
		filename = file_obj.name
		upload_file = os.path.join(upload_dir,filename)
		f = open(upload_file,'wb+')
		for chunk in file_obj.chunks():
			f.write(chunk)
		f.close()
	return HttpResponse("upload success")
@csrf_exempt
def handle_uploaded_file(request):
    order_no = request.POST.get('order_no','')
    host = request.POST.get('deploy_host','')
    user = request.POST.get('deploy_user','')
    file_req = request.FILES['uploadfile']
    file_name = file_req.name

    try:
        path = '/srv/salt/upload/' 
        if not os.path.exists(path):
            os.makedirs(path)
            destination = open(path + file_name, 'wb+')
            for chunk in file_req.chunks():
                destination.write(chunk)
            destination.close()
        else:
            destination = open(path + file_name, 'wb+')
            for chunk in file_req.chunks():
                destination.write(chunk)
            destination.close()
    except Exception, e:
        logging.error(e)
    
    return HttpResponse('upload succcessfully!')  
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Local_Dir = os.path.join(BASE_DIR,'upload')

@csrf_exempt
def upload_list(request):
	file_list = os.listdir(Local_Dir)
        '''分页'''
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1
        pagenum = 10
        p = paging(page,pagenum,file_list)
        pt = p.pt()
        ppn = p.ppn()
        npn = p.npn()
        pn = p.pn()
        pl = p.pl()
        if page < 9:
                pr = p.pr()[0:9]
        elif int(pn) - page < 9:
                pr = p.pr()[int(pn)-9:int(pn)]
        else:
                pr = p.pr()[page-9:page+8]
	return render_to_response('hosts/upload_list.html',locals())



def file_del(request):
	filename = request.POST.get('filename')
	try:
		r_filename = os.path.join(Local_Dir,filename)
		os.system('rm -rf %s' %r_filename)
		return HttpResponse('%s del success' %filename)
	except Exception as e:
		return HttpResponse('%s del failed,%s' %(filename,e))
@csrf_exempt
def file_send(request):
	filename = request.POST.get('filename')
	try:
		local_filename = os.path.join(Local_Dir,filename)
		remote_filename = os.path.join(saltstack_remote_dir,filename)
		ret = s.send_file(local_filename,remote_filename)
	except Exception as e:
		ret = "%s send failed,%s" %(filename,e)
	return HttpResponse(ret)


@csrf_exempt
def file_push(request):
    local_filename = request.POST.get('local_files')
    host_ip_req = request.POST.get('host_ip[]')
    host_name_req = request.POST.get('host_name[]')
    vhost_id_req = request.POST.get('host_ip[]', '').split(',')
    remote_path = request.POST.get('remote_path','')
    print request.POST

    selected_hosts = request.POST.getlist("host_name[]")
    saltkey = ','.join(selected_hosts)
    #upload_files = request.POST.getlist("local_files")
    #print "selected_hosts:", selected_hosts
    #print "upload_files:", upload_files
      
    salt_filename = "salt://upload/"+local_filename
    remote_filename = remote_path+"/"+local_filename
    arg = salt_filename.strip()+" "+ remote_filename.strip()
    print "====================================="
    print saltkey
    print arg
    #ret = SALTAPI.remote_noarg_execution1(selected_hosts,'cp.get_file',salt_filename.strip(),remote_filename.strip())['return'][0].items()
    ret = SALTAPI.remote_noarg_execution1(saltkey,'cp.get_file',arg)
    print ret

    return render_to_response('hosts/manage_file.html',locals())

@csrf_exempt
def multi_cmd(request):
    selected_gid = request.GET.get('selected_gid')                                                                                                                             
    host_ip_req = request.POST.get('host_ip[]')
    if selected_gid:                                                                                                                                                           
        host_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)                                                                                        
    else:                                                                                                                                                                      
        #host_list = request.user.bind_hosts.select_related()                                                                                                                  
        host_list = models.BindHostToUser.objects.all()                                                                                                                        
    data = {'host_list':host_list}                                                                                                                                             
    print "============data:",data
    return render(request,"hosts/cmd_mgr.html",locals())
@csrf_exempt
def command(request):
    cmd_req = request.POST.get('cmd_text').strip()
    selected_hosts = request.POST.getlist("host_name[]")
    #hostname_list = ','.join(selected_hosts)
    line = "################################################################"
    #result = {}
    #minion_id_list = []
    print request.POST
    print selected_hosts
    print "==host_list==",selected_hosts
    host_str = ",".join(selected_hosts)
    print "==host_str==",host_str
    ret = SALTAPI.shell_remote_execution(host_str, cmd_req)
    print ret
    minion_count = 'Total: ' + str(len(selected_hosts))
    cmd_succeed = 'Succeed: ' + str(len(ret))
    cmd_failure = 'Failure: ' + str(len(selected_hosts)-len(ret))
    cmd = 'Command: ' + cmd_req
    succeed_minion = []
    for i in ret:
        succeed_minion.append(i)
    failure_minion = 'Failure_Minion: ' + ','.join(list(set(selected_hosts).difference(set(succeed_minion))))
    print minion_count,cmd_succeed,cmd_failure,failure_minion
    print "=====================ret",ret
    data = [{
                                                                     'cmd': cmd,
                                                                     'hosts':host_str,
                                                                     'line': line,
                                                                     'minion_count': minion_count,
                                                                     'cmd_succeed': cmd_succeed,
                                                                     'cmd_failure': cmd_failure,
                                                                     'failure_minion': failure_minion
                                                                     }]
    
    data = {'msg': ret,'result':data}
    print "==================result:",data
    return HttpResponse(json.dumps(data,ensure_ascii=False))
    #return render(request,"hosts/cmd_mgr.html",locals())
    #return render(request,"hosts/cmd_result.html",result)                                                                  
    
def submit_task(request):
    print request.POST

    tas_obj = task.Task(request)
    res = tas_obj.handle()
    return HttpResponse("dddd")
