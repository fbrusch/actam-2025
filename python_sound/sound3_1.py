import sounddevice as sd
from random import random
from math import sin, pi, pow

sample_rate = 44100


def create_wave(f, t):
    return [sin(t / sample_rate * 2 * pi * f) for t in range(int(sample_rate * t))]


def interval_to_freq(semitones):
    return pow(2, semitones / 12)


melody_intervals = [0, 2, 4, 0] * 2 + [4, 5, 7, 7] * 2

waves = [create_wave(440 * interval_to_freq(i), 1) for i in melody_intervals]
wave = sum(waves, [])

if __name__ == "__main__":
    sd.play(wave)
    sd.wait()
