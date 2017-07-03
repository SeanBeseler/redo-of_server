from __future__ import unicode_literals
import socket
import sys


def client(message):
    """connects to the sever and returns the echo message"""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        client.connect(('127.0.0.1', 5003))
        message += '\r\n\r\n'
        client.sendall(message.encode('utf8'))
        buffer_len = 8
        responce_mess = b''
        while True:
            part = client.recv(buffer_len)
            responce_mess += part
            if b'\r\n\r\n' in responce_mess:
                break
        responce_mess = responce_mess.decode('utf8')
        client.shutdown(socket.SHUT_WR)
        client.close()
        return responce_mess
    except KeyboardInterrupt:
            client.shutdown(socket.SHUT_WR)
            client.close()
            sys.exit(0)


if __name__ == '__main__':
    print(client(sys.argv[1]))
