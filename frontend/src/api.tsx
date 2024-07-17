import axios from "axios"
import { Lesson } from "./models/lesson.model";
import { UseAuthContext } from "./hooks/useAuthContext";

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

function getUser() {
    const user = localStorage.getItem('user')
    return user ? JSON.parse(user) : user
}

const getEndpoint = async (endpoint: string,) => {
    const user = getUser()
    try {
        const data = await axios.get<any>(
            `${endpoint}`,
            {
                headers: {
                    Authorization: 'Bearer ' + user.token.access
                }
            }
        );

        return data.data.results;

    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return [];
        } else {
            console.log("unexpected error: ", error);
            return [];
        }
    }
}

const postEndpoint = async (endpoint: string, body: any) => {
    const user = getUser()
    try {
        const data = await axios.post<any>(
            `${endpoint}`,
            body,
            {
                headers: {
                    Authorization: 'Bearer ' + user.token.access
                }
            }
        );

        return data;

    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return [];
        } else {
            console.log("unexpected error: ", error);
            return [];
        }
    }
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
            //toast error message
            //release the submit button
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
            `${endpoint}` + 'api/classrooms?limit=3',
        );
        return data.data.results;

    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return [];
        } else {
            console.log("unexpected error: ", error);
            return [];
        }
    }
}

export const getAssignments = async () => {
    return await getEndpoint(api + 'assignments')
}

export const postNewCourse = async (data: any) => {
    return await postEndpoint(api + 'courses/', data)
}

export const getApiEndPoint = async (endpoint:String) => {
    return await getEndpoint(api + endpoint)
}

export const postApiEndPoint = async (endpoint:String, data:any) => {
    return await postEndpoint(api + endpoint, data)
}

const getEndpointNoPagination = async (endpoint: string,) => {
    const user = getUser()
    try {
        const data = await axios.get<any>(
            `${endpoint}`,
            {
                headers: {
                    Authorization: 'Bearer ' + user.token.access
                }
            }
        );

        if ('results' in data.data){
            return data.data.results;
        }
        else{
            return data.data
        }

    }
    catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("error message: ", error.message);
            return [];
        } else {
            console.log("unexpected error: ", error);
            return [];
        }
    }
}

export const getApi= async (endpoint:String) => {
    return await getEndpointNoPagination(api + endpoint)
}