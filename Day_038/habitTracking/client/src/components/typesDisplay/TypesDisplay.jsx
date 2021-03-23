import React from 'react'

const TypesDisplay = ({ types, setHabits, setCurrentType }) => {
  return (
    <div>
      {types.map((type) => (
        <button
          key={type.type}
          onClick={() => {
            setHabits(type.type)
            setCurrentType(type)
          }}
        >
          {type.type}
        </button>
      ))}
    </div>
  )
}

export default TypesDisplay
