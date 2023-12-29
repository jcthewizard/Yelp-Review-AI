// Main React component
import React, { useState } from 'react';

function App() {
  const [restaurantId, setRestaurantId] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    // Here you can call your backend API
    console.log(`Restaurant ID: ${restaurantId}`);
    // Example: await fetch('/api/getRestaurantDetails', { method: 'POST', body: JSON.stringify({ restaurantId }) });
  };

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label>
            Restaurant ID:
            <input
              type="text"
              value={restaurantId}
              onChange={e => setRestaurantId(e.target.value)}
            />
          </label>
          <button type="submit">Get Details</button>
        </form>
      </header>
    </div>
  );
}

export default App;
