import { Col, Container, Row } from 'react-bootstrap';
import './App.css';
import Home from './components/Home';

import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from './components/Login';
import Signup from './components/Signup';
import useToken from './hooks/useToken';
import { UseAuthContext } from './hooks/useAuthContext';
import Dashboard from './pages/Dashboard';
import Sidebar from './components/sidebar/Sidebar';


function App() {
  const { token, setToken } = useToken();

  //let user: boolean = true;
  if (!token) {
    //return <Login setToken={setToken} />
    //user = false;
  }

  const { user } = UseAuthContext()

  const NotFound = () => (
    <div className="text-center">
      Oops, what you are looking for, does not exist.
    </div>
  );

  return (
    <BrowserRouter>
      <Sidebar>
        <Routes>
          <Route path='/' element={user ? <Home /> : <Navigate to="/login" />}
          />
          <Route path="/login" element={!user ? <Login /> : <Navigate to="/" />} />
          <Route path="/signup" element={!user ? <Signup /> : <Navigate to="/" />} />
          <Route path="/dashboard" element={user ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Sidebar>
    </BrowserRouter >
  );
}

export default App;
