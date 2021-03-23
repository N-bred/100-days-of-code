const express = require('express')
const router = express.Router()
const getFile = require('../utils/getFile')
const resolveLocalPath = require('../utils/resolveLocalPath')
const createLocalFile = require('../utils/createLocalFile')
const makeYearsDate = require('../makeDates')
const fs = require('fs/promises')

router.get('/', async (req, res) => {
  try {
    await fs.access('../data/all.json')
  } catch (e) {
    if (e.code === 'ENOENT') {
      await createLocalFile('../data/all.json', JSON.stringify([]))
    }
  }
  res.end("Go to /api/types to get the list of all types, and the to /type/{type} to get all of one type's data ")
})

router.get('/types', async (req, res) => {
  try {
    const data = await getFile(resolveLocalPath('../data/all.json'))
    res.json(JSON.parse(data)).status(201)
  } catch (e) {
    console.log(e)
  }
})

router.get('/type/:type', async (req, res) => {
  const { type } = req.params

  try {
    const data = await getFile(resolveLocalPath(`../data/${type}.json`))
    res.json(JSON.parse(data)).status(201)
  } catch (e) {
    console.log(e)
  }
})

router.post('/createCategory', async (req, res) => {
  const { type, color } = req.body

  if (type === '') {
    res.end('No type received').status(401)
    return
  }

  try {
    const dates = makeYearsDate()
    const info = dates.map((date, id) => {
      return {
        id,
        name: '',
        date,
        quantity: 0,
      }
    })

    await createLocalFile(`../data/${type}.json`, JSON.stringify(info))

    // Good
    const allData = await getFile(resolveLocalPath('../data/all.json'))
    const allDataJson = JSON.parse(allData)
    const createdType = {
      type,
      color: color || 'blue',
    }
    allDataJson.push(createdType)

    await createLocalFile('../data/all.json', JSON.stringify(allDataJson))

    res.json({ result: 'type created', type: createdType }).status(201)
  } catch (e) {
    console.log(e)
  }
})

router.post('/type/:type/createHabit', async (req, res) => {
  const { type } = req.params
  const { name, date, quantity } = req.body
  try {
    const data = await getFile(resolveLocalPath(`../data/${type}.json`))
    const jsonData = JSON.parse(data)
    const habit = {
      id: jsonData.length,
      name,
      date,
      quantity,
    }
    jsonData.push(habit)
    await createLocalFile(`../data/${type}.json`, JSON.stringify(jsonData))
    res
      .json({
        result: 'operation done',
        habit: {
          id: jsonData.length,
          name,
          date,
          quantity,
        },
      })
      .status(201)
  } catch (e) {
    console.log(e)
  }
})

router.put('/type/:type/modifyHabit/:date', async (req, res) => {
  const { type, date } = req.params
  const { name, quantity } = req.body
  try {
    const data = await getFile(resolveLocalPath(`../data/${type}.json`))
    const jsonData = JSON.parse(data)
    const habit = { ...jsonData.find((hab) => hab.date === date), name, quantity }
    const modifiedData = jsonData.filter((hab) => hab.date !== date)
    modifiedData.push(habit)
    await createLocalFile(`../data/${type}.json`, JSON.stringify(modifiedData))
    res.json({ result: 'Habit modified', habit }).status(201)
  } catch (e) {
    console.log(e)
  }
})

router.delete('/type/:type/deleteHabit/:date', async (req, res) => {
  const { type, date } = req.params
  try {
    const data = await getFile(resolveLocalPath(`../data/${type}.json`))
    const jsonData = JSON.parse(data)
    const modifiedData = jsonData.filter((hab) => hab.date !== date)
    await createLocalFile(`../data/${type}.json`, JSON.stringify(modifiedData))
    res.json({ result: 'Habit deleted' }).status(201)
  } catch (e) {
    console.log(e)
  }
})

module.exports = router
