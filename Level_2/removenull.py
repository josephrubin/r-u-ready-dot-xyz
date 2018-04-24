import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

exp = open("bytes_export.bin", "rb")
dump = exp.read()

st = ""
print("ONLY ALPHABETIC\n--->--->---\n")
for char in dump:
    if chr(char) in alphabet:
            st += (chr(char))
print(st)
alphabetic = open("alphabetic.bin", "w")
alphabetic.write(st)
alphabetic.close()

st = ""
print("\nONLY ALPHA\n--->--->---\n")
for char in dump:
    if chr(char).isalpha():
            st += (chr(char))
print(st)
alpha = open("alpha.bin", "w")
alpha.write(st)
alpha.close()

print("\nONLY PRINTABLE\n--->--->---\n")
for char in dump:
    if chr(char) in string.printable:
            st += (chr(char))
print(st)
printable = open("alpha.bin", "w")
printable.write(st)
printable.close()

exp.close()
