import React from 'react';
import RegisterForm from './components/RegisterForm';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="/" element={<RegisterForm />} />
    </Routes>
  );
}

export default App;