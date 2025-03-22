import { Link } from "react-router-dom";
import { useLogout } from "../../hooks/useLogout";

const SignOutButton = () => {

    const { logout } = useLogout()

    const handleClick = () => {
        logout()
    }
    return (
        <>
        <span onClick={handleClick}>
            Sign Out
        </span>
        </>
    )
}

export default SignOutButton