def rotate(text, key):
    cypher_text = ''
    for i in text:
        cypher_text = cypher_text + rotate_char(i, key)

    return cypher_text
    pass

def rotate_char(char, key):
    if char.isupper():
        if ord(char) + key > 90:
            char = chr(ord(char) - (26 - key))
        else:
            char = chr(ord(char) + key)
    if char.islower():
        if ord(char) + key > 122:
            char = chr(ord(char) - (26 - key))
        else:
            char = chr(ord(char) + key)
    return char
