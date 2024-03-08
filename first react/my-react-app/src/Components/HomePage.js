import React from 'react';
import { Link } from 'react-router-dom';
import Dashboard from './Dashboard';

function HomePage() {
  return (
       <div>
      <h2>Welcome to BensonXSteve Suite Banking System</h2>
      <p>
        Thank you for choosing our banking system. To get started, please go to
        the{' '}
        <Link to="/dashboard" style={{ fontWeight: 'bold', color: 'blue' }}>
          Dashboard
        </Link>
        .
      </p>
      <p>
        If you don't have an account yet, you can{' '}
        <Link to="/register" style={{ fontWeight: 'bold', color: 'green' }}>
          register here
        </Link>
        .
      </p>
      <p>
        Already have an account?{' '}
        <Link to="/login" style={{ fontWeight: 'bold', color: 'red' }}>
          Login here
        </Link>
        .
      </p>
      <Dashboard />
      {/* Add other components or content here */}
    </div>
  );
}

export default HomePage;