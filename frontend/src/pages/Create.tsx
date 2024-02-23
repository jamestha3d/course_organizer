import * as React from 'react';

import CreateCourse from '../components/forms/CreateCourse';
interface ICreateProps {
}

const Create: React.FunctionComponent<ICreateProps> = (props) => {
    return (
        <div className="page">
            <h3> Create</h3>
            <CreateCourse />
        </div>
    );
};

export default Create;
