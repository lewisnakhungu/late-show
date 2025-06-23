import { useState } from 'react'
import axios from 'axios'

function AppearanceForm() {
  const [formData, setFormData] = useState({
    rating: '',
    episode_id: '',
    guest_id: '',
  })
  const [message, setMessage] = useState(null)

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    axios.post('/api/appearances', formData)
      .then((res) => setMessage('Appearance created successfully!'))
      .catch((err) => setMessage(`Error: ${err.response?.data?.error || err.message}`))
  }

  return (
    <div className="bg-white p-4 rounded shadow mt-6">
      <h2 className="text-2xl font-semibold mb-4">Add Appearance</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium">Rating (1-10)</label>
          <input
            type="number"
            name="rating"
            value={formData.rating}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            min="1"
            max="10"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Episode ID</label>
          <input
            type="number"
            name="episode_id"
            value={formData.episode_id}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            min="1"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Guest ID</label>
          <input
            type="number"
            name="guest_id"
            value={formData.guest_id}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            min="1"
            required
          />
        </div>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Submit
        </button>
      </form>
      {message && <p className={`mt-4 ${message.startsWith('Error') ? 'text-red-500' : 'text-green-500'}`}>{message}</p>}
    </div>
  )
}

export default AppearanceForm