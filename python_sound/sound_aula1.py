from sounddevice import play, wait

from random import random

from math import sin, pi

from time import sleep


def generate_tone(f, duration, sample_rate=44100):
    return [
        sin((x / sample_rate) * 2 * pi * f) for x in range(int(sample_rate * duration))
    ]


def generate_note(delta, duration, base_freq=440):
    return generate_tone(base_freq * pow(2, delta / 12), duration)


def generate_envelope(samples, attack, release):

    result = []
    for x in range(samples):
        print(x - (samples - release))
        if x < attack:
            result.append(x * 1 / attack)

        elif x > (samples - release):
            result.append((samples - x) / release)
            print(result[-1])
        else:
            result.append(1)

    return result


def modulate(wave1, wave2):
    return [wave1[i] * wave2[i] for i in range(len(wave1))]


def apply_envelope(wave):
    return modulate(wave, generate_envelope(len(wave), 100, 100))


notes = [
    [0, 1],
    [2, 1],
    [4, 1],
    [0, 1],
    [0, 1],
    [2, 1],
    [4, 1],
    [0, 1],
    [4, 1],
    [5, 1],
    [7, 2],
    [4, 1],
    [5, 1],
    [7, 2],
]

notes_waves = [apply_envelope(generate_note(n[0], n[1] * 0.5)) for n in notes]


play(sum(notes_waves, []))

wait()
