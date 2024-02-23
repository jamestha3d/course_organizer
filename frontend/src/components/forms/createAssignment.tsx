import * as React from 'react';
import { useState } from 'react';

interface IcreateCourseProps {
}

const createCourse: React.FunctionComponent<IcreateCourseProps> = (props) => {

    const [formData, setFormData] = useState({
        title: "",

    })

    const handleChange = (e: React.FormEvent) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }
    const createCourse = (e: React.FormEvent) => {
        e.preventDefault();

    }
    return (
        <form method={"POST"} onSumbit={createCourse}>
            <input name="title" value={formData.title} onChange={handleChange}></input>
        </form>
    );
};

export default createCourse;
