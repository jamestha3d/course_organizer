import { createContext, useReducer } from 'react'

//using context to update state locally. wrap app in index.js with this context provider

export const AssignmentContext = createContext()

export const assignmentsReducer = (state, action) => {
    switch (action.type) {
        case 'SET_ASSIGNMENTS':
            return {
                assignments: action.payload
            }

        case 'CREATE_ASSIGNMENT':
            return {
                assignments: [action.payload, ...state.assignments]
            }

        case 'DELETE_ASSIGNMENT':
            return {
                assignments: state.assignments.filter((a) => a.guid !== action.payload.guid)
            }

        default:
            return state
    }
}

export const AssignmentContextProvider = ({ children }) => {
    const [state, dispatch] = useReducer(assignmentsReducer, { assignments: null })

    // dispatch({type: 'SET_WORKOUTS', payload: [{},{}]})
    return (
        <AssignmentContext.Provider value={{ ...state, dispatch }}>
            {children}
        </AssignmentContext.Provider>
    )

}