
import * as FaIcons from "react-icons/fa"
import * as AiIcons from "react-icons/ai"
import * as IoIcons from "react-icons/io"
import { NavLink } from "react-router-dom"
import { useState } from 'react'

const Sidebar = ({ children }) => {
    const [isOpen, setIsOpen] = useState(false)
    const toggle = () => setIsOpen(!isOpen)
    const menuItem = [
        {
            title: 'Home',
            path: '/',
            icon: <AiIcons.AiFillHome />,
            cName: 'nav-text'
        },
        {
            title: 'Dashboard',
            path: '/dashboard',
            icon: <IoIcons.IoIosPaper />,
            cName: 'nav-text'
        },
        {
            title: 'My Courses',
            path: '/my_courses',
            icon: <FaIcons.FaCartPlus />,
            cName: 'nav-text'
        },
        {
            title: 'Discussion',
            path: '/discussion',
            icon: <IoIcons.IoMdPeople />,
            cName: 'nav-text'
        },
        {
            title: 'Messages',
            path: '/messages',
            icon: <FaIcons.FaEnvelopeOpenText />,
            cName: 'nav-text'
        },
        {
            title: 'Support',
            path: '/support',
            icon: <IoIcons.IoMdHelpCircle />,
            cName: 'nav-text'
        },
        {
            title: 'Create',
            path: '/create',
            icon: <FaIcons.FaPlus />,
            cName: 'nav-text'
        },
        {
            title: 'Notifications',
            path: '/notifications',
            icon: <IoIcons.IoMdHelpCircle />,
            cName: 'nav-text'
        },
        {
            title: 'Logout',
            path: 'logout',
            icon: <IoIcons.IoMdHelpCircle />,
            cName: 'nav-text'
        }
    ]

    return (
        <div className="sidebar-container">
            <div style={{ width: isOpen ? "200px" : "50px" }} className="sidebar">
                <div className="top_section">
                    <h1 style={{ display: isOpen ? "block" : "none" }} className="logo">Logo</h1>
                    <div style={{ marginLeft: isOpen ? "50px" : "0px" }} className="bars">
                        <FaIcons.FaBars onClick={toggle} />
                    </div>
                </div>
                {
                    menuItem.map((item, index) => (
                        <NavLink to={item.path} key={index} className={("sidebar-link")} activeclassname="active">
                            <div className="icon">{item.icon}</div>
                            <div style={{ display: isOpen ? "block" : "none" }} className="link_text">{item.title}</div>
                        </NavLink>
                    ))
                }
            </div>
            <main>{children}</main>
        </div>
    );
}
export default Sidebar;