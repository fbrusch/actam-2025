---
theme: default
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  Slides for introducing Python and sound generation with `sounddevice`
---

# Python beyond problem solving

- We have seen how to use Python to interactively explore/solve a problem.  
- But… can we use it for something else?  
- Obviously **yes**!

---

# Where can Python be used?

- **Backend** of web applications/infrastructures  
  - e.g. YouTube, PayPal, [add other famous apps/infrastructures: Instagram, Spotify, Dropbox]  
- **Videogames** (e.g. with `pygame`)  
- **Automation / scripting** (examples: file manipulation, web scraping, batch processing)  
- ...  

---

# Can Python "play" music / generate sound?

- Let’s find out!  

---

# First, a general observation

- Python runs on our computer.  
- Our computer has a **speaker**.  
- So, in principle, we can imagine/hope that Python could somehow *access* or *control* the speaker.  

---

# The general situation

- On one side: a process/programming language/automatic executor.  
- On the other side: a "piece of the world" we want our executor to:  
  - **Observe** the state of the world, obtaining information.  
  - **Modify** the state of the world.  
  [Here we are framing the general concept of "interface" between software and the environment]  

---

# Interfaces in the world

- Many "pieces of the world" / systems are designed to be *read* and *controlled*.  
- Example: the lamps in this room.  
  - They are designed to be turned on/off via **switches**.  
  - Switches are designed for **humans**, who manipulate them mechanically.  
- A standard car offers an **interface** designed for humans, with certain average anthropometric characteristics.  


---

# A small problem

- Suppose we want Python to turn a lamp on/off. Could it?  
  - Yes, but it would need a **dedicated interface**!  
  - For example: a function `switch_lamp(state)` that turns the lamp on/off when called with `1` or `0`.  

---

# Interfaces for executors

- An interface designed to be controlled by an automatic executor (like Python) is called an **Application Programming Interface (API)**.  

- Is there an API that allows Python to access the speaker?  
  - (In practice, the **sound card** that controls the speaker, etc.)  
- Yes! Several exist.  
- A very popular, cross-platform one is [`sounddevice`](https://python-sounddevice.readthedocs.io/en/0.5.1/).  

---

# The `sounddevice` interface

The documentation shows a simple interface:

```python
import sounddevice as sd
```
```
```
```
```

# Playback

Assuming you have a NumPy array named myarray holding audio data with a sampling frequency of fs (in most cases this will be 44100 or 48000 frames per second), you can play it back with `play()`:

```python
sd.play(myarray, fs)
```

- L'interfaccia è piuttosto "brutale": possiamo suonare un array/lista di _sample_
- Proviamo a fare qualche esercizio/esperimento!

esercizio 1: suonare un secondo di rumore bianco
esercizio 2: suonare un secondo di un tono a 440hz (A4)
esercizio 3: suonare due note (A4, B4) da un secondo, una di seguito all'altra
esercizio 4: suonare tre note (A4, B4, C#5) da un secondo, una di seguito all'altra
esercizio 5: suonare le tre note con un'onda quadra invece che con semplice tono
esercizio 6: suonare le tre note con un'onda a dente di sega
esercizio 7: aggiungere lfo (modulazione sinusoidale a 15hz)
esercizio 8: suonare tutto FJ
