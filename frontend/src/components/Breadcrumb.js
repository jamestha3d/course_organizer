import Breadcrumb from 'react-bootstrap/Breadcrumb';

function BreadCrumb() {
  return (
    <Breadcrumb>
      <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
      <Breadcrumb.Item href="/cohorts/all">
        Cohorts
      </Breadcrumb.Item>
      <Breadcrumb.Item active>All Cohorts</Breadcrumb.Item>
    </Breadcrumb>
  );
}

export default BreadCrumb;