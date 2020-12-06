import socket
import time

HOST='localhost'
PORT=10001

def transfile_client():  
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True :
        cmd=input('input > ')
        act=cmd.split()

        if act[0]=='exit':
            break
        elif act[0]=='ls':
            s.sendall(cmd.encode())
            data=s.recv(1024)
            if not data :
                break
            else:
                print(data.decode('gbk'))
        elif act[0]=='put':
            s.sendall(cmd.encode())
            msg=s.recv(1024)
            print(msg.decode())
            if msg.decode()=='ok':
                with open('clientfile/'+act[1],'rb') as f:
                    while True :
                        data=f.read(1024)
                        if not data:
                            break
                        s.send(data)
                    time.sleep(1)
                    s.send('EOF'.encode())
            
        elif act[0]=='get':
            s.sendall(cmd.encode())
            msg=s.recv(1024)
            print(msg.decode())
            if msg.decode()=='ok':
                with open('clientfile/'+act[1],'wb') as f:
                    while True:
                        msg = s.recv(1024)
                        if msg == b'EOF':
                            print( 'recv file success!')
                            break
                        f.write(msg)
        else:
            print('invalid input')

    s.close

if __name__=='__main__' :
    transfile_client()