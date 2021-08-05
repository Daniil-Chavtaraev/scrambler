import Morse
import Atbash
import Caesar

#Добавить проверки: Формат файла, символы, формат ключа

#Добавить комменты

#Написать тесты

def openEncryptedMassage(fileName):
    fileMessage = open(fileName, "r")
    lines = fileMessage.readlines()
    fileMessage.close()
    return lines

def tofileDecrypted(func, fileName, code, key, message, boolKey):
    decryptedMessage = open(fileName, "w")
    decryptedMessage.write(code)
    decryptedMessage.write(str(key) + "\n")
    if (boolKey):
        decryptedMessage.write(func(message, key))
    else:
        decryptedMessage.write(func(message))
    decryptedMessage.close()

def tofileEncrypted(func, fileName, code, key, message, boolKey):
    encryptedMessage = open(fileName, "w+")
    encryptedMessage.write(code)
    encryptedMessage.write(str(key) + "\n")
    if (boolKey):
        encryptedMessage.write(func(message, key))
    else:
        encryptedMessage.write(func(message))
    encryptedMessage.close()

def checkFileFomat(filename, codeNames):
    with open(filename):
        line_count = 0
        for line in filename:
            line_count += 1
    if (line_count != 3):
        return False
    fileMessage = open(fileName, "r")
    lines = fileMessage.readlines()
    fileMessage.close()
    if((lines[0] - "\n").lower() not in codeNames):
        return False
    else:
        return True

def checkMessageFormat(text):
    if all(x.isalpha() or x.isspace() for x in text):
        return True
    else:
        return False


#Arrays with parameters
codeNames = ["1", "2", "3", "morse", "morse code", "atbash", "atbash cipher", "caesar", "caesar cipher"]
modeNames = ["1", "2", "encrypt", "decrypt"]
formats = ["1", "2", "text", "file"]
#In this block we are selecting encryption/decryption parameters
print("Select code:\n 1) Morse code\n 2) Atbash cipher\n 3) Caesar cipher")
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
        while (not checkMessageFormat(message)):
            print("Message could contain only letters and spaces, plesae re-enter message:")
            message = str(input("Enter message:\n"))

        if (codeName == "1" or codeName == "morse" or codeName == "morse code"):
            encryptedMessage = Morse.encrypt(message)
            print(encryptedMessage)
        if (codeName == "2" or codeName == "atbash" or codeName == "atbash cipher"):
            encryptedMessage = Atbash.encryptDecrypt(message)
            print(encryptedMessage)
        if (codeName == "3" or codeName == "caesar" or codeName == "caesar cipher"):
            key = int(input("Enter key:\n"))
            encryptedMessage = Caesar.encrypt(message, key)
            print(encryptedMessage)

    if (format == "2" or format == "file"):
        message = str(input("Enter message:\n"))
        while (not checkMessageFormat(message)):
            print("Message could contain only letters and spaces, plesae re-enter message:")
            message = str(input("Enter message:\n"))

        if (codeName == "1" or codeName == "morse" or codeName == "morse code"):
            tofileEncrypted(Morse.encrypt, "MorseEncrypted.txt", "Morse Code\n", 0, message, False)
        if (codeName == "2" or codeName == "atbash" or codeName == "atbash cipher"):
            tofileEncrypted(Atbash.encryptDecrypt, "AtbashEncrypted.txt", "Atbash cipher\n", 0, message, False)
        if (codeName == "3" or codeName == "caesar" or codeName == "caesar cipher"):
            key = int(input("Enter key:\n"))
            tofileEncrypted(Caesar.encrypt, "CaesarEncrypted.txt", "Caesar cipher\n", key, message, True)

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
        if (codeName == "3" or codeName == "caesar" or codeName == "caesar cipher"):
            key = int(input("Enter key:\n"))
            decryptedMessage = Caesar.decrypt(message, key)
            print(decryptedMessage)

    if (format == "2" or format == "file"):
        fileName = str(input("Enter file name:\n"))
        lines = openEncryptedMassage(fileName)

        if (lines[0]  == "Morse Code\n"):
            tofileDecrypted(Morse.decrypt, "MorseDecrypted.txt", "Morse Code\n", 0, lines[2], False)
        if (lines[0]  == "Atbash cipher\n"):
            tofileDecrypted(Atbash.encryptDecrypt, "AtbashDecrypted.txt", "Atbash cipher\n", 0, lines[2], False)
        if (lines[0]  == "Caesar cipher\n"):
            tofileDecrypted(Caesar.decrypt, "CaesarDecrypted.txt", "Caesar cipher\n", int(lines[1]), lines[2], True)
        

