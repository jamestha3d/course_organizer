import { Container } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

const CreateClassroom = () => {
    return ( <Container>
        <h1> Create Classroom</h1>
        <hr/>
        <Form>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Title</Form.Label>
                <Form.Control type="text" placeholder="Enter Classsroom Title" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Start Date</Form.Label>
                <Form.Control type="date" placeholder="Enter Classsroom Title" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Start Time</Form.Label>
                <Form.Control type="time" placeholder="Enter Start Time" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>End Date</Form.Label>
                <Form.Control type="date" placeholder="Enter Classsroom Title" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>End Date</Form.Label>
                <Form.Control type="time" placeholder="Enter End time" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>
           
            <Form.Group className="mb-3" controlId="formBasicCheckbox">
                <Form.Check type="checkbox" label="Private Classroom" />
            </Form.Group>
            <Button variant="primary" type="submit">
                Submit
            </Button>
            </Form>
    </Container> );
}
 
export default CreateClassroom;


/*title = models.CharField(max_length=200)
    courses = models.ManyToManyField('Course') # TODO maybe courses should belong to only one classroom. that means we will change the unique code structure.
    start_date = models.DateTimeField(default=now, null=True)
    end_date = models.DateTimeField(null=True)
    students = models.ManyToManyField('Profile', related_name='classrooms_registered')
    admins = models.ManyToManyField('Profile', related_name='classrooms_teaching') #maybe i should call this managers?
    public = models.BooleanField(default=True) */