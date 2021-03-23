import React, { useState, useEffect } from 'react'
import TypesDisplay from './components/typesDisplay/TypesDisplay'

import HabitDisplay from './components/habitDisplay/HabitDisplay'

import './App.css'

async function makeRequest(url, params) {
  const req = await fetch(url)
  const res = await req.json()
  return res
}

function App() {
  const [types, setTypes] = useState([])
  const [currentType, setCurrentType] = useState('')
  const [habits, setHabits] = useState([])

  const makeTypesRequest = async () => {
    const typesData = await makeRequest('http://localhost:5000/api/types')
    setTypes(typesData)
  }

  const makehabitsRequest = async (type) => {
    const habitData = await makeRequest(`http://localhost:5000/api/type/${type}`)
    setHabits(habitData)
  }

  useEffect(() => {
    makeTypesRequest()
  }, [])

  return (
    <div className='App'>
      <TypesDisplay types={types} setHabits={makehabitsRequest} setCurrentType={setCurrentType} />
      <HabitDisplay type={currentType} data={habits}></HabitDisplay>
    </div>
  )
}

export default App
