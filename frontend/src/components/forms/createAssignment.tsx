import * as React from 'react';
import { useState } from 'react';

interface IcreateCourseProps {
}

interface IFormData {
    [key: string]: string;
  }

const createCourse: React.FunctionComponent<IcreateCourseProps> = (props) => {

    const [formData, setFormData] = useState<IFormData>({
        title: "",

    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        // const {name, value} = e.target;
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }
    const createCourse = (e: React.FormEvent) => {
        e.preventDefault();

    }
    return (
        <form method={"POST"} onSubmit={createCourse}>
            <input name="title" value={formData.title} onChange={handleChange}></input>
        </form>
    );
};

export default createCourse;
