import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from '../components/TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApi } from '../api';
import Loading from '../components/Loading';
import { useParams } from 'react-router-dom';
import Course from '../components/Course';
const CourseDetail = () => {
    const [course, setCourse] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const {guid} = useParams();
    const getcourse = async () => {
        const course = await getApi(`courses/${guid}`)
        if (course){
            setCourse(course)
        }
        
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getcourse()
            }

        }, [])

    console.log(course)
    return (
        course ? 
        (
        <>
            {isLoading ? <Loading/> : <><Course course={course}/></>}
        </>
        ) : isLoading? <Loading /> : <p>You have no registered courses</p>
    );
}
 
export default CourseDetail;



// function MyCourses() {
    

// export default MyCourses;