import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';
import './App.css';

function App() {
  const [laptops, setLaptops] = useState([]);

  useEffect(() => {
    async function fetchLaptops() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/laptops');
        setLaptops(response.data);
      } catch (error) {
        console.error('Error fetching laptops:', error);
      }
    }

    fetchLaptops();
  }, []);

  return (
    <div className="App">
      <h1>Laptop Deals</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Name</th>
            <th>Initial Price</th>
            <th>Final Price</th>
            <th>Savings</th>
          </tr>
        </thead>
        <tbody>
          {laptops.map((laptop, index) => (
            <tr key={index}>
              <td><a href={laptop.link}>{laptop.name}</a></td>
              <td>{laptop.initial_price}</td>
              <td>{laptop.final_price}</td>
              <td>{laptop.savings}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default App;
