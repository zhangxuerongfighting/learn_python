import socket
import os

s = socket.socket()
s.bind(('127.0.0.1',2222))
s.listen(2)
print('waiting for the connecting...')
(conn,addr) = s.accept()
filename = "C:/cc.txt"
print('I want to get the file %s' % filename)

s.send(filename.encode('utf-8'))
str1 = s.recv(1024)
str2 = str1.decode('utf-8')

if  str2 =='no':
    print('Does not the file %s' % filename)
else:
    s.send(b'I an ready!')
    temp = filename.split('/')
    myname = 'my_' + temp[len(temp)-1]
    size = 1024
    with open(myname,'wb') as f:
        while True:
            data = s.recv(data)
            f.write(data)
            if len(data) < 1024:
                break
print('The upload file is %s' % myname)
s.close()
