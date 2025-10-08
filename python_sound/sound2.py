import sounddevice as sd
from random import random
from math import sin, pi

sample_rate = 44100

wave = [
    sin(t / sample_rate * 2 * pi * 440) for t in range(sample_rate)
]  # 1 second worth of 440hz tone

sd.play(wave)
sd.wait()
