import * as React from 'react';

interface ITopNavProps {
    title: string,
}

const TopNav: React.FunctionComponent<ITopNavProps> = ({ title }) => {
    return (
        <div style={{ "display": "flex", "flexWrap": "wrap" }}>
            <h3> {title} </h3>

            <button style={{ "position": "absolute", "right": "0" }}> Notifications</button>
        </div>
    );
};

export default TopNav;
