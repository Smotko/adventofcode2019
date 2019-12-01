import requests
import percache
import os

cache = percache.Cache(".cache")


@cache
def get_input(day):
    print("Fetching from server")
    result = requests.get(
        f"https://adventofcode.com/2019/day/{day}/input",
        cookies={"session": os.getenv("AOC_SESSION")},
    )
    return result.text.splitlines()


def get_int_input(day):
    res = get_input(day)
    return [int(r) for r in res]
