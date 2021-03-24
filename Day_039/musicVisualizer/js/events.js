function changeVolume(song, slider) {
  song.setVolume(slider.value())
}

function playAudio(song) {
  if (!song.isPlaying()) {
    song.play()
  } else {
    song.pause()
  }
}
