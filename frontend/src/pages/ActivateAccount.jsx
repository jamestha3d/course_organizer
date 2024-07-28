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
    const {uid64, token} = useParams();
    const { user, dispatch } = UseAuthContext()
    const [alreadyfired, setAlreadyFired] = useState(false)
    const activateUser = async (uid64, token) => {
        const response = await postApi(`auth/activate/${uid64}/${token}/`)
        //const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
        setIsLoading(false)
        if (response.status == 200){
            setActivated(true)
            // setAlreadyFired(true)
            //wait 3 seconds and redirect.
            //await delay (3000)
            setTimeout(() => {
                const json = response.data
                localStorage.setItem('user', JSON.stringify(json))
                dispatch({ type: 'LOGIN', payload: json })
            }, 3000);
            

        } else if (!alreadyfired && response.data.error ){
            //inform user of this error
            const error = response.data.error
            setError(error)
        }
        else {
            //give error message
            setError(response.error)
        }
        
    }
    //activateUser(uid64, token)
    useEffect( ()=> {
        //activate account
        if (!alreadyfired){
            activateUser(uid64, token)
        }
        // setAlreadyFired(true)
        return (() => {
            setError(null)
            setAlreadyFired(true)
        })
        
    }, [])

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