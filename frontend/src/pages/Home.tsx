
import { useEffect, useState } from "react";
import { getCourses } from "../api";
import Navbar from "../components/Navbar";
import { UseAuthContext } from "../hooks/useAuthContext";
import TopNav from "../components/TopNav";
import Container from 'react-bootstrap/Container';
interface Props {
}



const Home = (props: Props) => {

    const [courses, setCourses] = useState<any>(null)
    const [isLoading, setIsLoading] = useState(true)
    const { user } = UseAuthContext()
    const [currentUser, setCurrentUser] = useState<any>(null)
    const getcourses = async () => {
        const courses: any = await getCourses()
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
                    <h5> My Courses</h5>
                    <ul>
                        {isLoading ? <> Courses Loading.. Please wait</> : <>{courses && courses.map((course: any, index: number) => (<li key={index}> {course.title}</li>))}</>}

                    </ul>

                    <h5> Explore other courses that may interest you</h5>

                    <span> Insert other courses for user here</span>

                </div>


            </div>
            </Container>

        </div>
    )
}

export default Home