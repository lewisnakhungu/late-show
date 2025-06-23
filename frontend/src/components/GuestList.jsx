import { useState, useEffect } from 'react'
import axios from 'axios'

function GuestList() {
  const [guests, setGuests] = useState([])
  const [error, setError] = useState(null)

  useEffect(() => {
    axios.get('/api/guests')
      .then((res) => setGuests(res.data))
      .catch((err) => setError(err.message))
  }, [])

  if (error) return <p className="text-red-500">Error: {error}</p>
  if (!guests.length) return <p>Loading guests...</p>

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-2xl font-semibold mb-4">Guests</h2>
      <ul className="space-y-2">
        {guests.map((guest) => (
          <li key={guest.id} className="border-b py-2">
            <p><strong>{guest.name}</strong> - {guest.occupation}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default GuestList