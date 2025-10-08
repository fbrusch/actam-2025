import sounddevice as sd
from random import random

sample_rate = 44100

wave = [random() for _ in range(sample_rate)]  # 1 second worth of noise

sd.play(wave)
sd.wait()
