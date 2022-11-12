import socket
import os
def sendfile(s):
	str1 = s.recv(1024)
	filename = str1.decode('utf-8')
	print('The server requests my file:',filename)

	if os.path.exists(filename):
		print ('Hello,I have %s,begin to upload!' % filename)
		s.send(b'yes')
		s.recv(1024)
		size = 1024
		with open(filename,'rb') as f:
			while True:
				data = f.read(size)
				s.send(data)
				if len(data) < 1024:
					break
		print('%s upload successfully!' % filename)

	else:
		print('Sorry,I have no %s' % filename)
		s.send(b'no')
		

s = socket.socket()
s.connect(('127.0.0.1',2222))
while True:
	sendfile(s)
	

