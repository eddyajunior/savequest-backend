from app.core.errors import (
    BusinessRuleViolationError,
    ConflictError,
    ForbiddenError,
    ResourceNotFoundError,
    UnauthorizedError,
)


def test_resource_not_found_error() -> None:
    error = ResourceNotFoundError(
        "Meta não encontrada.",
        details={"goal_id": "123"},
    )

    assert error.code == "RESOURCE_NOT_FOUND"
    assert error.status_code == 404
    assert error.message == "Meta não encontrada."
    assert error.details == {"goal_id": "123"}


def test_business_rule_violation_error() -> None:
    error = BusinessRuleViolationError("A data deve estar no futuro.")

    assert error.code == "BUSINESS_RULE_VIOLATION"
    assert error.status_code == 422


def test_conflict_error() -> None:
    error = ConflictError("Recurso já existe.")

    assert error.code == "CONFLICT"
    assert error.status_code == 409


def test_unauthorized_error() -> None:
    error = UnauthorizedError("Autenticação necessária.")

    assert error.code == "UNAUTHORIZED"
    assert error.status_code == 401


def test_forbidden_error() -> None:
    error = ForbiddenError("Acesso negado.")

    assert error.code == "FORBIDDEN"
    assert error.status_code == 403
