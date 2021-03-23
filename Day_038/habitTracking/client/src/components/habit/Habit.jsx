import React from 'react'
import './Habit.css'
import { setColor } from '../../colors'

const Habit = ({ name, quantity, date, color }) => {
  const currentColor = setColor(color, quantity)

  return <div className='habit' style={{ backgroundColor: currentColor }}></div>
}

export default Habit
