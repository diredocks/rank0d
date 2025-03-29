from datetime import datetime


def extract_between(s: str, start: str, end: str) -> str:
    return s[s.find(start) + len(start) : s.rfind(end)]


def iso_to_timestamp(iso: str) -> str:
    return str(int(datetime.fromisoformat(iso).timestamp()))


def string_to_timestamp(time: str) -> str:
    return str(int(datetime.strptime(time, "%Y-%m-%d %H:%M:%S").timestamp()))
