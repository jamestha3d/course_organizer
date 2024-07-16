

import { NavLink } from "react-router-dom"
import { useState } from 'react'
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Button from 'react-bootstrap/Button';
import * as FaIcons from "react-icons/fa";
import SignOutButton from "../components/buttons/SignOutButton";
import { useAuth } from "../utils/AuthContext";
//example from SideBar

const Layout = ({ children }) => {
    const {user} = useAuth()
    const APP_NAME= process.env.REACT_APP_NAME
    const [visible, setVisible] = useState(false)
    return (
        <>
        <Navbar expand="lg" className="bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand href="/">{APP_NAME}</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="/dashboard">Dashboard</Nav.Link>
            <Nav.Link href="/teach">Teach</Nav.Link>
            <NavDropdown title="Learning" id="navbarScrollingDropdown">
              <NavDropdown.Item href="/courses">My courses</NavDropdown.Item>
              <NavDropdown.Item href="/courses/all">
                All Courses
              </NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="/courses/recommended">
                Recommended
              </NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="/create">
              Create
            </Nav.Link>
          </Nav>
          <Nav.Link href="/notifications" disabled><FaIcons.FaBell/></Nav.Link>
          
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
            />
            <Button variant="outline-success">Search</Button>
          </Form>
          
          {user ? (
             <NavDropdown title="Me" id="navbarScrollingDropdown">
             <NavDropdown.Item href="/profile">Profile</NavDropdown.Item>
             <NavDropdown.Item href="/settings">
               Settings 
             </NavDropdown.Item>
             <NavDropdown.Divider />
             <NavDropdown.Item href="/login">
               <SignOutButton />
             </NavDropdown.Item>
           </NavDropdown>
          ) : (
            <Nav.Link href="/login">Log In</Nav.Link>
          )}
         

        </Navbar.Collapse>
      </Container>
    </Navbar>
        
        <main>{children}</main>
        </>
    );
}
export default Layout;