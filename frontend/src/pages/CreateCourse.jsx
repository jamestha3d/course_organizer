import { Container } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

const CreateCourse = () => {
    return ( <Container>
        <h1> Create Course</h1>
        <hr/>
        <Form>
            <p className="required-info">
                Fields marked with an asterisk<span className="required-asterisk">*</span> are required.
            </p>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Title <span className="required-asterisk">*</span></Form.Label>
                <Form.Control type="text" placeholder="Enter Course Title" required/>
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Course Code <span className="required-asterisk">*</span></Form.Label>
                <Form.Control type="text" placeholder="Course code" required/>
                <Form.Text className="text-muted">
                Course code is of the form: ABC123.
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Namespace</Form.Label>
                <Form.Control type="text" placeholder="Enter Namespace for course" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Description</Form.Label>
                <Form.Control type="text" placeholder="Enter Course Description" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>
           
            <Form.Group className="mb-3" controlId="formBasicCheckbox">
                <Form.Check type="checkbox" label="Private Classroom" />
            </Form.Group>
            <Button variant="primary" type="submit">
                Create Course
            </Button>
            </Form>
    </Container> );
}
 
export default CreateCourse;


/*title = models.CharField(max_length=256)
    code = models.CharField(max_length=6, unique=True)
    namespace = AutoSlugField(populate_from='title', blank=True, null=True, editable=True, always_update=False)
    description = models.TextField(null=True)
    instructors = models.ManyToManyField('Profile', related_name='courses_teaching')*/