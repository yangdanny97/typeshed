from ..rfc6749 import TokenMixin

class IntrospectionToken(dict, TokenMixin):
    def get_client_id(self): ...
    def get_scope(self): ...
    def get_expires_in(self): ...
    def get_expires_at(self): ...
    def __getattr__(self, key): ...