from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    def __init__(self, detail=None, reason=None):
        if detail is not None:
            self.detail = detail
        else:
            self.detail = self.default_detail
        self.reason = reason

        super().__init__(detail=self.detail)

def custom_exception_handler(exc, context):
    if isinstance(exc, CustomAPIException):
        response = {
            "status": str(exc.default_code),
            "detail": str(exc.detail),
        }
        if exc.reason:
            response["reason"] = str(exc.reason)
        return Response(response, status=exc.status_code)
    
    # Call REST framework's default exception handler if the exception is not caught
    response = exception_handler(exc, context)
    return response


class AlreadyInUse(APIException):
    status_code = 400
    default_detail = 'this value is already in use'
    default_code = 'already_in_use'

class UnexpectedDataError(APIException):
    status_code = 500
    default_detail = ''
    default_code = ''


class DuplicateRequestIgnored(CustomAPIException):
    status_code = 200
    default_detail="The data submitted matches an existing record or operation, so no new action was taken."
    default_code = 'duplicate_request_ignored'