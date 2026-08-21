"""Hotglue ETL Exceptions module."""


class InvalidCredentialsError(Exception):
    """Exception raised when credentials are invalid."""
    pass


class InvalidPayloadError(Exception):
    """Exception raised when payload is invalid."""
    pass


class InsufficientPermissionsError(Exception):
    """Exception raised when credentials lack the required permission scope."""
    pass


__all__ = ['InvalidCredentialsError', 'InvalidPayloadError', 'InsufficientPermissionsError']

