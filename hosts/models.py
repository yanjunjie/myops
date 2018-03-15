#_*_coding:utf-8_*_

from django.db import models

# Create your models here.
from myauth import UserProfile

class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)
    idc = models.ForeignKey('IDC')
    system_type_choices= (
        ('linux(vm)','Linux(VM)'),
        ('linux(p)','Linux(P)'),
    )
    system_type = models.CharField(choices=system_type_choices,max_length=32,default='linux')
    enabled = models.BooleanField(default=True)
    memo = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return  "%s(%s)" %(self.hostname,self.ip_addr)
    class Meta:
        verbose_name = u'主机列表'
        verbose_name_plural = u"主机列表"
class IDC(models.Model):
    name = models.CharField(unique=True,max_length=64)
    memo = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return  self.name

class HostUser(models.Model):
    auth_type_choices = (
        ('ssh-password', 'SSH/PASSWORD'),
        ('ssh-key', 'SSH/KEY'),
    )
    auth_type = models.CharField(choices=auth_type_choices,max_length=32,default='ssh-password')
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128,blank=True,null=True)

    def __unicode__(self):
        return "(%s)%s" %(self.auth_type,self.username)

    class Meta:
        unique_together = ('auth_type','username','password')
        verbose_name = u'远程主机用户'
        verbose_name_plural = u"远程主机用户"
class HostGroup(models.Model):
    name = models.CharField(unique=True,max_length=64)
    memo = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return  self.name
    class Meta:
        verbose_name = u'主机组'
        verbose_name_plural = u"主机组"
class BindHostToUser(models.Model):
    host = models.ForeignKey("Host")
    host_user= models.ForeignKey("HostUser")
    #host_user= models.ManyToManyField("HostUser")
    host_groups = models.ManyToManyField("HostGroup")

    class Meta:
        unique_together = ('host','host_user')
        verbose_name = u'主机与用户绑定关系'
        verbose_name_plural = u"主机与用户绑定关系"
    def __unicode__(self):
        return  '%s:%s' %(self.host.hostname, self.host_user.username)


    def get_groups(self):

        return ','.join([g.name for g in self.host_groups.select_related()])

class middleware(models.Model):
    name = models.CharField(verbose_name = "中间件名", max_length=50,null=True,blank=True)
    version = models.CharField(verbose_name = "中间件版本", max_length=50,null=True,blank=True)
    class Meta:
        managed =True
        verbose_name = "中间件"
        verbose_name_plural = "中间件"
    def __unicode__(self):
        return self.name

class app_user(models.Model):
    username = models.CharField(verbose_name = "用户名", max_length=20)
    password = models.CharField(verbose_name = "密码", max_length=20)
    middleware = models.ManyToManyField('middleware')
    class Meta:
        managed =True
        verbose_name = "中间件用户"
        verbose_name_plural = "中间件用户"
    
    def __unicode__(self):
        return self.username

    def get_middleware(self):
        return ','.join([g.name for g in self.middleware.select_related()])

class Subsys(models.Model):
    name = models.CharField(max_length=64)
    memo = models.TextField(blank=True,null=True)
    host = models.ManyToManyField('Host')


    def __unicode__(self):
        return  self.name


    class Meta:

        verbose_name = u'子系统'

        verbose_name_plural = u"子系统"
     
    def get_host(self):                                                                                                                 
        return ','.join([g.ip_addr for g in self.host.select_related()])

class App_host(models.Model):
    app_id = models.IntegerField(default=11)
    host_id = models.IntegerField(default=11)

class weblogic_admin_serverhost(models.Model):
    weblogic_admin_id = models.IntegerField(default=11)
    weblogic_server_id = models.IntegerField(default=11)

class App(models.Model):
    name = models.CharField(unique=True,max_length=64)
    package = models.CharField(max_length=30,null=True,blank=True)
    path = models.CharField(max_length=30,null=True,blank=True)
    memo = models.TextField(blank=True,null=True)
    subsys = models.ForeignKey(Subsys)
    host = models.ManyToManyField(Host)
    
    def __unicode__(self):
    
        return  self.name
    
    
    class Meta:
    
        verbose_name = u'应用'
    
        verbose_name_plural = u"应用"
    
    def get_subsys(self):
       return self.subsys.name
    
    #def get_host(self):
    #    return ','.join([g.ip_addr for g in self.host.select_related()])

