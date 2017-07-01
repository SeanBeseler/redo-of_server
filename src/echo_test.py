from client import client
import pytest
"""you must run server.py to be able to run the test"""


def test_one_buffer_len():
    """test the connection with message size of 8"""
    assert client('12345678') == '12345678\r\n\r\n'
    assert client('abababab') == 'abababab\r\n\r\n'
    assert client('seansean') == 'seansean\r\n\r\n'


def test_less_buffer_len():
    """test the conncection with the message size of not 8"""
    assert client('123456') == '123456\r\n\r\n'
    assert client('abababa') == 'abababa\r\n\r\n'
    assert client('seans') == 'seans\r\n\r\n'


def test_mul_buffer_len():
    """test the connection with the message size of multiple of 8"""
    assert client('123456781234567812345678') == '123456781234567812345678\r\n\r\n'
    assert client('abababababababab') == 'abababababababab\r\n\r\n'
    assert client('seanseanseansean') == 'seanseanseansean\r\n\r\n'
