import { AssignmentContext } from '../context/AssignmentContext'

import { useContext } from 'react'

//to ensure that the context is used in context
export const useAssignmentContext = () => {
    const context = useContext(AssignmentContext)

    if (!context) {
        throw Error('useAssignmentContext must be used inside an AssignmentContextProvider')
    }
    return context
}