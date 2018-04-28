auth = open("auths.txt", "r")

clients = []
servers = []

for line in auth:
    split = line.split(",")
    clients.append(split[0])
    servers.append(split[1])

for i in range(len(clients)):
    hexes = []
    cl = clients[i]
    for i in range(0, len(cl), 2):
        hx = cl[i] + cl[i + 1]
        hexes.append(hx)
    tot = 1
    for hx1 in hexes:
        tot *= int(hx1, 16)
    print("TOT OF: " + cl)
    print(hex(tot) + "\n")
