import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';

const TitleCard = ({ img, body, title, instructor, link }) => {

    return (
        <Card>
            <Card.Img variant="top" src={img} />
            <Card.Body>
                <Card.Title>{link ? <Link to={link}>{title}</Link> : title}</Card.Title>
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