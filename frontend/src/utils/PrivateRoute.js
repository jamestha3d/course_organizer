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
const PrivateRoutes = () => {
    //const user = true
    const {user} = useAuth() 
    return user ? <Outlet/> : <Navigate to='/login'/>
}

export default PrivateRoutes