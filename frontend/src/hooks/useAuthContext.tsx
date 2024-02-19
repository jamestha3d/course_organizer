import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

interface IUseAuthContextProps {
}

export const UseAuthContext: any = () => {
    const context = useContext(AuthContext)

    if (!context) {
        throw Error('useAuthContext must be used inside an AuthContextProvider')
    }
    return context;
};


