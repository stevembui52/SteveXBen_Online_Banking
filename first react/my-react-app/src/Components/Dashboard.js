import React from 'react';

function Dashboard() {
  return (
    <div>
      <h3>Dashboard</h3>
      <p>Welcome to your banking dashboard. Here's some information:</p>
      <ul>
        <li>Account Balance: $5,000.00</li>
        <li>Recent Transactions:</li>
        <ul>
          <li>Transaction 1: -$100.00</li>
          <li>Transaction 2: +$200.00</li>
          <li>Transaction 3: -$50.00</li>
        </ul>
      </ul>
    </div>
  );
}

export default Dashboard;