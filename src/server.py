from __future__ import unicode_literals  #pragma: no cover
import socket  #pragma: no cover
import sys  #pragma: no cover


def response_error():
    """Returns a HTTP error response."""
    return(b'HTTP/1.1 500 Internal Server Error\r\n')


def response_ok():
    """ Returns a HTTP 200 response."""
    return(b'HTTP/1.1 200 OK\r\n')


def server():  #pragma: no cover
    """ waits for a connection and echos back the message"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    while True:
        server.listen(1)
        while True:
            try:
                connection, address = server.accept()
                message = ''
                buffer_len = 8
                while True:
                    part = connection.recv(buffer_len)
                    message += part.decode('utf8')
                    if '\r\n\r\n' in message:
                        break
                print(message)
                echo = response_ok + message + '\r\n\r\n'
                connection.sendall(echo.encode('utf8'))
                connection.close()
                break
            except KeyboardInterrupt:
                server.shutdown(socket.SHUT_WR)
                server.close()
                sys.exit(0)


if __name__ == '__main__':  #pragma: no cover
    server()
