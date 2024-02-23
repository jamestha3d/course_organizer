import * as React from 'react';

interface ISubheaderProps {
    title: string,
    subtext: string
}

const Subheader: React.FunctionComponent<ISubheaderProps> = ({ title, subtext }) => {
    return (
        <>
            <h5>{title}</h5>
            <a className="sub-header-text"> {subtext}</a>
        </>
    );
};

export default Subheader;
