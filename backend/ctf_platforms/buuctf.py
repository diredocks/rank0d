from .abstract_platform import AbstractPlatform
from .util import extract_between, iso_to_timestamp
from bs4 import BeautifulSoup as bs


class BUUCTF(AbstractPlatform):
    base_url = "https://buuoj.cn"

    def get_user_path(self, user: str) -> str | None:
        resp = self.session.get(f"{self.base_url}/users?field=name&q={user}")
        soup = bs(resp.text, "lxml")
        elem = soup.select_one(
            ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)"
        )
        return str(elem.get("href")) if elem else None

    def get_user_solves(self, user: str) -> list | None:
        path = self.get_user_path(user)
        if not path:
            return None
        resp = self.session.get(self.base_url + path)
        soup = bs(resp.text, "lxml")
        return [each.find_all("td") for each in soup.select(".table-striped tbody tr")]

    def parse_user_solves(self, solves: list) -> list[dict]:
        return [
            {
                "challenges": solve[0].find("a").text
                if solve[0].find("a")
                else solve[0].text,
                "link": self.base_url + solve[0].find("a").get("href")
                if solve[0].find("a")
                else self.base_url,
                "category": solve[1].text,
                "point": solve[2].text,
                "time": iso_to_timestamp(
                    extract_between(
                        solve[3].find("script").text, 'moment("', '").local'
                    )
                ),
            }
            for solve in solves
        ]

    def fetch_challanges(self, user: str) -> list[dict] | None:
        raw_solves = self.get_user_solves(user)
        if not raw_solves:
            return None
        parsed_solves = self.parse_user_solves(raw_solves)
        return parsed_solves

    def get_user_info(self, user: str) -> dict[str, str | list[dict] | None]:
        return {"username": user, "solves": self.fetch_challanges(user)}
