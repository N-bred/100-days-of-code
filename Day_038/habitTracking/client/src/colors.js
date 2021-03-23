const COLORS = {
  blue: {
    c1: '#47477b',
    c2: '#1e2456',
    c3: '#000030',
  },
  red: {
    c1: '#f1645d',
    c2: '#d03838',
    c3: '#9c0014',
  },
  green: {
    c1: '#c3e06c',
    c2: '#a2c441',
    c3: '#739708',
  },
}

export function setColor(name, quantity) {
  let color = ''

  if (quantity === 0) return '#fff'

  if (quantity >= 7) {
    color = COLORS[name]['c3']
  } else if (quantity >= 3) {
    color = COLORS[name]['c2']
  } else if (quantity >= 1) {
    color = COLORS[name]['c1']
  }

  return color
}
