const fs = require('fs/promises')
const createLocalFile = require('./createLocalFile')

async function appendToLocalFile(path, data) {
  try {
    await fs.unlink(path)
    await createLocalFile(path, data)
  } catch (e) {
    throw e
  }
}

module.exports = appendToLocalFile
