auth = open("auths.txt", "r")

def dec(hx):
    return str(int(hx, 16))

clients = []
servers = []

for line in auth:
    split = line.split(",")
    clients.append(split[0])
    servers.append(split[1])

hexmap = {}
for i in range(len(clients)):
    cl = clients[i]
    sv = servers[i]
    for i in range(0, len(cl), 2):
        hx = cl[i] + cl[i + 1]
        hx2 = sv[i*2] + sv[i*2+1]
        hx3 = sv[i*2+2] + sv[i*2+3]

        hx = dec(hx)
        hx2 = dec(hx2)
        hx3 = dec(hx3)
        
        if not (hx in hexmap):
            hexmap[hx] = hx2 + ", " + hx3
        else:
            hexmap[hx] += " | " + hx2 + ", " + hx3

for key in hexmap:
    print(key + ": " + hexmap[key])
