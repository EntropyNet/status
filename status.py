import socket
from flask import Flask
from flask import render_template
status = Flask(__name__)
@status.route('/')

def statuscheck(normservers=None, sslservers=None): 
    normservers = {'amy.entropynet.net': 'OK', 'bender.entropynet.net': 'OK', 'kif.entropynet.net': 'OK', 'leela.entropynet.net': 'OK', 'scruffy.entropynet.net': 'OK'}
    normalport = '6667'

    for keys in normservers:
        try:
            socketcheck = socket.create_connection((keys, normalport))
            socketcheck.close()
        except socket.error:
            normservers[keys] = 'DOWN'

    sslservers = {'amy.entropynet.net': 'OK', 'bender.entropynet.net': 'OK', 'kif.entropynet.net': 'OK', 'leela.entropynet.net': 'OK', 'scruffy.entropynet.net': 'OK'}
    sslport = '6697'

    for keys in sslservers:
        try:
            socketcheck = socket.create_connection((keys, sslport))
            socketcheck.close()
        except socket.error:
            sslservers[keys] = 'DOWN'
    
    return render_template('status.html', normservers=normservers, sslservers=sslservers)
if __name__ == '__main__':
    status.debug = True
    status.run(host='0.0.0.0')
