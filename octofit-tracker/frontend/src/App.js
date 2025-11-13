

import './App.css';
import { NavLink, Routes, Route } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from '../public/octofitapp-small.png';

function App() {
  return (
    <div className="App container">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 rounded d-flex align-items-center">
        <img src={logo} alt="Octofit Logo" className="App-logo" style={{height:'48px',marginRight:'1rem'}} />
        <NavLink className="navbar-brand fw-bold" to="/">Octofit Tracker</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <NavLink className="nav-link" to="/activities">Activities</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/teams">Teams</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/users">Users</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/workouts">Workouts</NavLink>
            </li>
          </ul>
        </div>
      </nav>
      <div className="mb-4">
        <h1 className="display-4 text-center text-primary">Octofit Tracker</h1>
        <hr />
      </div>
      <Routes>
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/users" element={<Users />} />
        <Route path="/workouts" element={<Workouts />} />
        <Route path="/" element={
          <div className="card mx-auto" style={{maxWidth: '30rem'}}>
            <div className="card-body">
              <h2 className="card-title text-center">Welcome to Octofit Tracker!</h2>
              <p className="card-text text-center">Track your fitness activities, join teams, compete on the leaderboard, and get personalized workout suggestions.</p>
              <NavLink to="/activities" className="btn btn-primary w-100">Get Started</NavLink>
            </div>
          </div>
        } />
      </Routes>
    </div>
  );
}

export default App;
