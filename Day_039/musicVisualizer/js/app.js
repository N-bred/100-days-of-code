const WIDTH = 1270
const HEIGHT = 720
const barWidth = 5
const margin = 10
let song
let fft

function preload() {
  soundFormats('mp3')
  song = loadSound('/music/losing')
  song.setVolume(0.1)
}

function setup() {
  // Canvas
  const cnv = createCanvas(WIDTH, HEIGHT)
  cnv.parent('canvasParent')
  cnv.mousePressed(() => playAudio(song))

  // Volume Slider
  const slider = createVolumeSlider()
  slider.input(() => changeVolume(song, slider))
  // FFT
  fft = new p5.FFT()
  fft.setInput(song)
  background('#000')
}
function randomColor() {
  return color(random(0, 255), random(0, 255), random(0, 255), random(50, 255))
}

function drawCircleRects(bars, color) {
  translate(width / 2, height / 2)
  fill(color)
  bars.forEach((bar, i) => {
    rotate(i)
    rect(0, margin, barWidth, (bar * 2) % height)
  })
}

function drawRectRects(bars, color) {
  translate(0, height)
  fill(color)
  bars.forEach((bar, i) => {
    rect(i * barWidth, 0, barWidth, (-bar * 2) % height)
  })
}

function draw() {
  //   clear()

  drawCircleRects(fft.analyze(), randomColor())
  //   drawRectRects(fft.analyze(), randomColor())
}
