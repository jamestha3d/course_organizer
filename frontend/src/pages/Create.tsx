import * as React from 'react';

import CreateCourse from '../components/forms/CreateCourse';
interface ICreateProps {
}

const Create: React.FunctionComponent<ICreateProps> = (props) => {
    return (
        <div className="page">
            <h3> Create</h3>
            <CreateCourse classroom="78b6dadf-9d8e-467d-b4e8-177a196c561d" />
        </div>
    );
};

export default Create;
