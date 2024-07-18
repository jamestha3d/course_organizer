import { Col, Container, Row } from 'react-bootstrap';
import './App.css';
import Home from './pages/Home';

import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom"
import Login from './pages/Login';
import Signup from './pages/Signup';
import useToken from './hooks/useToken';
import { UseAuthContext } from './hooks/useAuthContext';
import Dashboard from './pages/Dashboard';
//import Sidebar from './components/sidebar/Sidebar';
import Create from './pages/Create';
import Layout from './pages/Layout';
import AllCourses from './pages/AllCourses';
import AllCohorts from './pages/AllCohorts';
import { useState, useEffect } from 'react';
import PrivateRoutes from './utils/PrivateRoute';
import Courses from './components/Courses';
import { AuthProvider } from './utils/AuthContext';
import CohortDetail from './pages/CohortDetail';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Discussions from './pages/Discussions';
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
        //setLoggedInUser(user.user)
        if (user) {
            setLoggedInUser(user.user)
        }
        // else{
        //   setLoggedInUser(null)
        // }
        console.log('use effect ran', user, loggedInUser)

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
    <AuthProvider>
    <Router>
      <Layout>
        <Routes>
          
          {/* <Route path="/login" element={!user ? <Login /> : <Navigate to="/" />} /> */}
          <Route path="/login" element={<Login />}/>
          <Route path="/signup" element={!user ? <Signup /> : <Navigate to="/" />} />
          <Route path="/dashboard" element={loggedInUser ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="/create" element={loggedInUser ? <Create /> : <Navigate to="/login" />} />
          <Route path="/courses/all" element={loggedInUser ? <AllCourses /> : <Navigate to="/login" />} />
          <Route path="/cohorts/all" element={loggedInUser ? <AllCohorts /> : <Navigate to="/login" />} />
          <Route path="/cohorts/:guid" element={loggedInUser ? <CohortDetail /> : <Navigate to="/login" />} />
          <Route element={<PrivateRoutes/>}>
            <Route path='/' element={user ? <Home /> : <Navigate to="/login" />}/>
            <Route path="/courses" element={<Courses/>} />
            <Route path='/profile' element={<Profile/>}/>
            <Route path="/settings" element={<Settings/>} />
            <Route path="/discussions" element={<Discussions/>} />
            
          </Route>
          {/* This is an experimental feature so using for /courses only */}
          
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Layout>
    </Router >
    </AuthProvider>
          
  );
}

//Make sure log in and sign up return same data
export default App;
