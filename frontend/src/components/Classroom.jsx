import { Link } from "react-router-dom";
import { Container } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import { postApiEndPoint } from "../api";
import { useState } from "react";
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Classroom = ({title, instructors, courses, start_date, end_date, is_student, is_instructor, students_count, guid, ...rest}) => {

    const [isStudent, setIsStudent] = useState(is_student)
    // const toggleIsStudent = () => setIsStudent(!isStudent)
    const [students, setStudents] = useState(students_count)
    const joinClassroom = async () => {
        const response = await postApiEndPoint(`classrooms/${guid}/join/`)
        if (response.length === 0) {
            toast.error('Something went wrong! Please try again.')
        }
        else{
            const data = response.data
            toast.success('You are now enrolled!')
            //toggleIsStudent()
            console.log(data)
            console.log(data.is_student)
            console.log(data.students_count)
            setIsStudent(data.is_student)
            setStudents(data.students_count)
        }

    }

    const leaveClassroom = async () => {
        const response = await postApiEndPoint(`classrooms/${guid}/leave/`)
        if (response.length === 0) {
            toast.error('Something went wrong! Please try again.')
        }
        else{
            const data = response.data
            console.log(data)
            console.log(data.is_student)
            console.log(data.students_count)
            toast.success('You left successfully!')
            //toggleIsStudent()
            setIsStudent(data.is_student)
            setStudents(data.students_count)
        }
        
    }

    //There should be more details about the classroom on this page. number of students. ratings.

    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const startDate = start_date ? new Date(start_date) : start_date
    const endDate = end_date ? new Date(end_date) : end_date
    return ( <Container>
        <br/>
        <h3> {title} </h3>
        <hr/>
        <p><b>Title</b>: {title} </p>
        <p><b>Duration</b>: {startDate?.toLocaleDateString(undefined, options)} - {endDate ? endDate.toLocaleDateString(undefined, options) : <span style={{color:'grey'}}>No end date set</span>} </p>

        <p><b>instructors</b>: {instructors} </p>
        <p><b>courses</b>: {courses?.join(', ')} </p>
        <p><b>students</b>: {students} </p>
        
        <p> {isStudent ? <span> You are enrolled to this Classroom. </span> : <span> You are not enrolled!</span>}</p>
        {/* clicking the enroll/leave button should bring up a modal to confirm your enrollment */}
        <p> {isStudent ? <Button onClick={leaveClassroom} variant="danger"> Leave</Button> : <Button onClick={joinClassroom} variant="primary"> Enroll!</Button>}</p>

        <hr/>
        <h3>Other stats</h3>
        <p>We should see:</p>
        <ul>
            <li> Assignments: pending and previous</li>
            <li> Courses: click on individual course to see the next schedule</li>
            <li> Time table</li>
            <li> Lessons: Upcoming and previous.</li>
        </ul>
        <ToastContainer />
    </Container> );
}
 
export default Classroom;