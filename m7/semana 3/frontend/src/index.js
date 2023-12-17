import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios'; // Importe o axios
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Configure a baseURL para apontar para o backend Flask
axios.defaults.baseURL = 'http://localhost:5000'; // Substitua pela URL do seu servidor Flask

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
