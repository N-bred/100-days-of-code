function createVolumeSlider() {
  const slider = createSlider(0, 1, 0.1, 0.1)
  slider.position(10, 10)
  slider.style('width', '80px')
  slider.input(changeVolume)
  return slider
}
