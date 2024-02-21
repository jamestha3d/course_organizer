import * as React from 'react';
import MyCourses from '../components/MyCourses';

interface IDashboardProps {
}

const Dashboard: React.FunctionComponent<IDashboardProps> = (props) => {
    return (<>
        <p>This is your dashboard</p>

        <p>MY Courses</p>
        <MyCourses />
    </>);
};

export default Dashboard;
