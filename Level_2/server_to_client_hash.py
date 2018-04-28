import sys
import hashlib
import subprocess
import socket
import struct
import time

def main():
    initlog()

def initlog():
    # Initial connect.
    nc = Netcat("35.204.90.89", 5555)

    # Get the server prompt.
    prompt = str(nc.read())[2:34]
    print("prompt: " + prompt)

    # Calculate response.
    input_md5_hash = prompt
    num = decrypt_md5(input_md5_hash) + 1
    resp = (encrypt_SHA512(str(num)))
    sys.stdout.write("resp: " + resp + "\n")

    # Send response.
    nc.write(resp)
    
    # Get server's authorization.
    server = str(nc.read())
    print(server)

    # Close connection.
    nc.close()
    print("Closed")

def converse(nc, st):
    nc.write(st + "\r\n")
    print(st)
    printserver(nc)

def writecommand(nc, st):
    nc.write(st + "\r\n")

def halfconverse(nc, st):
    nc.write(st + "\r\n")
    print(st)

def getserver(nc):
    sv = str(nc.read())
    return sv

def printserver(nc):
    sv = str(nc.read())
    print(sv)

def decrypt_md5(hsh):
    for i in range(100000):
        m = hashlib.md5()
        m.update(str(i).encode("utf-8"))
        testhsh = m.hexdigest()
        if hsh == testhsh:
            return i
    return False

def encrypt_SHA512(st):
    m = hashlib.new("SHA512")
    m.update(st.encode("utf-8"))
    return m.hexdigest()
 
class Netcat:
    # Credit: https://gist.github.com/leonjza/f35a7252babdf77c8421
    
    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        l_onoff = 1                                                                                                                                                           
        l_linger = 0                                                                                                                                                          
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))

    def read(self, length = 1024):
        """ Read 1024 bytes off the socket """
        return self.socket.recv(length)
    
    def write(self, data):
        self.socket.send(bytes(data, "utf-8"))
    
    def close(self):
        self.socket.close()

main()
