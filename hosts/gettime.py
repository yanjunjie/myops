import os.path, time

f = "/srv/salt/upload"
mtime = time.ctime(os.path.getmtime(f))
ctime = time.ctime(os.path.getctime(f))
print "Last modified : %s, last created time: %s" % (mtime, ctime)
