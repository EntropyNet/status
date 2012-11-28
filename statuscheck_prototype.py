import socket

def normalcheck():
    servers = {'amy.entropynet.net': 0, 'bender.entropynet.net': 0, 'kif.entropynet.net': 0, 'leela.entropynet.net': 0, 'scruffy.entropynet.net': 0}
    normalport = '6667'

    for keys in servers:
        try:
            socketcheck = socket.create_connection((keys, normalport))
        except socket.error:
            servers[keys] = 1

    return servers

def sslcheck():
    servers = {'amy.entropynet.net': 0, 'bender.entropynet.net': 0, 'kif.entropynet.net': 0, 'leela.entropynet.net': 0, 'scruffy.entropynet.net': 0}
    sslport = '6697'

    for keys in servers:
        try:
            socketcheck = socket.create_connection((keys, sslport))
        except socket.error:
            servers[keys] = 1

    return servers

def main():
    print normalcheck()
    print sslcheck()

if __name__ == "__main__":
    main()
