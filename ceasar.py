"""
Due to modularity, you can use this to encrypt and decrypt messages
"""
def encryptCaesar(str, n):
    res = ""
    for i in range(len(str)):
        if ((str[i]).isupper()):
            res += chr((ord(str[i]) + n - 65) % 26 + 65)
        elif ((str[i]).islower()):
            res += chr((ord(str[i]) + n - 97) % 26 + 97)
    return res      


def main():
    test = "PURPLE"
    output = encryptCaesar(test, 4)
    decrypt = (encryptCaesar(output, 22))
    print(decrypt)
    
if __name__ == "__main__":
    main()