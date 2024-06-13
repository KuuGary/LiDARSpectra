import requests
import numpy as np
import pandas as pd
import time
from rich import print
from rich.progress import track
import orjson

headers = {
    "Content-Type":
    "application/json; charset=utf-8",
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def find_start_end():
    session = requests.Session()
    session.get("https://lspdd.org/")
    start = 0
    end = 0
    for i in track(range(2400, 2500)):
        data = session.get(
            f"https://lspdd.org/app/en/lamps/{i}.json?showdata=true",
            headers=headers)
        if data.status_code == 200:
            start = i
            break
    for i in track(range(2800, 2900)):
        data = session.get(
            f"https://lspdd.org/app/en/lamps/{i}.json?showdata=true",
            headers=headers)
        if start != 0 and data.status_code != 200:
            end = i
            break
    return (start, end)


def get_data(start, end):
    session = requests.Session()
    session.get("https://lspdd.org/")
    db = {}
    for i in track(range(start, end)):
        try:
            data = session.get(
                f"https://lspdd.org/app/en/lamps/{i}.json?showdata=true",
                headers=headers)
            data = orjson.loads(data.content)
            db[data['id']] = data
        except:
            print(f"Error at {i}")
            print(data)
    return db


if __name__ == "__main__":
    # start,end = find_start_end()
    ## 2469-2803 is the range of lamps, some are missing, 311 in total
    db = get_data(2469, 2803)
    with open("db.json", "w") as f:
        f.write(
            orjson.dumps(db, option=orjson.OPT_NON_STR_KEYS).decode("utf-8"))
