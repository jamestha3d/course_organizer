import { useState } from "react";
import { Container } from "react-bootstrap";
import { Link } from "react-router-dom";
import { postApiUser } from "../api";
import { useNavigate } from "react-router-dom";
import Loading from "../components/Loading";
const CreateInstructorProfile = () => {
    const [loading, setLoading] = useState(false)
    const handleLinkAccount = async () => {
        setLoading(true)
        const response = await postApiUser(`api/oauth2init/`)

        if (response.status === 200) {
            const jwt_token = response.data.state_token
            localStorage.setItem('google_oauth_state_token', jwt_token)
            //window.location.href = response.data.auth_url
            const width = 600;
            const height = 800;
            const left = (window.screen.width / 2) - (width / 2);
            const top = (window.screen.height / 2) - (height / 2);

            window.open(response.data.auth_url, 'GoogleAuth', `width=${width},height=${height},top=${top},left=${left}`);

            }

    // useEffect(()=> {
    //     const urlParams = new URLSearchParams(window.location.search);
    //     const token = urlParams.get('token');
    // })
    }
    return ( <Container>
        <h1>Create an instructor Profile</h1>
        <p>This gives you access to create courses and share with students. We offer very flexible options to ensure you make the most of our resources.</p>
        
        <h4>Google Meet</h4>
        <p>Google meet is a video conferencing app that allows people to make calls. You can use this option to handle classes with your students. Premium Google Meet users can record their meetings.</p>

        <p>Link Your Google account with our app so we can help you manage your Meetings, Recordings, and even calendar events so your students are always in the loop!</p>

        <hr/>
        <h3>Connect your google account to CourseConnect</h3>
        <p> Do you want us to automatically handle scheduling of meetings?</p>
        <p>We will never use your data for anything other than creating meetings/calendars/retrieving recorded classes.</p>
        <p>Click <Link to="#" onClick={handleLinkAccount}>here</Link> to connect your account</p>
        {loading && <Loading/>}
        {/* <ul>
            <li>You will need to connect Your google account here</li>
        
        </ul> */}
    </Container> );
}
 
export default CreateInstructorProfile;