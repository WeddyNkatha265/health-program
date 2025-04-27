import React, { useState } from 'react';
import axios from 'axios';

function CreateProgram() {
  const [programName, setProgramName] = useState('');

  const createProgram = async () => {
    await axios.post('http://127.0.0.1:5000/programs', { name: programName });
    alert('Program created!');
    setProgramName('');
  };

  return (
    <div div className="form-section">
      <h2>Create Health Program</h2>
      <input 
        value={programName} 
        onChange={(e) => setProgramName(e.target.value)} 
        placeholder="Program Name" 
      />
      <button onClick={createProgram}>Create Program</button>
    </div>
  );
}

export default CreateProgram;
