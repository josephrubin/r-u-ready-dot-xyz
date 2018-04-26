s = input("Give Hex String:\n")
hexcodes = [str(s[i:i + 2]) for i in range(0, len(s), 2)]
deccodes = [int(s[i:i + 2], 16) for i in range(0, len(s), 2)]
st = ""
for num in deccodes:
    st += str(num)
print("--->--->--->--->---")
print("INPUT [hex]")
print(s)
print("--->--->--->--->---")
print("CODES [hex]")
print(hexcodes)
print("--->--->--->--->---")
print("CODES [decimal]")
print(deccodes)
print("--->--->--->--->---")
print("OUTPUT [decimal]")
print(st)
