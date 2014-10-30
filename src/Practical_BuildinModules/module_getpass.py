__author__ = 'wenychan'

# File:getpass-example-1.py
import getpass
usr = getpass.getuser()
pwd = getpass.getpass("enter password for user %s: " % usr)
print usr, pwd