if __name__ == '__main__':  
    import socket  
    import threading
    import time
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8001))
    print('Connect to the server!')

    def Speak():
        while True:
            msg=input()
            sock.send(msg.encode('utf-8'))
            time.sleep(0.1)
            
    
    def Hear():
        while True:
            str = sock.recv(1024)
            print(str.decode("utf-8"))
            time.sleep(0.2)
    
    threading.Thread(target=Speak).start()
    threading.Thread(target=Hear).start()

'''   
while True:  
    msg=input('msg: ')
    sock.send(msg.encode('utf-8'))
    str = sock.recv(1024)
    print(str.decode("utf-8"))

#sock.close()  
'''