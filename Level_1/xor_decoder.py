def main():
    # Key is: Israel-is-70
    # Represent that in ASCII
    key = "010010010111001101110010011000010110010101101100001011010110100101110011001011010011011100110000"

    # Now we use XOR to decode the right BF code by repeating the key as much as necessary
    ciphertext = open('ciphertext_with_whitespace.txt', 'r')
    plaintext = []
    for line in ciphertext:
        for i, char in enumerate(line):
            plaintext.append(int(char, 2) ^ int(key[i % len(key)], 2))
    print(''.join(str(n) for n in plaintext))
main()
