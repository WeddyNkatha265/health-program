import React, { useState, useEffect } from 'react';
import axios from 'axios';

function EnrollClient() {
  const [clientName, setClientName] = useState('');
  const [client, setClient] = useState(null);
  const [programs, setPrograms] = useState([]);
  const [selectedProgramId, setSelectedProgramId] = useState('');

  useEffect(() => {
    // Fetch all programs when component loads
    const fetchPrograms = async () => {
      const res = await axios.get('http://127.0.0.1:5000/programs/all'); 
      setPrograms(res.data);
    };

    fetchPrograms();
  }, []);

  const searchClientByName = async () => {
    const res = await axios.get(`http://127.0.0.1:5000/clients/search?name=${clientName}`);
    if (res.data.length > 0) {
      setClient(res.data[0]); // Take the first match
    } else {
      alert('Client not found');
      setClient(null);
    }
  };

  const handleEnroll = async () => {
    if (!client || !selectedProgramId) {
      alert('Please select both client and program');
      return;
    }

    await axios.post('http://127.0.0.1:5000/enroll', {
      client_id: client.id,
      program_ids: [parseInt(selectedProgramId)],
    });

    alert('Client enrolled successfully');
    setClient(null);
    setSelectedProgramId('');
    setClientName('');
  };

  return (
    <div className="form-section">
      <h2>Enroll Client</h2>
      
      <div>
        <input
          type="text"
          value={clientName}
          onChange={(e) => setClientName(e.target.value)}
          placeholder="Enter Client Name"
        />
        <button onClick={searchClientByName}>Search Client</button>
      </div>

      {client && (
        <div style={{ marginTop: 20 }}>
          <h4>Selected Client: {client.name}</h4>

          <select
            value={selectedProgramId}
            onChange={(e) => setSelectedProgramId(e.target.value)}
          >
            <option value="">Select Program</option>
            {programs.map((program) => (
              <option key={program.id} value={program.id}>
                {program.name}
              </option>
            ))}
          </select>

          <div style={{ marginTop: 10 }}>
            <button onClick={handleEnroll}>Enroll</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default EnrollClient;
