
def caesar(key,plain_text):
    encrypted_text = ""
    for c in plain_text:
        # checking it is upper
        if c.isupper():

            
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index + key) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encrypted_text = encrypted_text + new_character
        elif c.islower(): #checking it is upper
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
            new_index = (c_index + key) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            encrypted_text = encrypted_text + new_character

        else:

            #  # if character is not upper or lower,  leave it as it is
            encrypted_text += c

    print("Encrypted text:",encrypted_text)
caesar(1,"HELLO")
caesar(3,"HELLO")
caesar(13,"HELLO")

