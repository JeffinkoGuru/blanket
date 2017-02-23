import base64
import random
from Crypto import Random
from Crypto.Cipher import AES
from ecdsa import SigningKey, VerifyingKey, BadSignatureError, NIST521p

msg = "Hello"

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


class Blanket:

    def cover( self, rawMsg ):
        global sk, vk, vKey, cipher, sig, keyPass, decrypted, message, msg, secretKey

        sk = SigningKey.generate(curve=NIST521p)
        vk = sk.get_verifying_key()


        secretKey = str(random.randrange(1111111111111111, 6666666666666666))
        keyPass = base64.b64encode(secretKey)
        cipher = AESCipher(secretKey)

        encrypted = cipher.encrypt(rawMsg)

        vKey = cipher.encrypt(str(vk.to_pem()))

        decrypted = cipher.decrypt(encrypted)

        message = encrypted
        sig = sk.sign(message)

        sep = str(random.randrange(111, 999, 3))

        msg = (sep + keyPass + sep + vKey + sep + cipher.encrypt(sig) + sep + message)

        return msg

    def uncover( self, rawMsg ):
        global sk, vk, vKey, cipher, sig, keyPass, decrypted, message, msg, secretKey


        ## Decryption Code

        sep = data[0:3]
        details = data.split(sep)

        for detail in details:
            print (base64.b64decode(detail))

        ################################################################################

        sk = SigningKey.generate(curve=NIST521p)
        vk = sk.get_verifying_key()


        secretKey = str(random.randrange(1111111111111111, 6666666666666666))
        keyPass = base64.b64encode(secretKey)
        cipher = AESCipher(secretKey)

        encrypted = cipher.encrypt(rawMsg)

        vKey = cipher.encrypt(str(vk.to_pem()))

        decrypted = cipher.decrypt(encrypted)

        message = encrypted
        sig = sk.sign(message)

        sep = str(random.randrange(111, 999, 3))

        msg = (sep + keyPass + sep + vKey + sep + cipher.encrypt(sig) + sep + message)

        return msg