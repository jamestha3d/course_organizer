
import { useEffect, useState } from "react";
import { getCourses } from "../api";
import Navbar from "./Navbar";
import { UseAuthContext } from "../hooks/useAuthContext";

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
        <>
            <Navbar />
            <main className="container p-5">

                <div className="mainContainer">
                    <div className={'titleContainer'}>
                        <div>Welcome!</div>
                    </div>
                    <div>This is the home page.</div>
                    <h3> Courses</h3>
                    <ul>
                        {isLoading ? <> Courses Loading.. Please wait</> : <>{courses && courses.map((course: any, index: number) => (<li key={index}> {course.title}</li>))}</>}

                    </ul>

                </div>


            </main>


        </>
    )
}

export default Home