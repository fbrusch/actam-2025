import sounddevice as sd
from random import random
from math import sin, pi, pow

sample_rate = 44100


def create_wave(f, t):
    return [sin(t / sample_rate * 2 * pi * f) for t in range(int(sample_rate * t))]


def envelope_wave(wave, tt=10):
    result = []
    for i in range(len(wave)):

        if i < tt:
            result += [wave[i] * (i / tt)]
        elif i > len(wave) - tt:
            result += [wave[i] * (len(wave) - i) / tt]
        else:
            result += [wave[i]]

    return result


def interval_to_freq(semitones):
    return pow(2, semitones / 12)


melody_intervals = [0, 2, 4, 0]

waves = [
    envelope_wave(create_wave(440 * interval_to_freq(i), 1)) for i in melody_intervals
]
wave = sum(waves, [])


if __name__ == "__main__":
    sd.play(wave)
    sd.wait()
