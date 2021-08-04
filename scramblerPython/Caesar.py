abc = "abcdefghijklmnopqrstuvwxyz"

abcUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryptCheck(idx, key):
    if (idx + key >= 26):
        return (idx + key) % 26
    else:
        return idx + key

def decryptCheck(idx, key):
    if (idx - key < 0):
        return 26 + (idx - key)
    else:
        return idx - key
    

def encrypt(message, key):
    newKey = key % 26
    newMessage = ''
    for letter in message:
        if (letter != " "):
            if (letter.isupper()):
                newMessage += abcUpper[encryptCheck(abcUpper.find(letter), newKey)]
            else:
                newMessage += abc[encryptCheck(abc.find(letter), newKey)]
        else:
            newMessage += ' '
    return newMessage

def decrypt(message, key):
    newKey = key % 26
    newMessage = ''
    for letter in message:
        if (letter != " "):
            if (letter.isupper()):
                newMessage += abcUpper[decryptCheck(abcUpper.find(letter), newKey)]
            else:
                newMessage += abc[decryptCheck(abc.find(letter), newKey)]
        else:
            newMessage += ' '
    return newMessage