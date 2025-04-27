import React, { useState } from 'react';
import axios from 'axios';

function SearchClient({ onSelectClient }) {
  const [searchName, setSearchName] = useState('');
  const [results, setResults] = useState([]);

  const searchClient = async () => {
    const res = await axios.get(`http://127.0.0.1:5000/clients/search?name=${searchName}`);
    setResults(res.data);
  };

  return (
    <div>
      <h2>Search Clients</h2>
      <input 
        value={searchName} 
        onChange={(e) => setSearchName(e.target.value)} 
        placeholder="Search Name" 
      />
      <button onClick={searchClient}>Search</button>
      <ul className="client-list">
        {results.map(client => (
          <li key={client.id}>
            {client.name} <button onClick={() => onSelectClient(client.id)}>View Profile</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SearchClient;
