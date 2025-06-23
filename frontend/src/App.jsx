import EpisodeList from './components/EpisodeList'
import GuestList from './components/GuestList'
import AppearanceForm from './components/AppearanceForm'

function App() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6 text-center">Late Show Manager</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <EpisodeList />
        <GuestList />
      </div>
      <AppearanceForm />
    </div>
  )
}

export default App