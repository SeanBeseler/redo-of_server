from __future__ import unicode_literals  #pragma: no cover
import socket  #pragma: no cover
import sys  #pragma: no cover


def response_error(error):
    """Returns a HTTP error response."""
    if error == 400:
        return('HTTP/1.1 400 Bad Request\r\n')
    elif error == 500:
        return('HTTP/1.1 500 Internal Server Error\r\n')
    elif error == 505:
        return('HTTP/1.1 505 HTTP Version Not Supported\r\n')
    elif error == 405:
        return('HTTP/1.1 405 Method Not Allowed\r\n')


def response_ok():
    """ Returns a HTTP 200 response."""
    return('HTTP/1.1 200 OK\r\n')


def parse_request(message): #pragma: no cover
    """Checks to see if the message is a proper HTTP request and return the response"""
    request = message.split()
    if len(request) != 3 :
        return response_error(400)
    if request[0] != 'GET':
        return response_error(405)
    if request[2] != 'HTTP/1.1':
        return response_error(505)
    return response_ok()


def server():  #pragma: no cover
    """ waits for a connection and echos back the message"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5003)
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
                good = parse_request(message)
                echo = good + '\r\n'
                connection.sendall(echo.encode('utf8'))
                connection.close()
                break
            except KeyboardInterrupt:
                server.shutdown(socket.SHUT_WR)
                server.close()
                sys.exit(0)


if __name__ == '__main__':  #pragma: no cover
    server()
