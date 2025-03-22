import { Link } from "react-router-dom";
import { useLogout } from "../hooks/useLogout";

const LogoutButton = () => {

    const { logout } = useLogout()

    const handleClick = () => {
        logout()
    }
    return (
        <header>
            <div >
                <Link to="/">
                    <h1> Home</h1>
                </Link>
                <nav>
                    <div>
                        <button onClick={handleClick}>
                            Log out
                        </button>
                    </div>
                    <div>
                        <Link to='/login'> Log in</Link>
                        <Link to='/signup'> Sign up</Link>
                    </div>
                </nav>
            </div>
        </header>
    )
}

export default LogoutButton