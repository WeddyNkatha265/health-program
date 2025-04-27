import React from 'react';

function ClientProfile({ profile }) {
  if (!profile) return null;

  return (
    <div className="profile-section">
      <h2>Client Profile</h2>
      <p><strong>ID:</strong> {profile.id}</p>
      <p><strong>Name:</strong> {profile.name}</p>
      <p><strong>Programs:</strong> {profile.programs.join(', ')}</p>
    </div>
  );
}

export default ClientProfile;
