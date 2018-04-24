within = open("withinpcap.txt", "r")
output = open("withinpcap.pcap", "wb")

bt = bytes(bytearray.fromhex(within.read()))
print(bt)

output.write(bytes(0b11001100))
