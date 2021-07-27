morse_dict = { 'A':'.- ', 'B':'-... ',
                'C':'-.-. ', 'D':'-.. ', 'E':'. ',
                'F':'..-. ', 'G':'--. ', 'H':'.... ',
                'I':'.. ', 'J':'.--- ', 'K':'-.- ',
                'L':'.-.. ', 'M':'-- ', 'N':'-. ',
                'O':'--- ', 'P':'.--. ', 'Q':'--.- ',
                'R':'.-. ', 'S':'... ', 'T':'- ',
                'U':'..- ', 'V':'...- ', 'W':'.-- ',
                'X':'-..- ', 'Y':'-.-- ', 'Z':'--.. ',
                ' ':'/ '}

def encrypt(message):
    message = message.upper()
    newMessage = ''
    for letter in message:
        newMessage += morse_dict[letter]
    return newMessage

def decrypt(message):
    if (message[len(message)-1] != ' '):
        message += ' '
    tmpMorseLetter= ''
    newMessage = ''
    for letter in message:
        if (letter != ' '):
            tmpMorseLetter += letter
        else:
            tmpMorseLetter += ' '
            newMessage += list(morse_dict.keys())[list(morse_dict.values()).index(tmpMorseLetter)]
            tmpMorseLetter = ''
    return newMessage
