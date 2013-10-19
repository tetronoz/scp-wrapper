#!/usr/bin/python
 
import sys
import os
import pwd
from subprocess import call, Popen, PIPE
import re
 
def fail(msg):
    """(str) -> str Prints error message to STDOUT
    >>> fail('Error')
    Error
    >>> fail('Wrong argument')
    Wrong argument
    """
    
    print msg
    sys.exit(1)
 
def access_verify(user, dirto):
    """(str) -> Boolean Returns TRUE iff user is allowed to scp
    """
  
    if user in users:
        for d in users[user]:
            print user, dirto[-1:],  d.rstrip()[-1:], dirto[:-1] == d.rstrip(), dirto == d[:-1].rstrip()
            if dirto == d.rstrip():
                return True
            elif (dirto[-1:] == "/" or d.rstrip()[-1:] == "/") and (dirto[:-1] == d.rstrip() or dirto == d.rstrip()[:-1]):
                return True
            else:
                return False
    return False
 
if __name__ == '__main__':
 
    users = {}
    conf = "/usr/local/etc/scponly.conf"
 
    # Reading configuration file
 
    fp = open(conf, "r")
    for line in fp.readlines():
        record = line.split("=")
        users[record[0]] = record[1].split(":")
    fp.close()
  
    command = sys.argv[2]
    scp_args = command.split()
 
    if scp_args[0] != "scp":
        msg = "Only scp is allowed"
        fail(msg)
 
    if scp_args[1] != "-t" and not "-f" and not "-v":
        msg = "Restricted; only server mode is allowed"
        fail(msg)
 
    destdir = scp_args[-1]
   if not os.path.isfile(destdir) or os.path.isfile(destdir):
        destdirv = os.path.dirname(destdir)
    else:
        destdirv = destdir
    uname = pwd.getpwuid(os.getuid())[0]
    if not access_verify(uname, destdirv):
        msg = "User " + uname + " is not authorized to scp to this host."
        fail(msg)
    else:
        scp_args.pop(0)
        if len(scp_args) == 2:
            call(["/usr/bin/scp", scp_args[0], destdir])
        elif len(scp_args) == 3:
            call(["/usr/bin/scp", scp_args[0], scp_args[1], destdir])