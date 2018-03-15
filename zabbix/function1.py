#!/usr/bin/env python
#coding=utf-8 
import sys
import argparse
import urllib2
import json
from login import *

#定义通过ip获取主机id的函数
def ipgetHostsid(ip,url,auth):
    
    output = [{'host':'10.128.148.101','hostid':'10105'}]
    return output

#定义通过项目hostid获取itemid函数
def getHostsitemsid(hostid,itemsname,url,auth):
    
    output = [{'itemid':'25826'}]
    if len(output)==0:
        return output
    else:
        return output[0]['itemid']


#定义通过项目id获取监控项目最近值信息的函数
def getHostsitemsvalue(itemid,url,auth):
    output = [{'itemid':'25826','ns':'54554545','value':'1','clock':'155455455'}]
    if len(output)==0:
        return output
    else:
        return output[0]["value"]

