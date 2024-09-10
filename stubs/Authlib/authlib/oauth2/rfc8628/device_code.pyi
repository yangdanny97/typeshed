from _typeshed import Incomplete

from ..rfc6749 import BaseGrant, TokenEndpointMixin

DEVICE_CODE_GRANT_TYPE: str

class DeviceCodeGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE = DEVICE_CODE_GRANT_TYPE
    TOKEN_ENDPOINT_AUTH_METHODS: Incomplete
    def validate_token_request(self) -> None: ...
    def create_token_response(self): ...
    def validate_device_credential(self, credential): ...
    def query_device_credential(self, device_code) -> None: ...
    def query_user_grant(self, user_code) -> None: ...
    def should_slow_down(self, credential) -> None: ...