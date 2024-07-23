import { Container } from "react-bootstrap";

const Course = ({course}) => {
    //This page should have 
    return ( <Container>
        <h1>Course</h1>
        <p><b>title</b>: {course.title}</p>
        <p><b>code</b>: {course.code}</p>
        <p><b>description</b>: {course.description}</p>
        <p><b>instructors</b>: {course.instructors}</p>

        <hr/>
        <h5>Upcoming lessons</h5>

        <ul>
            <li>insert upcoming lessons here</li>
            <li>pending assignments</li>
            <li>classwork and more</li>
        </ul> 
        
    </Container> );
}
 
export default Course;