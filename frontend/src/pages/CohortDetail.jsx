import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from '../components/TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApi } from '../api';
import Loading from '../components/Loading';
import { useParams } from 'react-router-dom';
import Cohort from '../components/Cohort';
const CohortDetail = () => {
    const [cohort, setCohort] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const {guid} = useParams();
    const getcohort = async () => {
        const cohort = await getApi(`cohorts/${guid}`)
        if (cohort){
            setCohort(cohort)
        }
        
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getcohort()
            }

        }, [])

    console.log(cohort)
    return (
        cohort ? 
        (
        <>
            {isLoading ? <Loading/> : <><Cohort title={cohort.title} instructors={cohort.instructors} start_date={cohort.start_date} end_date={cohort.end_date} courses={cohort.courses} is_instructor={cohort.is_instructor} is_student={cohort.is_student} students_count={cohort.students_count} guid={guid}/></>}
        </>
        ) : isLoading? <Loading /> : <p>You have no registered courses</p>
    );
}
 
export default CohortDetail;



// function MyCourses() {
    

// export default MyCourses;