from client import client
import pytest
"""you must run server.py to be able to run the test"""


def test_one_buffer_len():
    """test the connection with message size of 8"""
    assert client('12345678') == 'HTTP/1.1 200 OK\r\n12345678\r\n\r\n'
    assert client('abababab') == 'HTTP/1.1 200 OK\r\nabababab\r\n\r\n'
    assert client('seansean') == 'HTTP/1.1 200 OK\r\nseansean\r\n\r\n'


def test_less_buffer_len():
    """test the conncection with the message size of not 8"""
    assert client('123456') == 'HTTP/1.1 200 OK\r\n123456\r\n\r\n'
    assert client('abababa') == 'HTTP/1.1 200 OK\r\nabababa\r\n\r\n'
    assert client('seans') == 'HTTP/1.1 200 OK\r\nseans\r\n\r\n'


def test_mul_buffer_len():
    """test the connection with the message size of multiple of 8"""
    assert client('123456781234567812345678') == 'HTTP/1.1 200 OK\r\n123456781234567812345678\r\n\r\n'
    assert client('abababababababab') == 'HTTP/1.1 200 OK\r\nabababababababab\r\n\r\n'
    assert client('seanseanseansean') == 'HTTP/1.1 200 OK\r\nseanseanseansean\r\n\r\n'
