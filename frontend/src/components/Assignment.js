import { useEffect } from "react"
import { UseAuthContext } from "../hooks/useAuthContext"

const Assignment = () => {
    const { user } = UseAuthContext()
    const { assignments, dispatch } = useAssignmentsContext() //TODO useAssignmentsContext

    useEffect(() => {
        const fetchAssignments = async () => {
            const response = await fetch('/api/workouts', {
                headers: {
                    'Authorization': `Bearer ${user.token}`
                }
            })
            const json = await response.json()

            if (response.ok) {
                dispatch({ type: 'SET_ASSIGNMENTS', payload: json })
            }

        }

        if (user) {
            fetchAssignments()
        }
    }, [dispatch, user])

    return (
        <></>
    )
}
export default Assignment