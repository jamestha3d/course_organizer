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
import AllClassrooms from './pages/AllClassrooms';
import { useState, useEffect } from 'react';
import PrivateRoutes from './utils/PrivateRoute';
import Courses from './components/Courses';
import { AuthProvider } from './utils/AuthContext';
import ClassroomDetail from './pages/ClassroomDetail';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Discussions from './pages/Discussions';
import Teach from './pages/Teach';
import CreateCourse from './pages/CreateCourse';
import CreateLesson from './pages/CreateLesson';
import CourseDetail from './pages/CourseDetail';
import ActivateAccountWarning from './pages/ActivateAccountWarning';
import ActivateAccount from './pages/ActivateAccount';
import { useNavigate } from 'react-router-dom';
import CreateClassroom from './pages/CreateClassroom';
import CreateInstructorProfile from './pages/CreateInstructorProfile';
function App() {
  const { token, setToken } = useToken();

  if (!token) {
    //return <Login setToken={setToken} />
    //user = false;
  }

  const { user } = UseAuthContext()
  const [count, setCount] = useState(0)
//   useEffect(
//     () => {
//       console.log('useeffect running')
//       console.log('user is', user)
//     }, [user]

// )

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
          
          <Route path="/login" element={!user ? <Login /> : <Navigate to="/" />} />
          <Route path="/signup" element={!user ? <Signup /> : <Navigate to="/" />} />
          {/* <Route path="/dashboard" element={user ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="/create" element={user ? <Create /> : <Navigate to="/login" />} />
          <Route path="/courses/all" element={user ? <AllCourses /> : <Navigate to="/login" />} />
          <Route path="/classrooms/all" element={user? <AllClassrooms /> : <Navigate to="/login" />} />
          <Route path="/classrooms/:guid" element={user ? <ClassroomDetail /> : <Navigate to="/login" />} /> */}
          <Route path="/activate" element={user ? (!user.user.activated ? <ActivateAccountWarning/> : <Navigate to="/" />) : <Navigate to="/login" />} />
          <Route path="/activate/:uid64/:token" element={user ? (!user.user.activated ? <ActivateAccount/> : <Navigate to="/" />): <ActivateAccount/>} />
          <Route element={<PrivateRoutes/>}>
            <Route path='/' element={user ? (user.user.activated ? <Home /> : <Navigate to="/activate"/>) : <Navigate to="/login" />}/>
            <Route path="/courses" element={<Courses/>} />
            <Route path='/profile' element={<Profile/>}/>
            <Route path="/settings" element={<Settings/>} />
            <Route path="/discussions" element={<Discussions/>} />
            <Route path="/teach" element={<Teach/>} />
            <Route path="/create/course" element={<CreateCourse/>} />
            <Route path="/create/lesson" element={<CreateLesson/>} />
            <Route path="/create/classroom" element={<CreateClassroom/>} />
            <Route path="/courses/:guid" element={<CourseDetail/>} />
            <Route path="/dashboard" element={<Dashboard /> } />
            <Route path="/create" element={<Create />}  />
            <Route path="/courses/all" element={<AllCourses />} />
            <Route path="/classrooms/all" element={<AllClassrooms /> } />
            <Route path="/classrooms/:guid" element={<ClassroomDetail /> } />
            <Route path="/become-instructor" element={<CreateInstructorProfile/> } />
            {/* <Route path="/" element={}/> */}
          </Route>
          {/* This is an experimental feature so using for /courses only localhost:3000/oauth2 */}
          
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Layout>
    </Router >
    </AuthProvider>
          
  );
}

//Make sure log in and sign up return same data
export default App;
