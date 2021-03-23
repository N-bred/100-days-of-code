const express = require('express')
const router = express.Router()
const getFile = require('../utils/getFile')
const resolveLocalPath = require('../utils/resolveLocalPath')

router.get('/', async (req, res) => {
  const data = await getFile(resolveLocalPath('../data/all.json'))
  const jsonData = JSON.parse(data)
  res.send(jsonData)
})

module.exports = router
