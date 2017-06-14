#!/usr/bin/python
import os,time,socket,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print "\nEnter Credentials: "

S_IP="192.168.122.66"
S_PORT=8888

u_name=raw_input("Username:- ")
#To get user name

u_passw=getpass.getpass("Password:- ")
#To get password

s.sendto(u_name,(S_IP,S_PORT))
s.sendto(u_passw,(S_IP,S_PORT))

resp=s.recvfrom(100)
if resp[0]=="ok":
	print "Connected To Server" 
	print "Wait For Some Time "
	time.sleep(2)
	execfile('saas.py')
else:
	print "Not Connected"
	
