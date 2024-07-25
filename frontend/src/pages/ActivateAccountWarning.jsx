import { Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import { postApiUser } from "../api";
import { useState, useRef } from "react";
import { UseAuthContext } from "../hooks/useAuthContext";

const ActivateAccountWarning = () => {
    const [hasToWait, setHasToWait] = useState(false)
    const countdownRef = useRef(null);
    const {user} = UseAuthContext()
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
    return ( <Container>
    <h1>Activate Account</h1>
    <p>You shall not pass! 😛</p>

    <p>Click the activation link in your email: {user.user.email} to activate your account.</p>
    <p>Click <button to="#" onClick={sendActivation} disabled={hasToWait}>here</button> to resend the activation link!</p>
    <div style={{'display': hasToWait ? 'block' : 'none'}}>
        <p>Activation Link has been sent to your email. Please wait 1 minute before retrying.</p>
        <p><span ref={countdownRef}></span></p>
    </div>

    </Container> );
}
 
export default ActivateAccountWarning;