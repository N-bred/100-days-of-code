const express = require('express')
const router = express.Router()
const getFile = require('../utils/getFile')
const resolveLocalPath = require('../utils/resolveLocalPath')
const createLocalFile = require('../utils/createLocalFile')

router.get('/', async (req, res) => {
  const data = await getFile(resolveLocalPath('../data/all.json'))
  const jsonData = JSON.parse(data)
  res.send(jsonData)
})

router.post('/createCategory', async (req, res) => {
  const { type, color } = req.body

  if (type === '') {
    res.end('No type received').status(401)
    return
  }

  try {
    await createLocalFile(`../data/${type}.json`, JSON.stringify([]))
    const allData = await getFile(resolveLocalPath('../data/all.json'))
    const allDataJson = JSON.parse(allData)
    allDataJson.push({
      type,
      color: color || 'blue',
    })
    await createLocalFile('../data/all.json', JSON.stringify(allDataJson))
  } catch (e) {
    console.log(e)
  }
})

module.exports = router
