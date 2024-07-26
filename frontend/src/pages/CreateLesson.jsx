import { Container } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
const CreateLesson = () => {
    const handleSubmit = (e) => {
        e.preventDefault()
    }

    //add time reader that will convert the fractional time to hour minutes. e.g 1.5 will show the user 1hr30mins.
    return ( <Container>
        <h1> Create Lesson</h1>
        <hr/>
        <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Topic</Form.Label>
                <Form.Control type="text" placeholder="Enter topic for the day" />
                <Form.Text className="text-muted">
                What topic will this lesson cover?
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Description</Form.Label>
                <Form.Control type="text" placeholder="Enter a description for this Lesson" />
                <Form.Text className="text-muted">
                Describe this lesson and what you aim to cover.
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Start Date</Form.Label>
                <Form.Control type="date" placeholder="Enter Classsroom Title" />
                <Form.Text className="text-muted">
                Start date.
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
                <Form.Label>Duration</Form.Label>
                <Form.Control type="number" step="0.25" min="0.25" placeholder="Enter Duration in hours" />
                <Form.Text className="text-muted">
                Decimals represent fractions of an hour. e.g 1.5 = 1 hour 30 minutes
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
 
export default CreateLesson;

// title = models.CharField(max_length=256)
//     course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
//     video_link = models.URLField(null=True)
//     meeting_link = models.URLField(null=True)
//     start_time = models.DateTimeField(null=True)
//     one_hour = datetime.time(1,0,0)
//     duration = models.TimeField(default=one_hour, null=True)
//     notes = models.ForeignKey('LessonNote', on_delete=models.CASCADE, null=True)
//     description = models.TextField()
//     instructor = models.ManyToManyField(Profile, related_name='lessons', through='LessonInstructor', through_fields=('lesson', 'instructor'))
//     assignments = models.ManyToManyField(Assignment, related_name='assignments' )