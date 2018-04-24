def main():
    st1 = getStr("corrupted_packet_capture")
    st2 = getStr("repaired.pcap")

    print("ORIGINAL\n" + st1 + "\n\n")
    print("REPAIRED\n" + st2)

def getHex(i, string):
    fst = string[i * 2]
    if fst == "":
        fst = "0"
    scd = string[i * 2 + 1]
    if scd == "":
        scd = "0"
    return fst + scd

def getStr(name):
    exp = open(name, "rb")
    dump = exp.read()

    st = ""
    for i, char in enumerate(dump):
        st += toStr(char, 16) + " "
        if i == 30:
            st += " | "
    return st

def toStr(n, base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

main()
