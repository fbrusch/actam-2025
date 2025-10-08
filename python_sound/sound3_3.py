import sounddevice as sd
from random import random
from math import sin, pi, pow

sample_rate = 44100


def create_wave(f, t):
    return [sin(t / sample_rate * 2 * pi * f) for t in range(int(sample_rate * t))]


def envelope_wave(wave, attack_decay=0.1):

    result = []
    tt = attack_decay * sample_rate
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


melody_notes = [
    (0, 0.5),
    (2, 0.5),
    (4, 0.5),
    (0, 0.5),
    (0, 0.5),
    (2, 0.5),
    (4, 0.5),
    (0, 0.5),
    (4, 0.5),
    (5, 0.5),
    (7, 1),
    (4, 0.5),
    (5, 0.5),
    (7, 1),
    (
        7,
        0.25,
    ),
    (9, 0.25),
    (
        7,
        0.25,
    ),
    (
        5,
        0.25,
    ),
]

waves = [
    envelope_wave(create_wave(440 * interval_to_freq(n[0]), n[1])) for n in melody_notes
]
wave = sum(waves, [])


if __name__ == "__main__":
    sd.play(wave)
    sd.wait()
