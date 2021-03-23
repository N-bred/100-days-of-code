const express = require('express')
const cors = require('cors')
const bodyParser = require('body-parser')
const router = require('./routes/')
const app = express()
const PORT = process.env.PORT || 5000

app.use(cors())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.use('/', router)

app.listen(PORT, (err) => {
  if (err) throw err
  console.log(`Running on PORT: ${PORT}`)
})
