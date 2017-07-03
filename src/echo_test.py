from client import client
from server import response_ok
from server import response_error
import pytest
"""you must run server.py to be able to run the test"""


def test_response_ok():
    """test the 200 response function"""
    assert response_ok() == 'HTTP/1.1 200 OK\r\n'


def test_response_error_500():
    """test the response error for error 500"""
    assert response_error(500) == 'HTTP/1.1 500 Internal Server Error\r\n'


def test_response_error_400():
    """test the response error for error 400"""
    assert response_error(400) == 'HTTP/1.1 400 Bad Request\r\n'


def test_response_error_405():
    """test the response error for the error 405"""
    assert response_error(405) == 'HTTP/1.1 405 Method Not Allowed\r\n'


def test_response_error_505():
    """test the response error for error 505"""
    assert response_error(505) == 'HTTP/1.1 505 HTTP Version Not Supported\r\n'


def test_one_buffer_len():
    """test the connection with message size of 8"""
    assert client('GET 12345678 HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
    assert client('GET abababab HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
    assert client('GET seansean HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'


def test_less_buffer_len():
    """test the conncection with the message size of not 8"""
    assert client('GET 123456 HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
    assert client('GET abababa HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
    assert client('GET seans HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'


def test_mul_buffer_len():
    """test the connection with the message size of multiple of 8"""
    assert client('GET 123456781234567812345678 HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
    assert client('GET abababababababab HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
    assert client('GET seanseanseansean HTTP/1.1') == 'HTTP/1.1 200 OK\r\n\r\n'
