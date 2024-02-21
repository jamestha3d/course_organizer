// import { useEffect } from "react"
// import { UseAuthContext } from "../hooks/useAuthContext"

// const Courses = () => {

//     const { dispatch } = UseAuthContext()
//     useEffect(
//         () => {
//             const fetchCourses = async () => {
//                 const response = await fetch('api/classrooms')
//                 const json = await response.json()

//                 if (response.ok) {
//                     dispatch({ type: 'SET_COURSES', payload: json })
//                 }

//             }

//             fetchCourses()
//         },
//         [dispatch]
//     )

//     return (
//         <>

//         </>
//     )
// }

// export default Courses