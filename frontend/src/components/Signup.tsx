import Button from 'react-bootstrap/Button';
import { Col, Form, Row } from 'react-bootstrap';
import { useState, useRef, useEffect } from 'react';
import { faCheck, faTimes, faInfoCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from 'react-router-dom';
import { useSignup } from '../hooks/useSignup';
// import Form from 'react-bootstrap/Form';
// import Row from 'react-bootstrap/Row';

const USER_REGEX = /^[A-z][A-z0-9-_]{3,23}$/;
const PWD_REGEX = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;
const REGISTER_URL = '/register';

function SignUpPage() {

    let [authMode, setAuthMode] = useState("signup")

    const [formData, setFormData] = useState({
        email: '',
        password: '',
        confirmPassword: ''
    })

    const handleChange = (e: any) => {
        const { name, value } = e.target;
        setFormData({
            ...formData, [name]: value
        })
    }

    const changeAuthMode = () => {
        setAuthMode(authMode === "signin" ? "signup" : "signin")
    }

    const [errors, setErrors] = useState<any>({})

    const { signup, error, isLoading } = useSignup()

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        const validationErrors: any = {}
        if (!formData.email.trim()) {
            validationErrors.email = "email is required"
        } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
            validationErrors.email = "email is not valid"
        }

        if (!formData.password.trim()) {
            validationErrors.password = "password is required"
        } else if (formData.password.length < 8) {
            validationErrors.password = "password should be at least 8 characters"
        }

        if (formData.confirmPassword !== formData.password) {
            validationErrors.confirmPassword = "passwords do not match"
        }

        setErrors(validationErrors)

        if (Object.keys(validationErrors).length === 0) {
            //sign up
            //alert("Form success")
            console.log('signing up', formData.email, formData.password)
            await signup(formData.email, formData.password)


        }
    }
    return (
        <div className="Auth-form-container">
            <form className="Auth-form" onSubmit={handleSubmit}>
                <div className="Auth-form-content">
                    <h3 className="Auth-form-title">Sign Up</h3>
                    <div className="text-center">
                        Already registered?{" "}
                        <Link to='/login' className="link-primary" onClick={changeAuthMode}>
                            Sign In
                        </Link>
                    </div>
                    <div className="form-group mt-3">
                        <label>Email address</label>
                        <input
                            type="email"
                            name="email"
                            value={formData?.email}
                            className="form-control mt-1"
                            placeholder="Email Address"
                            onChange={handleChange}
                        />
                        {errors.email && <span className="input-error"> {errors.email}</span>}
                    </div>
                    <div className="form-group mt-3">
                        <label>Password</label>
                        <input
                            type="password"
                            name="password"
                            value={formData?.password}
                            className="form-control mt-1"
                            placeholder="Password"
                            onChange={handleChange}
                        />
                        {errors.password && <span className="input-error"> {errors.password}</span>}
                    </div>
                    <div className="form-group mt-3">
                        <label>Confirm Password</label>
                        <input
                            type="password"
                            name="confirmPassword"
                            value={formData?.confirmPassword}
                            className="form-control mt-1"
                            placeholder="Confirm Password"
                            onChange={handleChange}
                        />
                        {errors.confirmPassword && <span className="input-error"> {errors.confirmPassword}</span>}
                    </div>
                    <div className="d-grid gap-2 mt-3">
                        <button type="submit" className="btn btn-primary" disabled={isLoading} >
                            Submit
                        </button>
                    </div>
                    {error && <div className="input-error"> {error} </div>}
                    <p className="text-center mt-2">
                        Forgot <Link to="/forgot_password">password?</Link>
                    </p>
                </div>

            </form>

        </div>
    );
}

export default SignUpPage;