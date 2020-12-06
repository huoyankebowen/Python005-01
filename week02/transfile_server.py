import socket
import time
from pathlib import Path

HOST='localhost'
PORT=10001


def transfile_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    while True :
        conn,addr=s.accept()
        print(f'connect by {addr}')
        while True :
            cmd=conn.recv(1024)
            if not cmd :
                break
            act=cmd.decode().split()
            if act[0]=='ls':
                serverdir=Path()
                print(serverdir)
                serverdir=serverdir/'serverfile'
                echostr='\r\n'.join([str(dir.name) for dir in list(serverdir.glob('*'))])
                print(echostr)
                conn.sendall(echostr.encode())

            elif act[0]=='get':
                conn.send('ok'.encode())
                with open('serverfile/'+act[1],'rb') as f :
                    print('serverfile/'+act[1])
                    while True:
                        data = f.read(1024)
                        if not data:
                            break
                        conn.send(data)   
                    time.sleep(1)                 
                    conn.send('EOF'.encode())
                    print('send EOF')
            elif act[0]=='put':
                conn.send('ok'.encode())
                with open('serverfile/'+act[1],'wb') as f :
                    while True:
                        data = conn.recv(1024)
                        if data == b'EOF':
                            break
                        f.write(data)

            elif act[0]=='bye':
                break
            else :
                conn.send(b'invalid action')
        conn.close
    s.close




if __name__=='__main__':
    transfile_server()

