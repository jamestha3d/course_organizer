import CardGroup from 'react-bootstrap/CardGroup';
import TitleCard from '../components/TitleCard';
import { useState, useEffect } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';
import { getCourses, getApiEndPoint } from '../api';
import { Link } from 'react-router-dom';
import Loading from '../components/Loading';
function AllCohorts() {
    const [cohorts, setCohorts] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const getcohorts = async () => {
        const cohorts = await getApiEndPoint('cohorts')
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
            {isLoading ? <Loading/> : <>{cohorts.map((cohort, index) => (<TitleCard key={index} body={cohort.description} title={<Link to={`/cohorts/${cohort.guid}`}>{cohort.title}</Link>} instructor={cohort.instructor} />)
            )}</>}
        </CardGroup>
        ) : <><p>There are no Cohorts available for you at this time</p></>
    );
}

export default AllCohorts;


// import { Container } from "react-bootstrap";

// const AllCohorts = () => {
//     return ( 
//         <Container> 
//         <h1>All Cohorts</h1>
//         <p>This page displays all the cohorts that the user can view</p>
//         </Container>
//             );
// }
 
// export default AllCohorts;