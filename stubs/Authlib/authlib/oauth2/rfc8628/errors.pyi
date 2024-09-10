from ..rfc6749.errors import OAuth2Error

class AuthorizationPendingError(OAuth2Error):
    error: str

class SlowDownError(OAuth2Error):
    error: str

class ExpiredTokenError(OAuth2Error):
    error: str