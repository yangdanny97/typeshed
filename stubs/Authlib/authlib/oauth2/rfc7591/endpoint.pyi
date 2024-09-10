from _typeshed import Incomplete

from .claims import ClientMetadataClaims

class ClientRegistrationEndpoint:
    ENDPOINT_NAME: str
    claims_class = ClientMetadataClaims
    software_statement_alg_values_supported: Incomplete
    server: Incomplete
    def __init__(self, server) -> None: ...
    def __call__(self, request): ...
    def create_registration_response(self, request): ...
    def extract_client_metadata(self, request): ...
    def extract_software_statement(self, software_statement, request): ...
    def get_claims_options(self): ...
    def generate_client_info(self): ...
    def generate_client_registration_info(self, client, request) -> None: ...
    def create_endpoint_request(self, request): ...
    def generate_client_id(self): ...
    def generate_client_secret(self): ...
    def get_server_metadata(self) -> None: ...
    def authenticate_token(self, request) -> None: ...
    def resolve_public_key(self, request) -> None: ...
    def save_client(self, client_info, client_metadata, request) -> None: ...