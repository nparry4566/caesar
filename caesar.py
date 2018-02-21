alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321!@#$%^&*()_+=-\\][|}{';:/.,?><`~\""

def shift(letter,n):
    unicode = chr(ord(letter) + n)
    if ord(unicode) > 126:
        return chr(ord(unicode) - 95)
    elif ord(unicode) < 32:
        return chr(ord(unicode) - 95)

    return unicode

def encrypt(message, shift_amount):
    new = ""
    for c in message:
        new += shift(c, shift_amount)

    return new

def decrypt(message, shift_amount):
    new = ""
    for c in message:
        new += shift(c, -1 * shift_amount)

    return new

message = "big boy pants"
encrypted_message = encrypt(message, 30)
decrypted_message = decrypt(encrypted_message, 30)    

print(message)
print(encrypted_message)
print(decrypted_message)
