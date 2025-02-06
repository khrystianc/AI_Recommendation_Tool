import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({ title: '', description: '', metadata: {} });

  useEffect(() => {
    axios.get('/items')
      .then(response => setItems(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleChange = (e) => {
    setNewItem({ ...newItem, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/items', newItem)
      .then(response => setItems([...items, response.data]))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h2>Items</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
      <h3>Add New Item</h3>
      <form onSubmit={handleSubmit}>
        <input type="text" name="title" value={newItem.title} onChange={handleChange} placeholder="Title" required />
        <input type="text" name="description" value={newItem.description} onChange={handleChange} placeholder="Description" required />
        <button type="submit">Add Item</button>
      </form>
    </div>
  );
};

export default ItemList;
