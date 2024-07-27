import { useParams } from "react-router-dom";
import { Container } from "react-bootstrap";
import { useState, useEffect } from "react";
import { postApi} from "../api";
import Loading from "../components/Loading";
import { UseAuthContext } from "../hooks/useAuthContext";

const ActivateAccount = () => {
    const [activated, setActivated] = useState(false);
    const [loading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);
    const [redirecting, setRedirecting] = useState(null);
    const {uid64, token} = useParams();
    const { dispatch } = UseAuthContext()

    const activateUser = async (uid64, token) => {
        const response = await postApi(`auth/activate/${uid64}/${token}/`)
        //const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
        setIsLoading(false)
        if (response.data.error){
            //inform user of this error
            const error = response.data.error
            setError(error)
        }
        else if (response.status == 200){
            setActivated(true)
            //wait 3 seconds and redirect.
            //await delay (3000)
            setTimeout(() => {
                const json = response.data
                localStorage.setItem('user', JSON.stringify(json))
                dispatch({ type: 'LOGIN', payload: json })
            }, 3000);
            

        } else {
            //give error message
            setError(response.error)
        }
        
    }
    
    useEffect( ()=> {
        //activate account
        activateUser(uid64, token)

    }, [])

    return () => {
        setError(null) //added clean up function to prevent wrong errors??
    }
    return ( 
        error ? 
        <Container> 
            <h1>Error!</h1>
            <p>{error}</p>
        </Container>
        :
    
        <Container>
            
            {loading ? <Loading/> : (activated ? <><h1>Success!</h1> <p>Account activation success. Log in If not automatically redirected. <br/><Loading/></p></> : <><h1>Failure</h1> <p>Could not activate your account</p></>)}
        
        </Container>
);
}
 
export default ActivateAccount;