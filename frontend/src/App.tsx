import { Col, Container, Row } from 'react-bootstrap';
import './App.css';
import Header from './components/Header';
import Home from './components/Home';
import LessonsList from './components/LessonsList';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from './components/Login';
import Signup from './components/Signup';
import { Footer } from './components/Footer';
import { useState } from 'react';
import useToken from './hooks/useToken';

function App() {

  const { token, setToken } = useToken();
  //const token: string = getToken();

  let user: boolean = true;
  if (!token) {
    //return <Login setToken={setToken} />
    user = false;
  }

  //const { user } = useAuthContext()

  return (
    <>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path='/' element={user ? <Home /> : <Navigate to="/login" />} //using Navigate to redirect
          />
          <Route path="/login" element={!user ? <Login /> : <Navigate to="/" />} />
          <Route path="/signup" element={!user ? <Signup /> : <Navigate to="/" />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;
