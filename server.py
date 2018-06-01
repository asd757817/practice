print('server start...')
if __name__ == '__main__':  
    import socket
    import threading
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8001))  
    sock.listen(5)
    client=[]
    for i in range(500):
        client.append(0)
    
    ClientAddr={}
    
    def ClientConnect(connection):
        No_client=0       
        for i in range(1,500):
            if client[i]==0:
                No_client=i
                client[i]=1
                ClientAddr[i]=connection
                print('client %d connet!'%(i))
                break
        while True:
            try:
                connection.settimeout(600)
                buf = connection.recv(1024)
                print(buf.decode("utf-8"))
                s1="Client %d : "%(No_client)
                s=s1+buf.decode("utf-8")                
                for i in range(1,500):
                    if client[i]==1 and i!=No_client:
                        ClientAddr[i].send(s.encode("utf-8"))
            except socket.timeout:
                print('Time is out')
        connection.close()


    while True:
        connect,address=sock.accept()
        threading.Thread(target=ClientConnect,args=[connect]).start()
        

'''
    while True:  
        connection,address = sock.accept()
        
        while True:
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                print(buf.decode("utf-8"))
                s = "I got you!"
                connection.send(s.encode('utf-8'))
            except socket.timeout:
                print('Time is out')
        #connection.close()
'''