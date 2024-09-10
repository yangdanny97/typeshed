from _typeshed import Incomplete

class JWTBearerTokenGenerator:
    DEFAULT_EXPIRES_IN: int
    secret_key: Incomplete
    issuer: Incomplete
    alg: Incomplete
    def __init__(self, secret_key, issuer: Incomplete | None = None, alg: str = "RS256") -> None: ...
    @staticmethod
    def get_allowed_scope(client, scope): ...
    @staticmethod
    def get_sub_value(user): ...
    def get_token_data(self, grant_type, client, expires_in, user: Incomplete | None = None, scope: Incomplete | None = None): ...
    def generate(
        self,
        grant_type,
        client,
        user: Incomplete | None = None,
        scope: Incomplete | None = None,
        expires_in: Incomplete | None = None,
    ): ...
    def __call__(
        self,
        grant_type,
        client,
        user: Incomplete | None = None,
        scope: Incomplete | None = None,
        expires_in: Incomplete | None = None,
        include_refresh_token: bool = True,
    ): ...