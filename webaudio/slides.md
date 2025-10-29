---
title: Web Audio Constructors & AudioParams
---

# Introduction to Web Audio API 
- The Web Audio API is modeled after modular synthesizers: sources, processors, and outputs you can patch together freely.
- Each block is a node, designed to be combined like modules on a Eurorack or classic analog rig.
- The browser runs the graph on the audio thread, so once wired the sound flows autonomously.

---

## Core Architecture
- `AudioContext` is the session: it allocates the audio graph, provides the current time, and manages scheduling.
- Nodes (oscillators, gains, filters…) are created via `context.create*` constructors and connected in series or parallel.
- `AudioParam` objects expose precise, sample-accurate parameter control, supporting instant changes and time-based automation.
- Sources can be real-time (oscillators, microphone) or buffers, processed through effects, and finally routed to the destination.

---

## Node Landscape
- Source nodes: `OscillatorNode`, `AudioBufferSourceNode`, `MediaStreamAudioSourceNode` for mic or media inputs.
- Processing nodes: `GainNode`, `BiquadFilterNode`, `DelayNode`, `DynamicsCompressorNode`, `WaveShaperNode`.
- Control/utility nodes: `ConstantSourceNode`, `AudioWorkletNode` for custom DSP, `PannerNode` for spatialization.
- Destination nodes: `AudioDestinationNode` (the speakers) plus `MediaStreamAudioDestinationNode` to record or stream.

---

## Mental Model: Patch the Graph
- Think of each node as a physical module; `connect()` is the virtual patch cable forming a directed graph.
- Signals flow downstream, but automation can schedule future changes with `setValueAtTime` and ramps tied to the context clock.
- You can branch, sum, or feedback signals by connecting nodes creatively, enabling complex synths, effects, or spatial scenes.

---

# Web Audio Building Blocks
- Using a few Web Audio constructors we can build complete signal chains directly in the browser.
- Each example comes from the existing HTML demos in this folder.

---

## Constructors in Action

```html
const c = new AudioContext();
const o = c.createOscillator();
o.connect(c.destination);
o.start();
```

- `AudioContext` is the main entry point; instantiate it with `new AudioContext()` to access the audio graph. (`index1.html`)
- `createOscillator()` constructs an `OscillatorNode`, while `connect()` wires it to `AudioDestinationNode`, completing the signal path.
- `start()` begins the oscillator immediately: without calling it, the node stays silent.

---

## Enabling Playback on User Gesture

```html
document.body.onclick = () => c.resume();
```

- Browsers suspend `AudioContext` objects until a user gesture is detected, so resuming inside a click handler makes the first example audible. (`index2.html`)
- Remember to resume only once; subsequent clicks simply resolve immediately.

---

## Introducing AudioParams

```html
o.frequency.value = 550;
document.getElementById("changeFrequency")
  .onclick = () => (o.frequency.value = 220);
```

- Properties such as `frequency` on an `OscillatorNode` are `AudioParam` objects. (`index2.html`)
- Assigning `AudioParam.value` changes the parameter instantly, giving us immediate control over pitch.

---

## Continuous Control with Inputs

```html
const slider = document.getElementById("frequencySlider");
slider.oninput = () => (o.frequency.value = slider.value);
```

- HTML inputs can drive `AudioParam` values for expressive controls. (`index3.html`)
- Because `slider.value` is a string, Web Audio converts it to a number on assignment; coerce manually if you need numeric math beforehand.

---

## Chaining GainNodes

```html
const g = c.createGain();
o.connect(g);
g.connect(c.destination);
g.gain.value = 1;
```

- `createGain()` returns a `GainNode`, whose `gain` property is another `AudioParam`. (`index5.html`)
- Positioning gain nodes between sources and destinations lets you sculpt loudness or build mixers.
- Just like frequency, you can update `gain.value` in response to UI events such as sliders.

---

## Modulating Parameters with Other Nodes

```html
const lfo = c.createOscillator();
lfo.connect(g.gain);
lfo.frequency.value = 10;
document.getElementById("startLFO").onclick = () => lfo.start();
```

- Any audio signal can drive an `AudioParam`; connecting an LFO oscillator to `g.gain` produces tremolo. (`index5_1.html`)
- The LFO runs in the same audio graph, so modulation stays sample-accurate and does not require manual updates.

---

## Extension Exercises

- Rework the oscillator examples into a simple three-voice synthesizer: add buttons for `A`, `C#`, and `E`, each calling `setFrequency()` with the right value.
- Expand the slider patch with range and waveform selectors (`o.type = "square"`) for timbre exploration.
