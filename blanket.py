import AESCipher
import random
import base64

msg = 'Hello testing'

def generateKeys():
    global sk, vk, vKey, cipher, sig, keyPass, decrypted, message, msg

    secretKey = str(random.randrange(1111111111111111,6666666666666666))
    keyPass = base64.b64encode(secretKey)

    cipher = AESCipher(secretKey)
    print msg
    encrypted = cipher.encrypt(msg)
    vKey = cipher.encrypt(str(vk.to_pem()))


    decrypted = cipher.decrypt(encrypted)

    message = encrypted
    sig = sk.sign(message)


def contactHome():

    global msg, sep, vkey, sig, message

    sep = str(random.randrange(111, 999, 3))

    msg = (sep + keyPass + sep + vKey + sep + cipher.encrypt(sig) + sep + message)
    print msg

    print cipher.decrypt(vkey)

generateKeys()
contactHome()