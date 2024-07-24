import { useParams } from "react-router-dom";
import { Container } from "react-bootstrap";
const ActivateAccount = () => {

    const {uid64, token} = useParams();

    //make a call to confirm account.
    //update user details in login/relog user in
    return ( <Container>
    <h1>Success! Account activated for {uid64} {token}</h1>

    
    </Container> );
}
 
export default ActivateAccount;