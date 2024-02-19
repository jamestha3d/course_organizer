import axios from "axios"
import { Lesson } from "./models/lesson.model";

const endpoint = process.env.REACT_APP_API_URL;
const api = endpoint + 'api/';
const login = endpoint + 'auth/login/'
const signup = endpoint + 'auth/signup/'
interface LessonsResponse {
    data: Lesson[]
}

export interface Login_details {
    email: string,
    password: string
}

export const getLessons = async (query: string) => {
    try {
        const data = await axios.get<LessonsResponse>(
            `${api}lessons`
        );
        return data;
    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return error.message;
        } else {
            console.log("unexpected error: ", error);
            return "An unexpected error has occured.";
        }
    }
}

export const loginUser = async (login_details: Login_details) => {
    try {
        console.log("SIGNING IN...")
        const data = await axios.post<Login_details>(
            `${login}`,
            login_details
        );
        console.log(data.data)
        return data;
    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return error.message;
        } else {
            console.log("unexpected error: ", error);
            return "An unexpected error has occured.";
        }
    }
}

export const signUpUser = async (signup_details: Login_details) => {
    try {
        console.log("SIGNING IN...")
        const data = await axios.post<Login_details>(
            `${signup}`,
            signup_details
        );
        return data;
    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return error.message;
        } else {
            console.log("unexpected error: ", error);
            return "An unexpected error has occured.";
        }
    }
}

export const getCourses = async () => {
    try {
        const data = await axios.get<any>(
            `${endpoint}` + 'api/classrooms',
        );
        return data.data;

    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return error.message;
        } else {
            console.log("unexpected error: ", error);
            return "An unexpected error has occured.";
        }
    }
}