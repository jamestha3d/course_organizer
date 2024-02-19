import { useState } from "react";
import { UseAuthContext } from "./useAuthContext";

export const useLogin = () => {
    const [error, setError] = useState(null)
    const [isLoading, setIsLoading] = useState(null)
    const { dispatch } = UseAuthContext()
    const api = process.env.REACT_APP_API_URL

    const login = async (email, password) => {
        setIsLoading(true)
        setError(null)

        const response = await fetch(api + 'auth/login/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        })

        console.log('POSTING', JSON.stringify({ email, password }))

        const json = await response.json()

        if (!response.ok) {
            setIsLoading(false)
            setError(json.errors)
            console.log('error', json.error)
        }

        if (response.ok) {
            //save user to local storage
            console.log(json)
            localStorage.setItem('user', JSON.stringify(json))

            //update the auth context
            dispatch({ type: 'LOGIN', payload: json })

            setIsLoading(false)

        }
    }

    return { login, isLoading, error }
}