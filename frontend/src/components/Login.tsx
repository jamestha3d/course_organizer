import * as React from 'react';
import { useState } from 'react';
import { loginUser } from '../api';
import { Link } from 'react-router-dom';
import { useLogin } from '../hooks/useLogin';

interface ILoginProps {
}

const Login: React.FunctionComponent<ILoginProps> = (props) => {
    let [authMode, setAuthMode] = useState("signin")
    const [loginForm, setLoginForm] = useState({
        email: "",
        password: "",
    });

    const { login, error, isLoading } = useLogin()

    const handleLogin = async (e: any) => {
        e.preventDefault();
        // const login: any = await loginUser(loginForm)
        // if (login.data) {
        //     const token = login.data.token.access
        //     console.log(token)
        // }
        // else {
        //     const token = false
        //     console.log(token)
        // }
        await login(loginForm.email, loginForm.password)
    }

    const handleChange = (e: any) => {
        //const { name, value } = e.target;
        setLoginForm({
            ...loginForm,
            [e.target.name]: e.target.value,
        });

    };
    return (
        <>
            <div className="Auth-form-container">
                <form className="Auth-form" onSubmit={handleLogin} method="post">
                    <div className="Auth-form-content">
                        <h3 className="Auth-form-title">Sign In</h3>
                        <div className="text-center">
                            Not registered yet?{" "}
                            <Link to="/signup" className="link-primary" >
                                Sign Up
                            </Link>
                        </div>
                        <div className="form-group mt-3">
                            <label>Email address</label>
                            <input
                                type="email"
                                name="email"
                                className="form-control mt-1"
                                placeholder="Enter email"
                                value={loginForm?.email}
                                onChange={handleChange}
                            />
                        </div>
                        <div className="form-group mt-3">
                            <label>Password</label>
                            <input
                                type="password"
                                name="password"
                                className="form-control mt-1"
                                placeholder="Enter password"
                                value={loginForm?.password}
                                onChange={handleChange}
                            />
                        </div>
                        <div className="d-grid gap-2 mt-3">
                            <button type="submit" className="btn btn-primary" disabled={isLoading}>
                                Submit
                            </button>
                        </div>
                        {error && <span className="input-error"> {error}</span>}
                        <p className="forgot-password text-right mt-2">
                            <a href="#">Forgot password?</a>
                        </p>
                    </div>
                </form>
            </div>
        </>
    );
};

export default Login;
