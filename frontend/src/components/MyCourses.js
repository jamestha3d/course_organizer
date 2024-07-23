import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from './TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApiEndPoint } from '../api';
import Loading from './Loading';

function MyCourses() {
    const [courses, setCourses] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const getcourses = async () => {
        const courses = await getApiEndPoint('courses/mycourses')
        if (courses){
            setCourses(courses)
        }
        
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getcourses()
            }

        }, []




    )
    return (
        courses.length  ? 
        (
        <CardGroup>
            {isLoading ? <Loading/> : <>{courses.map((course, index) => (<TitleCard key={index} body={course.description} title={course.title} instructor={course.instructor} link={`/courses/${course.guid}`}/>)
            )}</>}
        </CardGroup>
        ) : isLoading? <Loading /> : <p>You have no registered courses</p>
    );
}

export default MyCourses;