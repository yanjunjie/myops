#-*- coding: utf-8 -*-
from ssh_api import *
from utils import *
from time import sleep

#username = "weblogic"
#password = "weblogic"
#host_ip = "192.168.91.132"
#path = '/data/uploadpackage'
#s=SSH('192.168.91.132',22,'weblogic','weblogic')
#print s.exec_command_list('pwd;uptime')

#print s.send_file('/tmp/123','/tmp/123')
#print s.exec_command_list(r'cd /midware/script/'+username+'/deploy_all/;sh deploy-app.sh > '+username+'_deploy.log;')

#ssh2_deploy(host_ip,username,password,r'cd /midware/script/'+username+'/deploy_all/;sh deploy-app.sh > '+username+'_deploy.log;')
#while True:
#   result=ssh2_deploy(host_ip,r'cd /midware/script/weblogic/deploy_all/;grep releaseok  deploy.log')
#   if (len(result)>0):
#      break;
#   else:
#     sleep(10)
#result = ssh2_deploy(host_ip,username,password, r'cd /midware/script/'+username+'/deploy_all/;grep releaseok '+username+'_deploy.log;')

hostname = "192.168.91.132"
create_host_user_cmd = 'df' 

#ssh2
ssh2(hostname,create_host_user_cmd)
#ssh2_trust(hostname,create_host_user_cmd)


