import { Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import { postApiUser } from "../api";
import { useState, useRef, useEffect } from "react";
import { UseAuthContext } from "../hooks/useAuthContext";
import { ToastContainer, toast} from "react-toastify";
import { useNavigate } from "react-router-dom";
const ActivateAccountWarning = () => {
    const [hasToWait, setHasToWait] = useState(false)
    const countdownRef = useRef(null);
    const {user} = UseAuthContext();
    // const [activated, setActivated] = useState(user.user.activated)
    const sendActivation = async () => {
        setHasToWait(true)
        await postApiUser(`auth/send_activation/`)
        let countdown = 60;
        if (countdownRef.current) {
            countdownRef.current.style.display = 'block';
            countdownRef.current.innerText = `Resend available in ${countdown} seconds`;
        }
        const countdownInterval = setInterval(() => {
            countdown -= 1;
            if (countdownRef.current) {
                countdownRef.current.innerText = `Resend available in ${countdown} seconds`;
            }

            // When countdown reaches zero, re-enable the button and stop the interval
            if (countdown <= 0) {
                clearInterval(countdownInterval);
                if (countdownRef.current) {
                    countdownRef.current.style.display = 'none';
                }
                setHasToWait(false);
            }
    }, 1000);
    }

    // TODO: will work on this later. not needed rn 
    // const navigate = useNavigate()
    // useEffect( ()=> {
    //     //page should reload when user activation changes
    //     //Toast user that they have successfully activated
    //     if (user.user.activated){
    //         toast.success("Account activated")
    //         setTimeout(() => {
    //         }, 2000);
    //         if (user.user.activated) {
    //             navigate('/')
    //         }
    //     }
    //     // setActivated(true)
        

    // }, [user.user.activated]) //user does not change.

    
    
    // TODO: issues with this view.
    //when there is a user, react router just ignores the link and takes you to the user. maybe i want to log the user out.

    return ( <Container>
    <h1>Activate Account</h1>
    <p>You shall not pass! 😛</p>

    <p>Click the activation link in your email: {user.user.email} to activate your account.</p>
    <p>Click <button to="#" onClick={sendActivation} disabled={hasToWait}>here</button> to resend the activation link!</p>
    <div style={{'display': hasToWait ? 'block' : 'none'}}>
        <p>Activation Link has been sent to your email. Please wait 1 minute before retrying.</p>
        <p><span ref={countdownRef}></span></p>
    </div>
    <ToastContainer/>
    </Container> );
}
 
export default ActivateAccountWarning;