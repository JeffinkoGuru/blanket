# server.py
import socket
import time
import logging
import logging.handlers
import json

## LOGGING ##

## NOT RECOMMENDED IN PRODUCTION!!
# In wild should be /dev/null

LOG_FILENAME = '/dev/null'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME)

logger.addHandler(handler)

# Add formatting to logging messages
formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
handler.setFormatter(formatter)

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "127.0.0.1"

port = 4200

# bind to the port
serversocket.bind((host, port))
logger.info('Listening...')

# queue up to 5 requests
serversocket.listen(5)


while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    logger.info("Got a connection from %s" % str(addr))

    print('Got connection. Reading data..')


    data = clientsocket.recv(1024)
    clientsocket.close()

    print (data)
    sep = data[0:3]
    print (sep)
    details = data.split(sep)

    for detail in details:
        print (detail)

