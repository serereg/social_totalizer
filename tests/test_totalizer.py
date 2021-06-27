import json
import logging

# import pytest

from datetime import datetime
from totalizer.fetcher.vk import Wall, time_filter
from pathlib import Path

from totalizer.web.utils import form_csv


def test_getting_posts_excluding_date():
    wall = Wall(0)
    path = Path(__file__).parent / "data/club205427305.json"

    # monkeypatch
    wall_infos = json.loads(path.read_text())
    wall._posts = wall_infos["response"]

    posts = wall.get_posts_info()
    logging.warning("Parsed posts are: \n{}".format("\n ".join(map(str, posts))))
    assert len(posts) == 7
    for post in posts:
        post["date"] = ""
    assert posts[0] == {
        "date": "",
        "id": 10,
        "text": "tt.ru",
        "likes": 0,
        "req_count": 0,
        "attachs_count": 1,
        "com_count": 0,
        "attach": [{"photo": {"id": 456239316, "owner_id": 106017}}],
    }


def test_time_filter():
    dt1 = datetime(2020, 1, 1)
    dt2 = datetime(2021, 2, 2)
    dt3 = datetime(2022, 3, 3)
    assert dt1 < dt2 < dt3
    posts_1 = [{"date": dt1.timestamp()}, {"date": dt3.timestamp()}]
    func = time_filter(dt2)
    assert func(posts_1) is True

    posts_2 = [{"date": dt2.timestamp()}, {"date": dt3.timestamp()}]
    func = time_filter(dt1)
    assert func(posts_2) is False


def test_form_csv(tmp_path: Path):
    posts = [
        {
            "date": "",
            "id": 10,
            "text": "tt.ru",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 2,
            "com_count": 0,
            "attach": {"photo": {"id": 456239316, "owner_id": 106017}},
        },
        {
            "date": "",
            "id": 9,
            "text": "tt.ru",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 1,
            "com_count": 0,
            "attach": {"photo": {"id": 456239316, "owner_id": 106017}},
        },
    ]
    form_csv(path := tmp_path / "tmp.csv", ["date", "id", "attachs_count"], posts)
    posts_from_csv = path.read_text()
    assert (
        posts_from_csv
        == '''date,id,attachs_count
"""""",10,2
"""""",9,1
'''
    )
