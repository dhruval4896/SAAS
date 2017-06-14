#!/usr/bin/python
import os,time,getpass,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

data=s.recvfrom(100)
data1=s.recvfrom(100)
 
if data[0]=='test' and data1[0]=='123' :
	s.sendto("ok",data[1])
else:
	exit()
