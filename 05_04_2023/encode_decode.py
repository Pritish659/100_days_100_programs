
def encode(encode:str)->str:
    """The sentence is encoded this way-
    every character is converted into its corresponding
    ASCII value then added with 3 and after every word
    add ! instead of whitespace"""
    # encoded = ''.join([chr(ord(i)+3) if i!=' ' else '!' for i in encode])
    encoded = ''
    for i in encode:
        if i == ' ':
            encoded += '!'
            continue
        encoded+= chr(ord(i) + 3)
    return encoded


def decode(decode:str)->str:
    """Decoding is the reverse of the encoding"""
    # decoded = ''.join([chr(ord(i)-3) if i!='!' else ' ' for i in encoded])
    decoded = ''
    for i in decode:
        if i == '!':
            decoded += ' '
            continue
        decoded += chr(ord(i)-3)
    return decoded

if __name__=='__name__':
    encoded = encode('I love coding')
    decode(encoded)
