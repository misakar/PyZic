"""
    PyZic
    ~~~~~
              -,
    ---|--|----|-------
     --|--|----|--------
     _/   |    |_P

    python play music

"""

import os
import wave
import pyaudio

chunk = 1024


class Note():
    """basic note class"""
    def __init__(self):
        self.name = ""
        self.sound_path = r""

    @property
    def sound(self):
        """the note sound"""
        wf = wave.open(self.sound_path, 'rb')
        p = pyaudio.PyAudio()

        # sound stream
        stream = p.open(
            format = p.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
        )

        while True:
            data = wf.readframes(chunk)
            if data == "": break
            # put data into sound stream
            stream.write(data)

        stream.close()
        p.terminate()

    def __repr__(self):
        return "<Note %r>" % self.name


class A(Note):
    """Note Do"""
    def __init__(self):
        self.name = "Do"
        self.sound_path = r"./note/Sound_A.wav"


class B(Note):
    """Note Ra"""
    def __init__(self):
        self.name = "Ra"
        self.sound_path = r"./note/Sound_B.wav"


class C(Note):
    """Note Mi"""
    def __init__(self):
        self.name = "Mi"
        self.sound_path = r"./note/Sound_C.wav"


class D(Note):
    """Note Fa"""
    def __init__(self):
        self.name = "Fa"
        self.sound_path = r"./note/Sound_D.wav"


class E(Note):
    """Note Sol"""
    def __init__(self):
        self.name = "Sol"
        self.sound_path = r"./note/Sound_E.wav"


class F(Note):
    """Note La"""
    def __init__(self):
        self.name = "La"
        self.sound_path = r"./note/Sound_F.wav"


def play(note_list):
    """play note sound"""
    for note in note_list:
        note.sound
