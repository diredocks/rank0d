from .abstract_platform import AbstractPlatform
from bs4 import BeautifulSoup as bs


class BugKu(AbstractPlatform):
    base_url = "https://ctf.bugku.com"

    def get_user_solves(self, user: str) -> list | None:
        resp = self.session.get(f"{self.base_url}/user/info/id/{user}.html")
        soup = bs(resp.text, "lxml")
        elem = soup.select(".table tbody tr")
        return [each.find_all("td") for each in elem]

    def parse_user_solves(self, solves: list) -> list[dict]:
        return [
            {
                "challenges": solve[1].find("a").text,
                "link": self.base_url + solve[1].find("a").get("href"),
                "category": solve[2].find("span").text,
                "point": solve[3].text,
                "time": solve[5].text,
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
