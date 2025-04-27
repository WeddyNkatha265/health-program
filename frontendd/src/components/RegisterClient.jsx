import React, { useState } from 'react';
import axios from 'axios';

function RegisterClient() {
  const [clientName, setClientName] = useState('');

  const registerClient = async () => {
    await axios.post('http://127.0.0.1:5000/clients', { name: clientName });
    alert('Client registered!');
    setClientName('');
  };

  return (
    <div className="form-section">
      <h2>Register Client</h2>
      <input 
        value={clientName} 
        onChange={(e) => setClientName(e.target.value)} 
        placeholder="Client Name" 
      />
      <button onClick={registerClient}>Register</button>
    </div>
  );
}

export default RegisterClient;
