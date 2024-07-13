import { createContext, useReducer, useEffect } from 'react'

export const AuthContext = createContext(null)

export const authReducer = (state, action) => {
    switch (action.type) {
        case 'LOGIN':
            return { user: action.payload }
        case 'LOGOUT':
            return { user: null }
        default:
            return state
    }
}
export const AuthContextProvider = ({ children }) => {
    const [state, dispatch] = useReducer(authReducer, {
        user: null
    })
    useEffect(
        () => {
            const user_info = localStorage.getItem('user')
            const user = user_info ? JSON.parse(user_info) : null;
            if (user) {
                dispatch({ type: 'LOGIN', payload: user })
            }
        },
        []
    )
    return (
        <AuthContext.Provider value={{ ...state, dispatch }}>
            {children}
        </AuthContext.Provider>
    )
} 