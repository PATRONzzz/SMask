import React from 'react';
import RegisterForm from './components/RegisterForm';
import TaskForm from './components/TaskForm';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
        <Route path="/auth" element={<RegisterForm />} />
        <Route path="/tasks" element={<TaskForm />} />
    </Routes>
  );
}

export default App;