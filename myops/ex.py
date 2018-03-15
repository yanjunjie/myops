#!/usr/bin/python

from api import *
#print SALTAPI.salt_mod('monitor','cp.get_file',['salt://upload/logo.png','/tmp/logo.png'])
print SALTAPI.salt_mod('monitor','cmd.run',['uptime'])

