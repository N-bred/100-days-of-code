const maxiterations = 20
const WIDTH = 400
const HEIGHT = 400
let minSlider
let maxSlider

function setup() {
  createCanvas(WIDTH, HEIGHT)
  pixelDensity(1)
  colorMode(HSL)

  minSlider = createSlider(-1.5, -0, -1.5, 0.1)
  maxSlider = createSlider(0, 1.5, 1.5, 0.1)
}

function draw() {
  for (let x = 0; x < width; ++x) {
    for (let y = 0; y < height; ++y) {
      let xCoord = map(x, 0, width, minSlider.value(), maxSlider.value())
      let yCoord = map(y, 0, height, minSlider.value(), maxSlider.value())

      let originalXCoord = xCoord
      let originalYCoord = yCoord
      let nOfIterations = 0

      for (nOfIterations; nOfIterations < maxiterations; ++nOfIterations) {
        let firstPart = xCoord * xCoord - yCoord * yCoord
        let secondPart = 2 * xCoord * yCoord

        xCoord = firstPart + originalXCoord
        yCoord = secondPart + originalYCoord

        if (abs(xCoord + yCoord) > 16) break
      }

      let bright = map(nOfIterations, 0, maxiterations, 0, 1)
      bright = map(sqrt(bright), 0, 1, 0, 100)

      if (nOfIterations === maxiterations) bright = 0
      set(x, y, color(`hsl(327,${bright}%, ${bright}%)`))
    }
  }
  updatePixels()
  noLoop()
}
