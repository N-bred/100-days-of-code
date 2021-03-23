const path = require('path')
const fs = require('fs/promises')
const resolveLocalPath = require('./resolveLocalPath')

async function createLocalFile(path, data) {
  const resolvedPath = resolveLocalPath(path)
  try {
    await fs.writeFile(resolvedPath, data, { encoding: 'utf-8' })
  } catch (e) {
    throw e
  }
}

module.exports = createLocalFile
