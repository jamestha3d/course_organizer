import * as React from 'react';
import { Container, Navbar } from 'react-bootstrap'
import { Lesson } from '../models/lesson.model';
interface IHeaderProps {
    lessons?: Lesson[]
}

const Header: React.FunctionComponent<IHeaderProps> = ({ lessons }) => {
    return (
        <div>
            <Navbar fixed="top" bg="dark" variant="dark">
                <Container>
                    <Navbar.Brand>
                        {process.env.REACT_APP_NAME}

                    </Navbar.Brand>
                </Container>
            </Navbar>
        </div>
    );
};

export default Header;
