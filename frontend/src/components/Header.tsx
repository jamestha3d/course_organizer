import * as React from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';
import { Lesson } from '../models/lesson.model';
import { LinkContainer } from 'react-router-bootstrap';
import { UseAuthContext } from '../hooks/useAuthContext';
import { useLogout } from '../hooks/useLogout';
interface IHeaderProps {
    lessons?: Lesson[]
}

// const Header: React.FunctionComponent<IHeaderProps> = ({ lessons }) => {
//     return (
//         <div>
//             <Navbar fixed="top" bg="dark" variant="dark">
//                 <Container>
//                     <Navbar.Brand>
//                         {process.env.REACT_APP_NAME}

//                     </Navbar.Brand>
//                 </Container>
//             </Navbar>
//         </div>
//     );
// };

// export default Header;

function Header() {

    const { user } = UseAuthContext()
    const { logout } = useLogout()
    return (

        <header>
            <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
                <Container>
                    <LinkContainer to='/'>
                        <Navbar.Brand>{process.env.REACT_APP_NAME}</Navbar.Brand>
                    </LinkContainer>

                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                            <LinkContainer to='/'>
                                <Nav.Link><i className="fas fa-shopping-cart"></i>Home</Nav.Link>
                            </LinkContainer>
                            {user ?
                                <>
                                    <LinkContainer to='/dashboard'>
                                        <Nav.Link><i className="fas fa-user"></i>Dashboard</Nav.Link>
                                    </LinkContainer>
                                    <LinkContainer to='/'>
                                        <Nav.Link onClick={() => logout()}><i className="fas fa-user"></i>Logout</Nav.Link>
                                    </LinkContainer>
                                </>
                                :
                                <>
                                    <LinkContainer to='/login'>
                                        <Nav.Link><i className="fas fa-user"></i>Login</Nav.Link>
                                    </LinkContainer>
                                    <LinkContainer to='/signup'>
                                        <Nav.Link><i className="fas fa-user"></i>Signup</Nav.Link>
                                    </LinkContainer>
                                </>
                            }

                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>

    )
}
export default Header;