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


def kick(t, f=440):
    k = 10.1
    samples_n = t * sample_rate
    return [
        sin(i / sample_rate * 2 * pi * f * pow(10, -1 * (i / sample_rate) * k))
        for i in range(int(t * sample_rate))
    ]


def hihat(t):
    k = 30  # decadimento molto rapido
    samples_n = int(t * sample_rate)
    return [random() * pow(10, -1 * (i / sample_rate) * k) for i in range(samples_n)]


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

kicks_wave = kick(0.5) * 20
hihats_wave = [0 for _ in range(int(sample_rate * 0.25))] + hihat(0.5) * 20

wave = mix_waves(wave_sawtooth, wave_triangular)
wave = mix_waves(wave, kicks_wave)
wave = mix_waves(wave, hihats_wave)

lead_sequence = [0, None, 2, None, 4, None, 0, None] * 2 + [
    4,
    None,
    5,
    None,
    7,
    None,
    None,
    None,
    4,
    None,
    5,
    None,
    7,
    None,
    None,
    None,
    7,
    9,
    7,
    5,
]
hihat_sequence = [1, 1, 1, 1] * 4
kick_sequence = [1, 0] * 8


def silence(duration):
    return [0.0] * int(sample_rate * duration)


def lead_step(step, duration):
    if step is None:
        return silence(duration)
    else:
        return envelope_wave(
            create_sawtooth_wave(440 * interval_to_freq(step), duration)
        )


def hihat_step(step, duration):
    if step is 0:
        return silence(duration)
    return hihat(duration)


def kick_step(step, duration):
    if step is 0:
        return silence(duration)
    return kick(duration)


step_duration = 0.25


def steps_to_clips(steps, step_to_clip):
    return [step_to_clip(step, step_duration) for step in steps]


lead_clips = steps_to_clips(lead_sequence, lead_step)
hihat_clips = steps_to_clips(hihat_sequence, hihat_step)
kick_clips = steps_to_clips(kick_sequence, kick_step)

lead_wave = sum(lead_clips, [])
hihat_wave = sum(hihat_clips, [])
kick_wave = sum(kick_clips, [])


def mix_many_waves(waves):
    result = []
    for wave in waves:
        result = mix_waves(result, wave)

    return result


sound_wave = mix_many_waves([lead_wave, hihat_wave, kick_wave, kick_wave])

# ------------------------
# lead    |0 2 4 0 2 4
# kick    |1.0 1 0
# hihat   |1 1 1 1
# ------------------------

if __name__ == "__main__":
    sd.play(sound_wave)
    sd.wait()
