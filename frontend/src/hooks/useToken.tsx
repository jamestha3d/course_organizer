import * as React from 'react';
import { useState } from 'react';

interface IuseTokenProps {
}

function useToken() {
    const getToken = () => {
        const tokenString: any = localStorage.getItem('token');
        const userToken = JSON.parse(tokenString);
        return userToken?.token;
    };
    const [token, setToken] = useState(getToken());

    const saveToken = (userToken: any) => {
        localStorage.setItem('token', JSON.stringify(userToken));
        setToken(userToken.token);
    };

    return {
        setToken: saveToken,
        token
    }
}

export default useToken;
