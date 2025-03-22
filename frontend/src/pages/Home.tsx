
import { useEffect, useState } from "react";
import { getCourses, getApiEndPoint } from "../api";
import Navbar from "../components/Navbar";
import { UseAuthContext } from "../hooks/useAuthContext";
import TopNav from "../components/TopNav";
import Container from 'react-bootstrap/Container';
import Loading from "../components/Loading";
interface Props {
}



const Home = (props: Props) => {

    const [courses, setCourses] = useState<any>(null)
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const [currentUser, setCurrentUser] = useState<any>(null)
    const getcourses = async () => {
        // const courses: any = await getCourses()
        const courses: any = await getApiEndPoint('courses?limit=3')
        setCourses(courses)
        setIsLoading(false)

    }

    useEffect(
        () => {
            if (user) {
                getcourses()
            }
            setCurrentUser(user.user)
        }, [user]

    )

    return (
        <div className="page">
            <Container>
            <br /> 
            <h2> Welcome, <span style={{color:'grey'}}> {currentUser?.email}</span> </h2>
            <hr />
            <div className="">

                <div className="">
                    <div className={""}>

                    </div>
                    <div><h6> Start learning or continue a course. . .</h6></div>
                    <h5> My Recent Courses</h5>
                    <ul>
                        {isLoading ? <> <Loading/></> : <>{courses && courses.map((course: any, index: number) => (<li key={index}> {course.title}</li>))}</>}

                    </ul>

                    <br/>
                    <h5> Explore other courses that may interest you</h5>

                    <p> See All Courses...</p>

                   

                </div>


            </div>
            </Container>

        </div>
    )
}

export default Home