const WIDTH = 600
const HEIGHT = 480
let song

function preload() {
  soundFormats('mp3')
  song = loadSound('/music/losing')
  song.setVolume(0.1)
}

function setup() {
  // Canvas
  const cnv = createCanvas(600, 480)
  cnv.parent('canvasParent')
  cnv.mousePressed(() => playAudio(song))
  // Volume Slider
  const slider = createVolumeSlider()
  slider.input(() => changeVolume(song, slider))
}

function draw() {
  background('#000')

  noLoop()
}
