import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';

const Recommendations = () => {
  const [recommendations, setRecommendations] = useState([]);
  const user = useSelector(state => state.auth.user);

  useEffect(() => {
    if (user) {
      axios.get(`/recommendations/${user.id}`)
        .then(response => setRecommendations(response.data))
        .catch(error => console.error(error));
    }
  }, [user]);

  return (
    <div>
      <h2>Recommendations</h2>
      <ul>
        {recommendations.map((rec, index) => (
          <li key={index}>{rec}</li>
        ))}
      </ul>
    </div>
  );
};

export default Recommendations;
