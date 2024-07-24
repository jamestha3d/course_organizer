import { Container } from "react-bootstrap";
import { Link } from "react-router-dom";
const ActivateAccountWarning = () => {
    return ( <Container>
    <h1>Activate Account</h1>
    <p>You shall not pass! 😛</p>

    <p>Click the activation link in your email to activate your account.</p>
    <p>Click <Link to="#">here</Link> to resend the activation link!</p>
    </Container> );
}
 
export default ActivateAccountWarning;