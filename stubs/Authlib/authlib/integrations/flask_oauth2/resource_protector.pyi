from _typeshed import Incomplete
from collections.abc import Generator

from authlib.oauth2 import ResourceProtector as _ResourceProtector

class ResourceProtector(_ResourceProtector):
    def raise_error_response(self, error) -> None: ...
    def acquire_token(self, scopes: Incomplete | None = None, **kwargs): ...
    def acquire(self, scopes: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def __call__(self, scopes: Incomplete | None = None, optional: bool = False, **kwargs): ...

current_token: Incomplete