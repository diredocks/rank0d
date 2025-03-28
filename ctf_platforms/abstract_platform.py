from abc import ABC, abstractmethod
import httpx
from http.cookies import SimpleCookie


class AbstractPlatform(ABC):
    base_url = ""

    def __init__(self, cookies: str):
        self.session = httpx.Client()
        self.set_client_cookie(cookies)

    def set_client_cookie(self, cookies: str):
        cookie = SimpleCookie()
        cookie.load(cookies)
        for key, morsel in cookie.items():
            self.session.cookies.set(key, morsel.value)

    @abstractmethod
    def fetch_challanges(self, user: str) -> list[dict] | None:
        pass

    @abstractmethod
    def get_user_info(self, user: str) -> dict[str, str | list[dict] | None]:
        pass
