from socket import socket

def mainRun():
    host = '127.0.0.1'
    port = 5000
    server = socket()
    server.bind((host,port))
    server.listen(1)
    print('Wait connected Cliend')
    cliend,addr = server.accept()
    print("Connect from :",addr)
    while True:
        data = cliend.recv(1024).decode('utf-8')
        if not data:
            break
        print('Message is ',data)
        data = str(data.upper())
        cliend.send(data.encode('utf-8'))
    cliend.close()

if __name__ == "__main__":
    mainRun()