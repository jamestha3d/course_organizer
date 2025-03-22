import Badge from 'react-bootstrap/Badge';
import ListGroup from 'react-bootstrap/ListGroup';

function GroupListItem({subheading, text, number}) {
  return (
      <ListGroup.Item
        as="li"
        className="d-flex justify-content-between align-items-start"
      >
        <div className="ms-2 me-auto">
          <div className="fw-bold">{subheading}</div>
          {text}
        </div>
        <Badge bg="primary" pill>
          {number}
        </Badge>
      </ListGroup.Item>

  );
}

export default GroupListItem;