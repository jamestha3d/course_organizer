const Courses = () => {

    useEffect(
        () => {
            const fetchCourses = async () => {
                const response = await fetch('api/classrooms')
                const json = await response.json()

                if (response.ok) {
                    dispatch({ type: 'SET_COURSES', payload: json })
                }

            }

            fetchCourses()
        },
        [dispatch]
    )

    return (
        <>

        </>
    )
}

export default Courses