DecryptMode = 2

while DecryptMode == 2:
    print("Welcome to the xor decryptor!")
    print("Enter 'encrypt' to encrypt a number via xor")
    print("Enter 'decrypt' to decrypt a number encrypted via xor")
    DecryptMode = input(": ")

    if DecryptMode == "encrypt":
        DecryptMode = 0
    elif DecryptMode == "decrypt":
        DecryptMode = 1
    else:
        DecryptMode = 2
        print("Please enter a valid input")

while DecryptMode == 0:
    try:
        plaintext = str(input("Enter plaintext: "))
        key = str(input("Enter key: "))
        code = [0, 0, 0, 0, 0, 0, 0, 0]
    except ValueError:
        continue
    try:
        if plaintext[0] != key[0]:
            code[0] = "1"
        else:
            code[0] = "0"

        if plaintext[1] != key[1]:
            code[1] = "1"
        else:
            code[1] = "0"

        if plaintext[2] != key[2]:
            code[2] = "1"
        else:
            code[2] = "0"

        if plaintext[3] != key[3]:
            code[3] = "1"
        else:
            code[3] = "0"

        if plaintext[4] != key[4]:
            code[4] = "1"
        else:
            code[4] = "0"

        if plaintext[5] != key[5]:
            code[5] = "1"
        else:
            code[5] = "0"

        if plaintext[6] != key[6]:
            code[6] = "1"
        else:
            code[6] = "0"

        if plaintext[7] != key[7]:
            code[7] = "1"
        else:
            code[7] = "0"
    except(TypeError, ValueError):
        print("Didn't work, try again")
        continue
    print("".join(code))
    DecryptMode = 2
    continue

while DecryptMode == 1:
    try:
        encrypt = str(input("Enter encrypted message: "))
        key = str(input("Enter key: "))
        code = [0, 0, 0, 0, 0, 0, 0, 0]
    except ValueError:
        continue
    try:
        if encrypt[0] != key[0]:
            code[0] = "1"
        else:
            code[0] = "0"

        if encrypt[1] != key[1]:
            code[1] = "1"
        else:
            code[1] = "0"

        if encrypt[2] != key[2]:
            code[2] = "1"
        else:
            code[2] = "0"

        if encrypt[3] != key[3]:
            code[3] = "1"
        else:
            code[3] = "0"

        if encrypt[4] != key[4]:
            code[4] = "1"
        else:
            code[4] = "0"

        if encrypt[5] != key[5]:
            code[5] = "1"
        else:
            code[5] = "0"

        if encrypt[6] != key[6]:
            code[6] = "1"
        else:
            code[6] = "0"

        if encrypt[7] != key[7]:
            code[7] = "1"
        else:
            code[7] = "0"
    except(ValueError, TypeError):
        print("Didn't work, try again")
        continue
    print("".join(code))
    DecryptMode = 2
