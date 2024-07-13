import * as React from 'react';
import { useState, useEffect } from 'react';
import { postNewCourse } from '../../api';
import { Navigate, useNavigate } from 'react-router-dom';
interface IcreateCourseProps {
  classroom: string
}

const CreateCourse: React.FunctionComponent<IcreateCourseProps> = ({ classroom }) => {

  const emptyForm = {
    classroom: classroom,
    title: "",
    code: "",
    description: ""
  }
  const [formData, setFormData] = useState(emptyForm)
  const [submitted, setSubmitted] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }


  let navigate = useNavigate();

  useEffect(() => {
    //toast success
    if (submitted) {
      return navigate("/dashboard");
    }
  }, [submitted]);

  const submitCourse = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true)
    const post = await postNewCourse(formData)
    setIsLoading(false)
    if (post.status === 201) {
      //redirect to home page
      setFormData(emptyForm)
      setSubmitted(true)
    }
    else {
      alert("Something went wrong")
    }

  }

  return (
    <div>
      <form className="" method={"POST"} onSubmit={submitCourse}>
        <div className="form-content">
          <div className="form-group">
            <label>Title</label>
            <input type="text" name="title" value={formData.title} className="form-control mt-1" placeholder="Title" onChange={handleChange}></input>
          </div>
          <div className="form-group">
            <label>code</label>
            <input type="text" name="code" value={formData.code} className="form-control mt-1" onChange={handleChange} placeholder="Cource Code e.g ABC123" maxLength="6"></input>
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea name="description" value={formData.description} onChange={handleChange} placeholder="Enter a description" className="form-control mt-1" rows={4} cols={40}></textarea>
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary" disabled={isLoading} >
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default CreateCourse;
