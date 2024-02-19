import { Container, Row, Col } from 'react-bootstrap'

export const Footer = () => {
    return (
        <footer>
            <Container>
                <Row>
                    <Col className="text-center py-3"> Copyright &copy; {process.env.REACT_APP_NAME}</Col>

                </Row>

            </Container>

        </footer>
    );
};

export default Footer