csv = open("auths.txt", "r")

clients = []
servers = []

for line in csv:
    split = line.split(",")
    clients.append(split[0])
    servers.append(split[1])

hexes = {}
for client in clients:
    for i in range(0, len(client), 2):
        hx = client[i] + client[i + 1]
        if hx in hexes:
            hexes[hx] += 1
        else:
            hexes[hx] = 1

print("ALL")
print(str(hexes) + "\n")

print("MORE THAN ONE")
many = []
for hx in hexes:
    if hexes[hx] > 1:
        print(hx + ": " + str(hexes[hx]) + ", ")
        many.append(hx)

haxes = {}
for server in servers:
    for i in range(0, len(server) - 1, 2):
        hx = server[i] + server[i + 1]
        if hx in haxes:
            haxes[hx] += 1
        else:
            haxes[hx] = 1

print("MORE THAN ONE")
many = []
for hx in haxes:
    if haxes[hx] > 1:
        print(hx + ": " + str(haxes[hx]) + ", ")
        many.append(hx)
