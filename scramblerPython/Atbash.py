abc = {'A' : 'Z', 'a' : 'z', 'B' : 'Y', 'b' : 'y', 'C' : 'X', 'c' : 'x', 'D' : 'W', 'd' : 'w', 'E' : 'V', 'e' : 'v',
        'F' : 'U', 'f' : 'u', 'G' : 'T', 'g' : 't', 'H' : 'S', 'h' : 's', 'I' : 'R', 'i' : 'r', 'J' : 'Q', 'j' : 'q',
        'K' : 'P', 'k' : 'p', 'L' : 'O', 'l' : 'o', 'M' : 'N', 'm' : 'n', 'N' : 'M', 'n' : 'm', 'O' : 'L', 'o' : 'l',
        'P' : 'K', 'p' : 'k', 'Q' : 'J', 'q' : 'j', 'R' : 'I', 'r' : 'i', 'S' : 'H', 's' : 'h', 'T' : 'G', 't' : 'g',
        'U' : 'F', 'u' : 'f', 'V' : 'E', 'v' : 'e', 'W' : 'D', 'w' : 'd', 'X' : 'C', 'x' : 'c', 'Y' : 'B', 'y' : 'b', 'Z' : 'A', 'z' : 'a'}

def encryptDecrypt(message):
    newMessage = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            #adds the corresponding letter from the lookup_table
            newMessage += abc[letter]
        else:
            # adds space
            newMessage += ' '
    return newMessage

