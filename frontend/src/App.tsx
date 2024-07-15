import { Col, Container, Row } from 'react-bootstrap';
import './App.css';
import Home from './pages/Home';

import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from './pages/Login';
import Signup from './pages/Signup';
import useToken from './hooks/useToken';
import { UseAuthContext } from './hooks/useAuthContext';
import Dashboard from './pages/Dashboard';
//import Sidebar from './components/sidebar/Sidebar';
import Create from './pages/Create';
import Layout from './pages/Layout';
import { useState, useEffect } from 'react';

function App() {
  const { token, setToken } = useToken();
  const [loggedInUser, setLoggedInUser] = useState(UseAuthContext())
  //let user: boolean = true;
  if (!token) {
    //return <Login setToken={setToken} />
    //user = false;
  }

  const { user } = UseAuthContext()
  
  useEffect(
    () => {
        if (user) {
            setLoggedInUser(user)
        }

    }, [user]

)

  // user ? console.log('USER') : console.log('NO USERRRR')
  // const user = JSON.parse(localStorage.getItem('user'))

  const NotFound = () => (
    <div className="page">
      <span style={{ "textAlign": "center" }}>Oops, what you are looking for, does not exist.</span>
    </div>
  );

  return (
    <BrowserRouter>
      {/* <Sidebar> */}
      <Layout>
        <Routes>
          <Route path='/' element={user ? <Home /> : <Navigate to="/login" />}
          />
          <Route path="/login" element={!user ? <Login /> : <Navigate to="/" />} />
          <Route path="/signup" element={!user ? <Signup /> : <Navigate to="/" />} />
          <Route path="/dashboard" element={loggedInUser ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="/create" element={user ? <Create /> : <Navigate to="/login" />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      {/* </Sidebar> */}
      </Layout>
    </BrowserRouter >
  );
}

export default App;
