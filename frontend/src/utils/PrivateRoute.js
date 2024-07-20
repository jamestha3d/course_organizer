// import {Route, Redirect} from 'react-router-dom'

// const PrivateRoute = ({children, ...rest}) => {
//     console.log('Private route works')
//     return (
//         <Route {...rest}>{children}</Route>
//     )
// }

// export default PrivateRoute

//Code update 

import {Outlet, Navigate} from "react-router-dom";
import { useAuth } from "./AuthContext";
import { UseAuthContext } from "../hooks/useAuthContext";
const PrivateRoutes = () => {
    //const user = true
    const {user} = UseAuthContext() 
    return user ? <Outlet/> : <Navigate to='/login'/>
}

export default PrivateRoutes