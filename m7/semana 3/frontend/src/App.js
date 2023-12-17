import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios'; // Importe o axios
import LoginForm from './components/LoginForm';
import CreateNote from './components/CreateNote';

// Configure a baseURL para apontar para o backend Flask
axios.defaults.baseURL = 'http://localhost:5000'; // Substitua pela URL do seu servidor Flask

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/create-note" element={<CreateNote />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
