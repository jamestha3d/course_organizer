import { Container } from "react-bootstrap";
import { UseAuthContext } from "../hooks/useAuthContext";
const Profile = () => {
    const {user} = UseAuthContext()
    console.log(user)
    return ( <Container>
        <h3> User Profile</h3>
        {user && <p> User {user.user.email} is making changes</p>}
    </Container> );
}
 
export default Profile;