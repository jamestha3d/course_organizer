import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from './TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApiEndPoint } from '../api';
import { Link } from 'react-router-dom';
import Loading from './Loading';
function MyCohorts() {
    const [cohorts, setCohorts] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const getcohorts = async () => {
        const cohorts = await getApiEndPoint('cohorts/mycohorts')
        if (cohorts){
            setCohorts(cohorts)
        }
        
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getcohorts()
            }

        }, []




    )
    return (
        cohorts.length  ? 
        (
        <CardGroup>
            {isLoading ? <Loading/> : <>{cohorts.map((cohort, index) => (<TitleCard key={index} body={cohort.start_date} title={cohort.title} instructor={cohort.instructor} />)
            )}</>}
        </CardGroup>
        ) : (isLoading ? <Loading/> : <><p>You have no registered Cohorts. Click <Link to='/cohorts/all'>here</Link> to find Public Cohorts to Join For Free</p></>)
    );
}

export default MyCohorts;