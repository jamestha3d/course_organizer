import { createContext, useReducer, useEffect } from 'react'

export const AuthContext = createContext(null)

export const authReducer:any = (state, action) => {
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
            const user = JSON.parse(localStorage.getItem('user'))
            if (user) {
                console.log('user found', user)
                //@ts-ignore
                dispatch({ type: 'LOGIN', payload: user })
            }
            else{
                console.log('user not found')
            }
        },
        []
    )
    return (
        //@ts-ignore
        <AuthContext.Provider value={{ ...state, dispatch }}>
            {children}
        </AuthContext.Provider>
    )
} 