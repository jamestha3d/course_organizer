import Card from 'react-bootstrap/Card';

const TitleCard = ({ img, body, title, instructor }) => {

    return (
        <Card>
            <Card.Img variant="top" src={img} />
            <Card.Body>
                <Card.Title>{title}</Card.Title>
                <Card.Text>
                    {body}
                </Card.Text>
            </Card.Body>
            <Card.Footer>
                <small className="text-muted">{instructor}</small>
            </Card.Footer>
        </Card>
    )
}

export default TitleCard