
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

        }, [user]

    )


    return (
        <div className="page">
            <Container>
            <Navbar />
            <TopNav title="Home" />
            {/* <h3> Home </h3> */}
            <br /> <hr />
            <div className="aaaa">

                <div className="aaa">
                    <div className={"aaa"}>

                    </div>
                    <div>This is the home page.</div>
                    {/* <h3> Courses</h3> */}
                    <ul>
                        {isLoading ? <> Courses Loading.. Please wait</> : <>{courses && courses.map((course: any, index: number) => (<li key={index}> {course.title}</li>))}</>}

                    </ul>

                </div>


            </div>
            </Container>

        </div>
    )
}

export default Home