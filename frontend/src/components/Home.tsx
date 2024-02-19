
// const Home = () => {

import Navbar from "./Navbar";

//     return (
//         <a href='google.com'> home was imported</a>
//     )
// }

// export default Home
//import { useNavigate } from 'react-router-dom'
interface Props {
}


const Home = (props: Props) => {
    //const { loggedIn, email } = 
    //const navigate = useNavigate()
    const email: string = '';
    const loggedIn: boolean = false;
    const onButtonClick = () => {
        // You'll update this function later
    }

    return (
        <>
            <Navbar />
            <main className="container p-5">

                <div className="mainContainer">
                    <div className={'titleContainer'}>
                        <div>Welcome!</div>
                    </div>
                    <div>This is the home page.</div>

                </div>


            </main>


        </>
    )
}

export default Home