import socket
import json
from server_data import ip, port

def send(amount, to):
    with open("bloostamp", 'rb') as file:
        f = file.read().split(":")
        addr = f[0]
        key = f[1]
    s = socket.socket()
    s.connect((ip, port))
    s.send(json.dumps({"cmd":"send_coin", "to":to, "addr":addr, "pwd":key, "amount":amount}))
    data = s.recv(1024)
    if data:
        data = json.loads(data)
        if data['success']:
            return "Transaction Successful!"
        else:
            return data['message']
