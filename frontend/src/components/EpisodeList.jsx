import { useState, useEffect } from 'react'
import axios from 'axios'

function EpisodeList() {
  const [episodes, setEpisodes] = useState([])
  const [error, setError] = useState(null)

  useEffect(() => {
    axios.get('/api/episodes')
      .then((res) => setEpisodes(res.data))
      .catch((err) => setError(err.message))
  }, [])

  if (error) return <p className="text-red-500">Error: {error}</p>
  if (!episodes.length) return <p>Loading episodes...</p>

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-2xl font-semibold mb-4">Episodes</h2>
      <ul className="space-y-2">
        {episodes.map((episode) => (
          <li key={episode.id} className="border-b py-2">
            <p><strong>Episode {episode.number}</strong> - {episode.date}</p>
            <p>Appearances: {episode.appearances.length ? episode.appearances.map(a => `Guest ${a.guest_id} (Rating: ${a.rating})`).join(', ') : 'None'}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default EpisodeList