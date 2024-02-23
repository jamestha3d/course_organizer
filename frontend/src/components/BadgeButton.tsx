import * as React from 'react';

interface IAppProps {
}

const App: React.FunctionComponent<IAppProps> = (props) => {
    return (
        <button type="button" className="btn btn-primary position-relative">
            Inbox
            <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                99+
                <span className="visually-hidden">unread messages</span>
            </span>
        </button>
    );
};

export default App;



