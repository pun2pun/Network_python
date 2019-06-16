import socket 

def mainRun():
    host = '127.0.0.1'
    port = 5000
    server = socket.socket()
    server.connect((host,port))
    data = (input("Write message :"))
    while data !='q':
        server.send(data.encode('utf-8'))
        data = server.recv(1024).decode('utf-8')
        print('Data from server :',data)
        data = (input("Write message :"))
    
    server.close()

if __name__ == "__main__":
    mainRun()