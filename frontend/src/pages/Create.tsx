import * as React from 'react';
import Container from 'react-bootstrap/Container';
import CreateCourse from '../components/forms/createCourse';
interface ICreateProps {
}

const Create: React.FunctionComponent<ICreateProps> = (props) => {
    return (
        <Container>
        <div className="page">
            <h3> Create</h3>
            <CreateCourse classroom="78b6dadf-9d8e-467d-b4e8-177a196c561d" />
        </div>
        </Container>
    );
};

export default Create;
