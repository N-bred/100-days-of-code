const WIDTH = 600
const HEIGHT = 480
let song

function preload() {
  soundFormats('mp3')
  song = loadSound('/music/losing')
  song.setVolume(0.1)
}

function setup() {
  const cnv = createCanvas(600, 480)
  cnv.parent('canvasParent')
  cnv.mousePressed(playAudio)
}

function playAudio() {
  if (!song.isPlaying()) {
    song.play()
  } else {
    song.pause()
  }
}

function draw() {
  background('#000')

  noLoop()
}
