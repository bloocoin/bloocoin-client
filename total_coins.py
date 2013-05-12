from server_data import ip, port
import json
import socket

def total_coins():
    data = json.dumps({"cmd":"total_coins"})
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect((ip, port))
    except:
        return "Server is down"
    s.send(data)
    data = json.loads(s.recv(1024))
    if data['success']:
        return data['payload']['amount']
    else:
        return "Error"
