import Morse
import Atbash

def openEncryptedMassage(fileName):
    fileMessage = open(fileName, "r")
    lines = fileMessage.readlines()
    fileMessage.close()
    return lines

def tofileDecrypted(func, fileName, code, key, message):
    decryptedMessage = open(fileName, "w")
    decryptedMessage.write(code)
    decryptedMessage.write(key)
    decryptedMessage.write(func(message))
    decryptedMessage.close()

def tofileEncrypted(func, fileName, code, key, message):
    encryptedMessage = open(fileName, "w+")
    encryptedMessage.write(code)
    encryptedMessage.write(key)
    encryptedMessage.write(func(message))
    encryptedMessage.close()

    
#Arrays with parameters
codeNames = ["1", "2", "morse", "morse code", "atbash", "atbash cipher"]
modeNames = ["1", "2", "encrypt", "decrypt"]
formats = ["1", "2", "text", "file"]
#In this block we are selecting encryption/decryption parameters
print("Select code:\n 1) Morse code\n 2) Atbash cipher")
codeName = str(input("Code name or number:\n")).lower()
while (codeName not in codeNames):
    print("Wrong code or number, please re-enter!\n")
    codeName = str(input("Code name or number:\n")).lower()
print("Select mode:\n 1) Encrypt\n 2) Decrypt")
mode = str(input("Enter mode name or number:\n")).lower()
while (mode not in modeNames):
    print("Wrong mode name or number, please re-enter!\n")
    mode = str(input("Mode name or number:\n")).lower()
print("Select format:\n 1) Text\n 2) File")
format = str(input("Format name or number:\n")).lower()
while (format not in formats):
    print("Wrong format name or number, please re-enter!\n")
    format = str(input("Format name or number:\n")).lower()

#encryption block
if (mode == "1" or mode == "encrypt"):
    if (format == "1" or format == "text"):
        message = str(input("Enter message:\n"))

        if (codeName == "1" or codeName == "morse" or codeName == "morse code"):
            encryptedMessage = Morse.encrypt(message)
            print(encryptedMessage)
        if (codeName == "2" or codeName == "atbash" or codeName == "atbash cipher"):
            encryptedMessage = Atbash.encryptDecrypt(message)
            print(encryptedMessage)

    if (format == "2" or format == "file"):
        message = str(input("Enter message:\n"))

        if (codeName == "1" or codeName == "morse" or codeName == "morse code"):
            tofileEncrypted(Morse.encrypt, "MorseEncrypted.txt", "Morse Code\n", "Key: -\n", message)
        if (codeName == "2" or codeName == "atbash" or codeName == "atbash cipher"):
            tofileEncrypted(Atbash.encryptDecrypt, "AtbashEncrypted.txt", "Atbash cipher\n", "Key: -\n", message)

#decryption block
if (mode == "2" or mode == "decrypt"):
    if (format == "1" or format ==  "text"):
        message = str(input("Enter message:\n"))

        if (codeName == "1" or codeName == "morse" or codeName == "morse code"):
            decryptedMessage = Morse.decrypt(message)
            print(decryptedMessage)
        if (codeName == "2" or codeName == "atbash" or codeName == "atbash cipher"):
            decryptedMessage = Atbash.encryptDecrypt(message)
            print(decryptedMessage)

    if (format == "2" or format == "file"):
        fileName = str(input("Enter file name:\n"))
        lines = openEncryptedMassage(fileName)

        if (lines[0]  == "Morse Code\n"):
            tofileDecrypted(Morse.decrypt, "MorseDecrypted.txt", "Morse Code\n", "Key: -\n", lines[2])
        if (lines[0]  == "Atbash cipher\n"):
            tofileDecrypted(Atbash.encryptDecrypt, "AtbashDecrypted.txt", "Atbash cipher\n", "Key: -\n", lines[2])

