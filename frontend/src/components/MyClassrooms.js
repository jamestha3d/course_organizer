import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from './TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApiEndPoint } from '../api';
import { Link } from 'react-router-dom';
import Loading from './Loading';
function MyClassrooms() {
    const [classrooms, setClassrooms] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const getclassrooms = async () => {
        const classrooms = await getApiEndPoint('classrooms/myclassrooms')
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
        classrooms.length  ? 
        (
        <CardGroup>
            {isLoading ? <Loading/> : <>{classrooms.map((classroom, index) => (<TitleCard key={index} body={classroom.start_date} title={classroom.title} instructor={classroom.instructor} link={`/classrooms/${classroom.guid}`}/>)
            )}</>}
        </CardGroup>
        ) : (isLoading ? <Loading/> : <><p>You have no registered Classrooms. Click <Link to='/classrooms/all'>here</Link> to find Public Classrooms to Join For Free</p></>)
    );
}

export default MyClassrooms;