import socket
import json
from server_data import ip, port


def check_addr(addr):
    s = socket.socket()
    try:
        s.settimeout(5)
        s.connect((ip, port))
    except:
        return "Could not connect to server"
    s.send(json.dumps({"cmd":"check_addr", "addr":addr}))
    data = s.recv(1024)
    if data:
        data = json.loads(data)
        return data['payload']['addr']+ " "+str(data['payload']['amount'])
    else:
        return "Error retrieving data"
