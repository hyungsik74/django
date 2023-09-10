import socket
  
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('hyungsik74.github.io', 80))
cmd = 'GET http://hyungsik74.github.io/django/ch01/page01.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()