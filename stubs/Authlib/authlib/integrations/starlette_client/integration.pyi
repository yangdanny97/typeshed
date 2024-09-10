from _typeshed import Incomplete
from typing import Any

from ..base_client import FrameworkIntegration

class StarletteIntegration(FrameworkIntegration):
    async def get_state_data(self, session: dict[str, Any] | None, state: str) -> dict[str, Any]: ...
    async def set_state_data(self, session: dict[str, Any] | None, state: str, data: Any): ...
    async def clear_state_data(self, session: dict[str, Any] | None, state: str): ...
    def update_token(self, token, refresh_token: Incomplete | None = None, access_token: Incomplete | None = None) -> None: ...
    @staticmethod
    def load_config(oauth, name, params): ...