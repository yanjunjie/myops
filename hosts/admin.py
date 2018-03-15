from django.contrib import admin

import auth_admin
# Register your models here.
import models

class HostAdmin(admin.ModelAdmin):
    list_editable = ('hostname','ip_addr')
    list_display = ('hostname','ip_addr','port','idc','system_type','enabled','date')
    search_fields = ('hostname','ip_addr')
    list_filter = ('idc','system_type')
class HostUserAdmin(admin.ModelAdmin):
    list_display = ('auth_type','username','password')

class BindHostToUserAdmin(admin.ModelAdmin):
    list_display = ('host','host_user','get_groups')
    filter_horizontal = ('host_groups',)
class SubsysAdmin(admin.ModelAdmin):
    list_display = ('name','memo','get_host')

class AppAdmin(admin.ModelAdmin):
    list_display = ('name','memo','package','path','get_subsys')
class weblogicAdmin(admin.ModelAdmin):
    list_display = ('name','primary','middleware','username','console_port','cluster','create_date','get_host')
class weblogicServerAdmin(admin.ModelAdmin):
    list_display = ('server_name','server_port','get_app','get_managed_server','server_status','date')
class middlewareAdmin(admin.ModelAdmin):
    list_display = ('name','version')
class app_userAdmin(admin.ModelAdmin):
    list_display = ('username','password','get_middleware')

class java_severAdmin(admin.ModelAdmin):
    list_display = ('name','app','get_subsys','get_process_path','get_process_ip','status')

class java_processAdmin(admin.ModelAdmin):
    list_display = ('name','pid','path','port','host','cpu','date','status')

class web_serverAdmin(admin.ModelAdmin):
    list_display = ('name','type','project','path','host','date','status')

class zk_serverAdmin(admin.ModelAdmin):
    list_display = ('name','type','project','path','host','date','status')

class platformAdmin(admin.ModelAdmin):
    list_display = ('name','name','version','machine','cpu','memory','swap')

admin.site.register(models.UserProfile,auth_admin.UserProfileAdmin)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.HostGroup)
admin.site.register(models.HostUser,HostUserAdmin)
admin.site.register(models.BindHostToUser,BindHostToUserAdmin)
admin.site.register(models.IDC)
admin.site.register(models.Subsys,SubsysAdmin)
admin.site.register(models.App,AppAdmin)
admin.site.register(models.weblogic_admin,weblogicAdmin)
admin.site.register(models.weblogic_server,weblogicServerAdmin)
admin.site.register(models.middleware,middlewareAdmin)
admin.site.register(models.app_user,app_userAdmin)
admin.site.register(models.java_server,java_severAdmin)
admin.site.register(models.java_process,java_processAdmin)
admin.site.register(models.web_server,web_serverAdmin)
admin.site.register(models.zk_server,zk_serverAdmin)
admin.site.register(models.Platform,platformAdmin)
