import React from 'react'
import Habit from '../habit/Habit'
import './HabitDisplay.css'

const HabitDisplay = ({ data, type }) => {
  return (
    <div className='habitDisplay'>
      {data.map((habit) => (
        <Habit key={habit.id} {...habit} color={type.color} />
      ))}
    </div>
  )
}

export default HabitDisplay
