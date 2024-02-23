import * as React from 'react';
import { useState } from 'react';

interface IcreateSubmissionProps {
}

const createSubmission: React.FunctionComponent<IcreateSubmissionProps> = (props) => {

    const [formData, setFormData] = useState({
        title: "",

    })

    const handleChange = (e: React.FormEvent) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }
    const createSubmission = (e: React.FormEvent) => {
        e.preventDefault();
        //submit

    }
    return (
        <form method={"POST"} onSumbit={createSubmission}>
            <input name="title" value={formData.title} onChange={handleChange}></input>
            <input name="body" value={formData.title} onChange={handleChange}></input>
            <input name="attachments" value={formData.title} onChange={handleChange}></input>
        </form>
    );
};

export default createSubmission;