class weblogic_admin(models.Model):
    primary = models.ForeignKey(Host)
    middleware = models.ForeignKey(middleware)
    username = models.ForeignKey(app_user)
    console_port = models.IntegerField(verbose_name = "控制台端口", null=True,blank=True)
    cluster = models.CharField(verbose_name = "集群名",max_length=30,null=True,blank=True)
    create_date = models.DateTimeField(verbose_name = "安装时间", null=True,blank=True)
    name = models.CharField(verbose_name = "系统名称", null=True,max_length=200,blank=True)
    servername = models.CharField(verbose_name = "实例名", default="AdminServer",null=True,max_length=200,blank=True)
    server_status = models.CharField(verbose_name = "状态", max_length=20,null=True,blank=True)
    admin_status = models.CharField(verbose_name = "状态", max_length=20,null=True,blank=True)
    date = models.DateTimeField(verbose_name = "修改时间", null=True,blank=True)
    serverhost = models.ManyToManyField('weblogic_server')

    def __unicode__(self):
        return  self.name
    
    class Meta:
        managed = True
        verbose_name = "weblogic控制台部署信息"
        verbose_name_plural = "weblogic控制台部署信息"

    def get_host(self):                                                                                                             
        return ','.join([g.managed_server_id.ip_addr for g in self.serverhost.select_related()])

class weblogic_server(models.Model):
        managed_server_id = models.ForeignKey(Host)
        #type = models.ForeignKey(middleware)
        apps_id = models.ForeignKey(App)
        server_name = models.CharField(verbose_name = "实例名", max_length=50,null=True,blank=True)
        server_port = models.IntegerField(verbose_name = "实例端口", null=True,blank=True)
        server_status = models.CharField(verbose_name = "状态", max_length=20,null=True,blank=True)
        date = models.DateTimeField(verbose_name = "修改时间", null=True,blank=True)
        def __unicode__(self):
            return  self.server_name


        class Meta:
        	managed = True
        	verbose_name = "weblogic实例部署信息"
        	verbose_name_plural = "weblogic实例部署信息"
        
        def get_app(self):
            return self.apps_id.name
        

        def get_managed_server(self):
            return self.managed_server_id.ip_addr

class java_test(models.Model):
      server_name = models.CharField(verbose_name = "工程名", max_length=50,null=True,blank=True)
      #app = models.ForeignKey(App)
      def __unicode__(self):
            return  self.server_name

class fuck(models.Model):
      name = models.CharField(verbose_name = "工程名", max_length=50,null=True,blank=True)
      #app = models.ForeignKey(App)
      def __unicode__(self):
            return  self.server_name

class java_process(models.Model):
      name = models.CharField(verbose_name = "名称",max_length=50,null=True,blank=True)
      pid = models.IntegerField(verbose_name = "进程ID", null=True,blank=True)
      path = models.CharField(verbose_name = "部署路径", max_length=50,null=True,blank=True)
      port = models.IntegerField(verbose_name = "端口", null=True,blank=True)
      host = models.ForeignKey(Host)
      cpu = models.CharField(verbose_name = "cpu", max_length=50,null=True,blank=True)
      date = models.DateTimeField(verbose_name = "时间", null=True,blank=True)
      status = models.CharField(verbose_name = "状态", max_length=50,null=True,blank=True)
      
      def __unicode__(self):
            return  self.name
      class Meta:
        managed = True
        verbose_name = "java部署信息"
        verbose_name_plural = "java部署信息"

class java_server(models.Model):
       name = models.CharField(verbose_name = "名称", max_length=50,null=True,blank=True)
       app = models.ForeignKey(App)      
       process = models.ManyToManyField(java_process)
       status = models.CharField(verbose_name = "状态", max_length=50,null=True,blank=True)
       def __unicode__(self):
            return  self.name

       class Meta:
        managed = True
        verbose_name = "java后台进程"
        verbose_name_plural = "java后台进程"

       def get_subsys(self):                                                                                           
            return self.app.subsys.name

       def get_process_ip(self):
            return ','.join([g.host.ip_addr for g in self.process.select_related()])
       def get_process_path(self):
            return ','.join([g.path for g in self.process.select_related()])

class web_server(models.Model):
      name = models.CharField(verbose_name = "实例名", max_length=50,null=True,blank=True)
      type = models.ForeignKey(middleware)
      project = models.CharField(verbose_name = "部署单元",max_length=50,null=True,blank=True)
      path = models.CharField(verbose_name = "部署路径",max_length=50,null=True,blank=True)
      host = models.ForeignKey(Host)
      date = models.DateTimeField(verbose_name = "时间", null=True,blank=True)
      status = models.CharField(verbose_name = "状态", max_length=50,null=True,blank=True)

class zk_server(models.Model):
      name = models.CharField(verbose_name = "实例名", max_length=50,null=True,blank=True)
      type = models.ForeignKey(middleware)
      project = models.CharField(verbose_name = "部署单元",max_length=50,null=True,blank=True)
      path = models.CharField(verbose_name = "部署路径",max_length=50,null=True,blank=True)
      host = models.ForeignKey(Host)
      date = models.DateTimeField(verbose_name = "时间", null=True,blank=True)
      status = models.CharField(verbose_name = "状态", max_length=50,null=True,blank=True)


class Platform(models.Model):
    server = models.OneToOneField('Host')
    name = models.TextField(null=True)
    release = models.TextField(null=True)
    version = models.TextField(null=True)
    machine = models.TextField(null=True)
    cpu = models.IntegerField(null=True)
    memory = models.IntegerField(null=True)
    swap = models.IntegerField(null=True)
