import CardGroup from 'react-bootstrap/CardGroup';
import Course from './TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses } from '../api';

function Courses() {
    const [courses, setCourses] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const getcourses = async () => {
        const courses = await getCourses()
        setCourses(courses)
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
        <CardGroup>
            {isLoading ? <> Loading...</> : <>{courses.map((course, index) => (<Course key={index} img={'www.img'} body={course.description} title={course.title} instructor={course.instructor} />)
            )}</>}
        </CardGroup>
    );
}

export default Courses;