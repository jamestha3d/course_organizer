import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from '../components/TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApi } from '../api';
import Loading from '../components/Loading';
import { useParams } from 'react-router-dom';
import Classroom from '../components/Classroom';
const ClassroomDetail = () => {
    const [classroom, setClassroom] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const {guid} = useParams();
    const getclassroom = async () => {
        const classroom = await getApi(`classrooms/${guid}`)
        if (classroom){
            setClassroom(classroom)
        }
        
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getclassroom()
            }

        }, [])

    console.log(classroom)
    return (
        classroom ? 
        (
        <>
            {isLoading ? <Loading/> : <><Classroom title={classroom.title} instructors={classroom.instructors} start_date={classroom.start_date} end_date={classroom.end_date} courses={classroom.courses} is_instructor={classroom.is_instructor} is_student={classroom.is_student} students_count={classroom.students_count} guid={guid}/></>}
        </>
        ) : isLoading? <Loading /> : <p>You have no registered courses</p>
    );
}
 
export default ClassroomDetail;



// function MyCourses() {
    

// export default MyCourses;