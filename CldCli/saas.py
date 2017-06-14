#!/usr/bin/python
import os,time,socket

os.system('clear')

print "Welcome to SAAS Menu:"
print "\t\t1. FireFox"
print "\t\t2. GEdit"
print "\t\t3. VLC"
print "\t\t4. Calculator "
print "\t\t5. Office"
print "\t\t6. ScreenShot"
print "\t\t7. WebCam"


ch=raw_input("Enter Your Choice:")

if ch=='1' :
	print "Please Wait A Second: "
	execfile('firefox.py')

elif ch=='2' :
	print "Please Wait A Second: "
	execfile('gedit.py')
	
elif ch=='3' :
	print "Please Wait A Second: "
	execfile('vlc.py')
elif ch=='4' :
	print "Please Wait A Second: "
	execfile('calculator.py')
elif ch=='5' :
	print "Please Wait A Second: "
	execfile('office.py')

elif ch=='6' :
	print "Please Wait A Second: "
	execfile('screenshot.py')

elif ch=='7' :
	print "Please Wait A Second: "
	execfile('webcam.py')
else :

	print "Wrong Choice. Please Re-enter your Choice"
	time.sleep(3)
	os.system('clear')	
	execfile('saas.py') 

