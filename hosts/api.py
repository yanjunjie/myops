import os
import hashlib
import random
import datetime
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'saltweb.conf'))


SALT_URL = config.get('salt-api', 'salt_url')
SALT_USERNAME = config.get('salt-api', 'salt_username') 
SALT_PASSWORD = config.get('salt-api','salt_password')



class SaltApi(object):
	__token = ''

	def __init__(self,url,username,password):
		self.__url = url
		self.__username = username
		self.__password = password

	def get_token(self):
		''' user login and get token id'''
		params = {'eauth' : 'pam', 'username' : self.__username, 'password' : self.__password}
		headers = {'Accept' : 'application/json'}
		args = urllib.urlencode(params)
		url = self.__url.rstrip('/')+'/login'
		req = urllib2.Request(url,args,headers)
		response = urllib2.urlopen(req).read()
		ret = json.loads(response)
		self.__token = ret['return'][0]['token'] 
	
	def postRequest(self,params,*args):
		url = self.__url.rstrip('/')
		headers = {'X-Auth-Token' : self.__token, 'Accept' : 'application/json'}
		if args:
			r_args = urllib.urlencode(params)+'&'+urllib.urlencode({'arg':args[0]},doseq=True)
		else:
			r_args = urllib.urlencode(params)
		req = urllib2.Request(url,r_args,headers)
		response = urllib2.urlopen(req).read()
		return json.loads(response)
		
		
	def list_all_key(self):
		self.get_token()
		params = {'client' : 'wheel' , 'fun': 'key.list_all'}
		ret = self.postRequest(params)
		return ret

	def delete_key(self,key):
		self.get_token()
		params = {'client': 'wheel', 'fun': 'key.delete', 'match': key}
		ret = self.postRequest(params)
		return ret['return'][0]['data']['success']

	def accept_key(self,key):
		'''add saltstack key,return True'''
		self.get_token()
		params = {'client': 'wheel', 'fun': 'key.accept', 'match': key}
		ret = self.postRequest(params)
		return ret['return'][0]['data']['success']

	def lookup_jid(self,jid):
		self.get_token()
		params = {'client' : 'runner' , 'fun' : 'jobs.lookup_jid' , 'jid' : jid}
		ret = self.postRequest(params)
		return ret

	def salt_mod(self,key,mod_name,*args):
		self.get_token()
		params = {'client':'local', 'tgt':key, 'fun':mod_name, 'expr_form':'compound'}
		ret = self.postRequest(params,*args)
		return ret

SALTAPI = SaltApi(SALT_URL,SALT_USERNAME,SALT_PASSWORD)

