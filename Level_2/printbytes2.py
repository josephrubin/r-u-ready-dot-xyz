def main():
    st1 = getStr("corrupted_packet_capture")
    print(st1)

def getHex(i, string):
    fst = string[i * 2]
    if fst == "":
        fst = "0"
    print("fst\n")
    scd = string[i * 2 + 1]
    if scd == "":
        scd = "0"
    return fst + scd

def getStr(name):
    exp = open(name, "rb")
    dump = exp.read()

    st = ""
    for i, char in enumerate(dump):
        st += toStr(char, 16, True) + " "
    return st

def toStr(n, base, fst):
    convertString = "0123456789ABCDEF"
    if n < base:
        if fst:
           return "0" + convertString[n]
        else:
            return convertString[n]
    else:
        return toStr(n//base,base,False) + convertString[n%base]

main()
