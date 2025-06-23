
# Late Show Manager

A full-stack web application to manage episodes, guests, and appearances for a late-night show. The backend is built with Flask, and the frontend is a React application powered by Vite, styled with Tailwind CSS.

- **Backend**: Flask with SQLite database, running on `http://127.0.0.1:5000`.
- **Frontend**: React with Vite, connecting to the backend via API endpoints.

## Features
- View a list of episodes with their appearances.
- View a list of guests with their occupations.
- Add new appearances with ratings, episode IDs, and guest IDs.

## Prerequisites
- **Node.js**: v16+ (e.g., v18.17.0)
- **npm**: v8+ (e.g., 9.6.7)
- **Python**: v3.8+ with `pip`
- **Git** (optional, for cloning)

## Installation

### Backend Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd late-show
Create a Virtual Environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:
bash
pip install -r requirements.txt
(Note: Create requirements.txt with pip freeze > requirements.txt if not present.)
Initialize the Database:
Ensure instance/ directory exists.
Run migrations (if using Flask-Migrate):
bash
flask db init  # Only once
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database:
bash
python scripts/seed.py
Run the Backend:
bash
python run.py
The server will start on http://127.0.0.1:5000.
Frontend Setup
Navigate to Frontend Directory:
bash
cd frontend
Install Dependencies:
bash
npm install
Run the Development Server:
bash
npm run dev
Open http://localhost:5173 in your browser.
Usage
Episodes: Displays a list of episodes with associated appearances.
Guests: Shows a list of guests with their occupations.
Appearance Form: Add a new appearance by entering a rating (1-10), episode ID, and guest ID.
API Endpoints (for testing):
GET /api/episodes
GET /api/guests
POST /api/appearances (requires JSON: {"rating": 8, "episode_id": 1, "guest_id": 1})
Configuration
Backend: Check app/config.py for settings (e.g., database URI).
Frontend: 
Proxy to backend set in vite.config.js (/api -> http://127.0.0.1:5000).
Tailwind CSS configured in tailwind.config.js and postcss.config.cjs.
File Structure
late-show/
├── app/              # Flask backend
│   ├── __init__.py   # App initialization
│   ├── config.py     # Configuration
│   ├── models.py     # Database models
│   ├── resources.py  # API resources
│   └── extensions.py # Flask extensions
├── instance/         # Database and migration files
│   └── app.db        # SQLite database
├── scripts/          # Seed scripts
│   └── seed.py       # Database seeding
├── run.py            # Backend entry point
├── frontend/         # React frontend
│   ├── src/          # React components and styles
│   │   ├── App.jsx   # Main component
│   │   ├── index.css # Tailwind styles
│   │   └── components/ # Sub-components
│   ├── tailwind.config.js # Tailwind configuration
│   ├── postcss.config.cjs # PostCSS configuration
│   ├── vite.config.js # Vite configuration
│   ├── package.json   # Node dependencies
│   └── node_modules/  # Node modules
├── requirements.txt  # Python dependencies
└── README.md         # This file
Contributing
Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit changes: git commit -m "Description".
Push to the branch: git push origin feature-name.
Open a Pull Request.
Issues
Report bugs or suggest features via GitHub Issues (if hosted).
License
[Add license, e.g., MIT] - Specify if applicable.


