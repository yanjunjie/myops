#!/usr/bin/env python
#coding=utf-8
import urllib2
import sys
import json
import argparse
from login import *
from function1 import *
#登陆zabbix获取auth
itemsname='java.mon.port[8000]'
auth = authenticate(url, username, password)
#状态0是启用监控，1是禁用监控
status=1
#定义操作ip
hostip='192.168.1.100'
#通过hostip获取zabbix hostid
hostids=ipgetHostsid(hostip,url,auth)
print hostids
hostid=hostids[0]['hostid']
print hostid
itemid = getHostsitemsid(hostid,itemsname,url,auth)
print itemid
value = getHostsitemsvalue(itemid,url,auth)
print value

