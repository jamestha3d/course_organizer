

import { NavLink } from "react-router-dom"
import { useState } from 'react'
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Button from 'react-bootstrap/Button';
import * as FaIcons from "react-icons/fa"
//example from SideBar

const Layout = ({ children }) => {
    
    const APP_NAME= process.env.REACT_APP_NAME
    const [visible, setVisible] = useState(false)
    return (
        <>
        <Navbar expand="lg" className="bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand href="#">{APP_NAME}</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="/dashboard">Dashboard</Nav.Link>
            {/* <NavLink to="dashboard" className={("sidebar-link")} activeclassname="active"> Dashboard</NavLink>
            <Nav className="mr-auto">
                <NavLink to="/dashboard" className={("sidebar-link")} activeclassname="active"> Dashboard</NavLink>
            </Nav> */}
            <Nav.Link href="/assignments">Assignments</Nav.Link>
            <NavDropdown title="Courses" id="navbarScrollingDropdown">
              <NavDropdown.Item href="/courses">My courses</NavDropdown.Item>
              <NavDropdown.Item href="/courses/all">
                All Courses
              </NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="/courses/recommended">
                Recommended
              </NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="/" disabled>
              Link
            </Nav.Link>
          </Nav>
          <Nav.Link href="dashboard"><FaIcons.FaBell/></Nav.Link>
          
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
            />
            <Button variant="outline-success">Search</Button>
          </Form>
          

          <NavDropdown title="Me" id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action3">Profile</NavDropdown.Item>
              <NavDropdown.Item href="#action4">
                Settings 
              </NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action5">
                Sign Out
              </NavDropdown.Item>
            </NavDropdown>

            {/* <NavLink to="dashboard" className={("sidebar-link")} activeclassname="active"></NavLink> */}
        </Navbar.Collapse>
      </Container>
    </Navbar>
        
        <main>{children}</main>
        </>
    );
}
export default Layout;