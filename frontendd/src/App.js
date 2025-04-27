import React, { useState } from 'react';
import CreateProgram from './components/CreateProgram';
import RegisterClient from './components/RegisterClient';
import SearchClient from './components/SearchClient';
import EnrollClient from './components/EnrollClient';
import ClientProfile from './components/ClientProfile';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedClientProfile, setSelectedClientProfile] = useState(null);

  const fetchClientProfile = async (clientId) => {
    const res = await axios.get(`http://127.0.0.1:5000/clients/${clientId}`);
    setSelectedClientProfile(res.data);
  };

  return (
    <div className="app-container" style={{ padding: 20 }}>
      <h1>Health Information System</h1>
      <CreateProgram />
      <RegisterClient />
      <EnrollClient />
      <SearchClient onSelectClient={fetchClientProfile} />
      <ClientProfile profile={selectedClientProfile} />
    </div>
  );
}

export default App;
