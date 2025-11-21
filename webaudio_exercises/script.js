
//the web audio api only allow sounds with user gesture (no autoplay when the page loads) 
// the user must interact with the page


buttonEl = document.querySelector('button');

// create our context 
let audioContext = new AudioContext();

function playSound() {

    // create an oscillator node (many ways to create an input node)
    let osc = audioContext.createOscillator() // sine by default

    // set type of wave
    osc.type = 'triangle';

    // set frequency 
    osc.frequency.value = 140;

    // up fq over a second
    //osc.frequency.exponentialRampToValueAtTime(300, audioContext.currentTime + 1)

    // create a gain node
    let gain = audioContext.createGain();
    gain.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 1.9)

    // chain on nodes with connect method
    osc.connect(gain).connect(audioContext.destination);
    //osc.connect(audioContext.destination); // the dafault is the speaker
    
    // start and stop oscillator
    osc.start();
    osc.stop(audioContext.currentTime + 2) // the time in secs since the context was instantiated

}

buttonEl.addEventListener('click', function() {

    // if the audio context is not running, resume it by clicking the button
    if (audioContext.state !== 'running') {
        audioContext.resume();
    }

    playSound();
});

