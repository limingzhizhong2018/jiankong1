import  socket

host =''
port = 11111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print("Server running on port %d"  %port)

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw')
    clientfile.write("welcome," + str(clientaddr) + '\n')
    clientfile.write("please enter string:")
    line = clientfile.readline().strip()
    clientfile.write("your enter work len:" +str(len(line)) )
    clientfile.close()
    clientsock.close()
