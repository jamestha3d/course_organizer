import * as React from 'react';
import MyCourses from '../components/MyCourses';
import Subheader from '../components/Subheader';
import Assignments from '../components/Assignments';
import MyCohorts from '../components/MyCohorts';

interface IDashboardProps {
}

const Dashboard: React.FunctionComponent<IDashboardProps> = (props) => {
    return (<div className="page">
        <h3>Dashboard</h3>
        <br /> <hr />

        <Subheader title="Cohorts" subtext="You are currently a part of:" />

        <MyCohorts />
        <Subheader title="My Courses" subtext="These are the courses that you have registered for" />

        <MyCourses />
        <br /> <hr />
        <Subheader title="Assignments" subtext="Here are your recent assignments" />
        <Assignments />
    </div>);
};

export default Dashboard;
