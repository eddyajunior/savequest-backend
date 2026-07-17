from typing import Any


class ApplicationError(Exception):
    code = "APPLICATION_ERROR"
    status_code = 400

    def __init__(
        self,
        message: str,
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}


class ResourceNotFoundError(ApplicationError):
    code = "RESOURCE_NOT_FOUND"
    status_code = 404


class BusinessRuleViolationError(ApplicationError):
    code = "BUSINESS_RULE_VIOLATION"
    status_code = 422


class ConflictError(ApplicationError):
    code = "CONFLICT"
    status_code = 409


class UnauthorizedError(ApplicationError):
    code = "UNAUTHORIZED"
    status_code = 401


class ForbiddenError(ApplicationError):
    code = "FORBIDDEN"
    status_code = 403
