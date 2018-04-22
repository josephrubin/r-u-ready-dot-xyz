import chardet
cook="5040d7818df44bac8fbf75eb8f31e55c"
byte = cook.encode()
the_encoding = chardet.detect(byte)
print(the_encoding)
