import { Container } from "react-bootstrap";
import { Link } from "react-router-dom";
const Teach = () => {
    return ( <Container>
        <h1> Teach </h1>
        <hr/>
        <p> Handle your Teaching</p>
       <Link to='/create/course'> <button> Create Course</button></Link>
       <Link to='/create/lesson'><button> Create Lesson</button></Link>

    </Container> );
}
 
export default Teach;