# coding: utf-8

from pyzic import A, B, C, D, E, F
from pyzic import play


def happySong():
    """a happy song!"""
    play(
        [C(), C(), D(), E(),
        E(), D(), C(), B(),
        A(), A(), B(), C(),
        C(), B(), B()] # =>
    )

# pyzic
happySong()
