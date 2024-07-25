import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const LoginRedirect = () => {
  const history = useHistory();

  useEffect(() => {
    // Assume that the server sets a cookie on successful login
    // You can check for the cookie or perform a request to verify the login state
    axios.get('/api/verify-login')
      .then(response => {
        if (response.data.logged_in) {
          // Redirect to the dashboard or home page
          history.push('/dashboard');
        } else {
          // Redirect to the login page or show an error
          history.push('/login');
        }
      })
      .catch(error => {
        console.error('Login verification failed:', error);
        history.push('/login');
      });
  }, [history]);

  return <div>Redirecting...</div>;
};

export default LoginRedirect;