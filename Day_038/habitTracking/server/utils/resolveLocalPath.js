const path = require('path')

function resolveLocalPath(p) {
  return path.join(__dirname, p)
}

module.exports = resolveLocalPath
