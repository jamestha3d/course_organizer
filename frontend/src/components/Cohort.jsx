import { Link } from "react-router-dom";
import { dateToDay } from "../utils/utils";
import { Container } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import { postApiEndPoint } from "../api";
import { useState } from "react";
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
const Cohort = ({title, instructors, courses, start_date, end_date, is_student, is_instructor, guid, ...rest}) => {

    const [response, setResponse] = useState(''); //using this just to rerender after response
    const toggleEnrollment = () => {
        console.log('clicked')
    }

    const joinCohort = async () => {
        try {
            const response = await postApiEndPoint(`cohorts/${guid}/join/`)
            console.log(response)
            
            toast.success('You are now enrolled!')
            setResponse(response.data)
            
        } catch (error) {
            console.error('Error joining cohort:', error)
        }
        
    }

    const leaveCohort = async () => {
        try {
            const response = await postApiEndPoint(`cohorts/${guid}/leave/`)
            console.log(response)
            
            toast.success('You left successfully!')
            setResponse(response.data)
            
        } catch (error) {
            console.error('Error Leaving cohort:', error)
        }
        
    }
    return ( <Container>
        <br/>
        <h3> {title} </h3>
        <hr/>
        <p><b>Title</b>: {title} </p>
        <p><b>Duration</b>: {start_date} to {end_date} </p>
        <p><b>instructors</b>: {instructors} </p>
        <p><b>courses</b>: {courses.join(', ')} </p>

        <p> {is_student ? <span> You are enrolled to this Cohort. </span> : <span> You are not enrolled!</span>}</p>
        {/* clicking the enroll/leave button should bring up a modal to confirm your enrollment */}
        <p> {is_student ? <Button onClick={leaveCohort} variant="danger"> Leave</Button> : <Button onClick={joinCohort} variant="primary"> Enroll!</Button>}</p>
        <ToastContainer />
    </Container> );
}
 
export default Cohort;