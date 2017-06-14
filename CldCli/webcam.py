#!/usr/bin/python
import os,time,socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

S_IP="192.168.122.66"
S_PORT=8888

os.system('sshpass -p "qw" ssh -X root@'+ S_IP +' cheese')

execfile('saas.py')

