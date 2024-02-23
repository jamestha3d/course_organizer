import * as React from 'react';
import { getAssignments } from '../api';
import { useEffect, useState } from 'react';
import { UseAuthContext } from '../hooks/useAuthContext';



interface IAssignmentsProps {
}

const Assignments: React.FunctionComponent<IAssignmentsProps> = (props) => {

    const user = UseAuthContext()
    const [loading, setLoading] = useState(true)
    const [assignments, setAssignments] = useState([])
    const fetchAssignments = async () => {
        const data = await getAssignments()
        console.log(data)
        setAssignments(data)
        setLoading(false)
    }

    useEffect(
        () => {
            if (user) {
                fetchAssignments()
            }
        }, []
    )

    return (<div>
        {loading ? <a>Loading Assignments</a> : <> {assignments.map((assignment, index) => (<a key={index}>{assignment.title}</a>))}</>}

    </div>);
};

export default Assignments;
