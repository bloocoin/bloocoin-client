import uuid
import socket
from hashlib import sha1
import random
import json

from server_data import ip, port


def register():
    addr = sha1(str(uuid.uuid1(random.randint(0, 100000000000000)))).hexdigest()
    key = sha1(str(uuid.uuid1(random.randint(0, 100000000000000)))).hexdigest()
    if submit(addr, key):
        print "Registration Success! Your BlooCoin Address is: ", addr
    else:
        print "Registration Failed"


def submit(addr, key):
    reg = socket.socket()
    reg.connect((ip, port))
    reg.send(json.dumps({"cmd": "register", "addr": addr, "pwd": key}))
    data = reg.recv(1024)
    if data:
        try:
            data = json.loads(data)
            print data
        except Exception, error:
            print error
            return False

        if data[u'success']:
            with open("bloostamp", 'wb') as file:
                file.write(addr+":"+key)
            return True
    else:
        return False
