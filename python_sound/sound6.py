import sounddevice as sd
from random import random
from math import sin, pi, pow

sample_rate = 44100


def create_wave(f, t):
    return [sin(t / sample_rate * 2 * pi * f) for t in range(int(sample_rate * t))]


def create_sawtooth_wave(f, t):
    n_samples = int(t * sample_rate)
    period_samples = int(sample_rate / f)

    return [(i % period_samples) / period_samples for i in range(n_samples)]


def create_triangular_wave(f, t):
    n_samples = int(t * sample_rate)
    period_samples = int(sample_rate / f)
    single_triangle = [i / period_samples for i in range(period_samples)] + [
        1 - (i / period_samples) for i in range(period_samples)
    ]
    n_triangles = int(n_samples / period_samples / 2)
    return single_triangle * n_triangles


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


def safe_get(l, i):
    if i < len(l):
        return l[i]
    return 0


def mix_waves(wave1, wave2):
    result = []

    for i in range(max(len(wave1), len(wave2))):
        result.append(safe_get(wave1, i) + safe_get(wave2, i))
    return result


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
]

waves_triangular = [
    envelope_wave(create_triangular_wave(440 * interval_to_freq(n[0]), n[1]))
    for n in melody_notes
]

wave_triangular = sum(waves_triangular, [])

waves_sawtooth = [
    envelope_wave(create_sawtooth_wave(440 * interval_to_freq(n[0]), n[1]))
    for n in melody_notes
]

wave_sawtooth = sum(waves_sawtooth, [])

wave = mix_waves(wave_sawtooth, wave_triangular)

if __name__ == "__main__":
    sd.play(wave)
    sd.wait()
