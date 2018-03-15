import paramiko,os
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'saltweb.conf'))
Local_Dir = os.path.join(BASE_DIR,'upload')

#saltstack_ip = '192.168.91.132'
#saltstack_username = 'root'
#saltstack_password = 'rootroot'

class SSH(object):
	def __init__(self,ip,port,username,password):
		self.ip = ip
		self.port = port
		self.username = username
		self.password = password
		
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(self.ip,self.port,self.username,self.password,timeout=20000)

	def exec_command(self,command):
		try:
			stdin,stdout,stderr = self.ssh.exec_command(command)
			return stdout.read()
		except Exception as e:
			return e
		else:
			self.ssh.close()
		
	def exec_command_list(self,command):
		'''return list'''
		try:
                	stdin,stdout,stderr = self.ssh.exec_command(command)
                	return stdout.readlines()
                except Exception as e:
                        return e
                else:
                        self.ssh.close()

	def send_file(self,local,remote):
		try:
			self.sftp.put(local,remote)
			return "send %s to %s success!" %(local,remote)
		except Exception as e:
			return "send %s to %s failed,%s" %(local,remote,e)
		else:
			self.t.close()

#s = SSH(saltstack_ip,22,saltstack_username,saltstack_password)
