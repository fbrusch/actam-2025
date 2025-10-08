import sounddevice as sd
from random import random
from math import sin, pi, pow

sample_rate = 44100


def create_wave(f, t):
    return [sin(t / sample_rate * 2 * pi * f) for t in range(int(sample_rate * t))]


def interval_to_freq(semitones):
    return pow(2, semitones / 12)


wave = (
    create_wave(440, 1)
    + create_wave(440 * interval_to_freq(2), 1)
    + create_wave(440 * interval_to_freq(4), 1)
    + create_wave(440, 1)
)

if __name__ == "__main__":
    sd.play(wave)
    sd.wait()
