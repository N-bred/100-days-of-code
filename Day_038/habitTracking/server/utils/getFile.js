const fs = require('fs/promises')

async function getFile(path) {
  const data = await fs.readFile(path, { encoding: 'utf-8' })
  return data
}

module.exports = getFile
