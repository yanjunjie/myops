#!/usr/bin/env python
#coding=utf-8 
import sys
import argparse
import urllib2
import json
from login import *
#定义更新action函数
def mediatypeupdate(mediatypeid,status,auth):
    values = {'jsonrpc': '2.0',
              'method': 'mediatype.update',
              'params': {
                  "mediatypeid": mediatypeid,
                  "status": status
              },
              'auth': auth,
              'id': '1'
              }
    output = requestJson(url,values)
#定义读取状态函数
def triggerget(auth):
    values = {'jsonrpc': '2.0',
           "method":"trigger.get",
               "params": {
                        "output": [
                        "triggerid",
                        "description",
                        "priority"
                        ],
              "filter": {
                         "value": 1
                         },
              "expandData":"hostname",
              "sortfield": "priority",
              "sortorder": "DESC"
            },
              'auth': auth,
              'id': '2'
              }
    output = requestJson(url,values)
    return output

#定义通过ip获取主机id的函数
def ipgetHostsid(ip,url,auth):
    values = {'jsonrpc': '2.0',
              'method': 'host.get',
              'params': {
                  'output': [ "host" ], 
                  'filter': {
                      'ip': ip
                  },
              },
              'auth': auth,
              'id': '3'
              }
    output = requestJson(url,values)
    return output

#定义通过主机id获取开启关闭监控函数
def idupdatehost(status,hostid,url,auth):
    values = {'jsonrpc': '2.0',
              'method': 'host.update',
              'params': {
                  "hostid": hostid, 
                  "status": status
              },
              'auth': auth,
              'id': '4'
              }
    output = requestJson(url,values)
    return output
#定义通过项目hostid获取itemid函数
def getHostsitemsid(hostid,itemsname,url,auth):
    values = {'jsonrpc': '2.0',
              'method': "item.get",
              "params": {
                    "output": ["itemids"],
                    "hostids": hostid,
            "filter":{
                    "key_": itemsname,
                },
                },

              'auth': auth,
              'id': '5'
              }
    output = requestJson(url,values)
    if len(output)==0:
        return output
    else:
        return output[0]['itemid']


#定义通过项目id获取监控项目最近值信息的函数
def getHostsitemsvalue(itemid,url,auth):
    values = {'jsonrpc': '2.0',
              'method': "history.get",
              "params": {
                    "output": "extend",
                    "history":3,
                    "itemids":itemid,
                    "sortfield": "clock",
                    "sortorder": "DESC",
                    "limit":1,
                },

              'auth': auth,
              'id': '6'
              }
    output = requestJson(url,values)
    if len(output)==0:
        return output
    else:
        return output[0]["value"]

#定义更新读取状态action函数
def mediatypeget(mediatypeid,auth):
    values = {'jsonrpc': '2.0',
              'method': 'mediatype.get',
              'params': {
                "output": "extend",

              "filter": {
                        "mediatypeid":mediatypeid,
                         },
              },

              'auth': auth,
              'id': '7'
              }
    output = requestJson(url,values)
    if len(output)==0:
        return output
    else:
        return output[0]['status']


#定义maintenance维修模式host函数
def maintenancecreate(maintenancename,active_since,active_till,hostid,auth):
    values = {'jsonrpc': '2.0',
              'method': 'maintenance.create',
              'params': {
              "name": maintenancename,
              "active_since": active_since,
              "active_till": active_till,
              "hostids": [
                    hostid
                ],
                "timeperiods": [
                            {
                "timeperiod_type": 0,
                "every": 1,
                "dayofweek": 64,
                "start_time": 64800,
                "period": 3600
                            }
                                ]
              },
              'auth': auth,
              'id': '8'
              }
    output = requestJson(url,values)

#定义通过模糊获取关闭主机信息函数
def disabledhostget(url,auth):
    values = {'jsonrpc': '2.0',
              'method': 'host.get',
            "params": {
                "output": ["host"],
                'selectInterfaces': [ "ip" ],
                "filter": {
                    "status":1
        }
    },
              'auth': auth,
              'id': '9'
              }
    output = requestJson(url,values)
    return output

#定义maintenance维修模式group函数
def maintenancecreategroup(maintenancename,active_since,active_till,groupid,auth):
    values = {'jsonrpc': '2.0',
              'method': 'maintenance.create',
              'params': {
              "name": maintenancename,
              "active_since": active_since,
              "active_till": active_till,
              "groupids": [
                    groupid
                ],
                "timeperiods": [
                            {
                "timeperiod_type": 0,
                "every": 1,
                "dayofweek": 64,
                "start_time": 64800,
                "period": 3600
                            }
                                ]
              },
              'auth': auth,
              'id': '10'
              }
    output = requestJson(url,values)

#定义通过host groups named 获取groupid
def groupnameGroupid(groupname,auth):
    values = {'jsonrpc': '2.0',
              'method': 'hostgroup.get',
              "params": {
                    "output": "extend",
                    "filter": {
                        "name": [
                            groupname
                        ]
                    }
                },
              'auth': auth,
              'id': '11'
              }
    output = requestJson(url,values)
    return output

#定义模糊查询维护主机
def maintenanceget(url,auth):
    values = {'jsonrpc': '2.0',
              'method': 'maintenance.get',
              "params": {
                    "output": "extend",
                },
              'auth': auth,
              'id': '12'
              }
    output = requestJson(url,values)
    return output

#定义批量恢复处于维护主机
def maintenancedelete(maintenanceid,url,auth):
    values = {'jsonrpc': '2.0',
              'method': 'maintenance.delete',
              "params": [
                    maintenanceid
                ],
              'auth': auth,
              'id': '13'
              }
    output = requestJson(url,values)
    return output

#定义通过hostid获取graphid的函数
def getgraphid(hostid,graphname,url,auth):
        values = {'jsonrpc': '2.0',
                          'method': 'graph.get',
                          'params': {
                                  "output": "name",
                                  "hostids": hostid,
                                  "sortfield": "name",
                          'filter': {
                                        "name": graphname
                                  },

                          },
                          'auth': auth,
                          'id': '14'
                          }
        output = requestJson(url,values)
        return output

