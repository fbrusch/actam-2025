let audioContext;
try {
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
} catch (e) {
    console.error('Web Audio API is not supported in this browser');
}

//let NoiseBuffer = new AudioBufferSourceNode(audioContext, {loop:true})
let NoiseBuffer = audioContext.createBufferSource()
NoiseBuffer.loop=true
const bufferSize = audioContext.sampleRate * 1;
const buffer = audioContext.createBuffer(1, bufferSize, audioContext.sampleRate)
const data = buffer.getChannelData(0);
for (i=0; i<bufferSize; i++) {
    // Fill the buffer with white noise, so values between -1.0 and +1.0
    data[i] = 2*Math.random()-1
}
NoiseBuffer.buffer=buffer

let NoiseGain = audioContext.createGain()
NoiseGain.gain.value=0

let delay= audioContext.createDelay()
delay.delayTime.value=0.001

let feedbackGain= audioContext.createGain()
feedbackGain.gain.value=0.8
  
NoiseBuffer.start() // start the noise source, but inaudible because of zero gain

// Route the nodes
NoiseBuffer.connect(NoiseGain)

NoiseGain.connect(audioContext.destination)
NoiseGain.connect(delay)

delay.connect(feedbackGain)

feedbackGain.connect(delay)
feedbackGain.connect(audioContext.destination)

// UI elements

// This controls feedback gain
// The higher the value, the longer the sound will last
document.getElementById("Decay").addEventListener("input", function() {
    feedbackGain.gain.value=this.value
    DecayLabel.innerHTML = this.value
})    

// This controls delay time
document.getElementById("Delay").addEventListener("input", function() {
    delay.delayTime.value=0.001*this.value
    DelayLabel.innerHTML = this.value
})

// This controls the noise burst width
document.getElementById("Width").addEventListener("input", function() {
    WidthLabel.innerHTML = this.value
})

document.getElementById("Play").addEventListener("click", function() {
    audioContext.resume()
    let now = audioContext.currentTime
    NoiseGain.gain.setValueAtTime(1, now)
    NoiseGain.gain.linearRampToValueAtTime(0, now + Width.value/1000)
})