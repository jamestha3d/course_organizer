import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from '../components/TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApiEndPoint } from '../api';
import { Link } from 'react-router-dom';
import Loading from '../components/Loading';
import BreadCrumb from '../components/Breadcrumb';
import { Container } from 'react-bootstrap';
function AllClassrooms() {
    const [classrooms, setClassrooms] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const getclassrooms = async () => {
        const classrooms = await getApiEndPoint('classrooms')
        if (classrooms){
            setClassrooms(classrooms)
        }
        
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getclassrooms()
            }

        }, []




    )
    return (
        <Container>
        <BreadCrumb />

        <Link to="#"> Create New</Link>
        <br/> <hr/>
        {classrooms.length  ? 
        (
        <CardGroup>
            
            {isLoading ? <Loading/> : <>{classrooms.map((classroom, index) => (<TitleCard key={index} body={classroom.description} title={<Link to={`/classrooms/${classroom.guid}`}>{classroom.title}</Link>} instructor={classroom.instructor} />)
            )}</>}
        </CardGroup>
        ) : <><p>There are no Classrooms available for you at this time</p></>}
        </Container>
    );
}

export default AllClassrooms;


// import { Container } from "react-bootstrap";

// const AllClassrooms = () => {
//     return ( 
//         <Container> 
//         <h1>All Classrooms</h1>
//         <p>This page displays all the classrooms that the user can view</p>
//         </Container>
//             );
// }
 
// export default AllClassrooms;