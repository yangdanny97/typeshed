def register_temporary_credential_hooks(authorization_server, cache, key_prefix: str = "temporary_credential:"): ...
def create_exists_nonce_func(cache, key_prefix: str = "nonce:", expires: int = 86400): ...
def register_nonce_hooks(authorization_server, cache, key_prefix: str = "nonce:", expires: int = 86400) -> None: ...