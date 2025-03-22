import { useContext, useState, useEffect, createContext } from "react";

const AuthContext = createContext()

export const AuthProvider = ({children}) => {

    const [loading, setLoading] = useState(true)
    const [user, setUser] = useState(true)

    useEffect( () => {
        //setLoading(false)
        checkUserStatus()
    }, [])
    const loginUser = async (userInfo) => {
        setLoading(true)
        try{
            // let response = await fetch(userInfo) //log user in
            // setUser(response.user)
        }catch(error){
            console.error(error)
        }
    }

    const logoutUser = () => {
        setUser(null)
    }

    const registerUser = (userInfo) => {}

    const checkUserStatus = async () => {
        try{
            // let account = await fetch()
            // setUser(account.user)
        }catch(error){
            console.error(error)
        }
        setLoading(false)
    }
    const contextData = {
        user,
        loginUser,
        logoutUser,
        registerUser,

    }
    return(
        <AuthContext.Provider value={contextData}>
        {loading ? <p>Loading . . .</p> : children }
    </AuthContext.Provider>
    )
    
}

export const useAuth = () => {
    return useContext(AuthContext)
}
export default AuthContext