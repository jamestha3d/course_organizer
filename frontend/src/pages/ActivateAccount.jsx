import { useParams } from "react-router-dom";
import { Container } from "react-bootstrap";
import { useState, useEffect } from "react";
import { postApi} from "../api";
import Loading from "../components/Loading";
const ActivateAccount = () => {
    const [activated, setActivated] = useState(false);
    const [loading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);
    const {uid64, token} = useParams();

    const activateUser = async (uid64, token) => {
        const response = await postApi(`auth/activate/${uid64}/${token}/`)
        if (response.data.error){
            //inform user of this error
            const error = response.data.error
            setError(error)
        }
        else if (response.status == 200){
            //give success message
            //LogUserIn
            setActivated(true)

        } else {
            //give error message
            setError(response.error)
        }
        
    }
    useEffect( ()=> {
        //activate account
        activateUser(uid64, token)
        setIsLoading(false)
        //log user in
    }, [])

    return ( 
        error ? 
        <Container> 
            <h1>Error!</h1>
            <p>{error}</p>
        </Container>
        :
    
        <Container>
            
            {loading ? <Loading/> : (activated ? <><h1>Success!</h1> <p>Account activation success. Log in If not automatically redirected.</p></> : <><h1>Failure</h1> <p>Could not activate your account</p></>)}
        
        </Container>
);
}
 
export default ActivateAccount;