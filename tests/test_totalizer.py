import json
import logging

from totalizer.fetcher.vk import Wall
from pathlib import Path


def test_getting_posts():
    wall = Wall(0)
    path = Path(__file__).parent / "data/club205427305.json"
    wall_infos = json.loads(path.read_text())
    wall._posts = wall_infos["response"]
    posts = wall.get_posts_info()
    # logging.warning("Parsed posts are:
    # \n{}".format("\n ".join(map(str, posts))))

    real_posts = [
        {
            "date": "2021-06-25T17:36:23",
            "id": 10,
            "text": "tt.ru",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 1,
            "com_count": 0,
            "attach": {"photo": {"id": 456239316, "owner_id": 106017}},
        },
        {
            "date": "2021-06-25T16:57:34",
            "id": 9,
            "text": "6 https://www.booking.com/",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 1,
            "com_count": 0,
            "attach": {"link": {"url": "http://www.booking.com/"}},
        },
        {
            "date": "2021-06-24T16:43:45",
            "id": 5,
            "text": "5",
            "likes": 2,
            "req_count": 1,
            "attachs_count": 0,
            "com_count": 0,
            "attach": {},
        },
        {
            "date": "2021-06-24T16:41:22",
            "id": 4,
            "text": "4",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 0,
            "com_count": 0,
            "attach": {},
        },
        {
            "date": "2021-06-24T16:41:19",
            "id": 3,
            "text": "3",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 0,
            "com_count": 2,
            "attach": {},
        },
        {
            "date": "2021-06-24T16:40:37",
            "id": 2,
            "text": "2",
            "likes": 1,
            "req_count": 0,
            "attachs_count": 0,
            "com_count": 1,
            "attach": {},
        },
        {
            "date": "2021-06-24T16:40:32",
            "id": 1,
            "text": "1",
            "likes": 0,
            "req_count": 0,
            "attachs_count": 0,
            "com_count": 0,
            "attach": {},
        },
    ]
    for post in posts:
        logging.debug(post)
        assert post in real_posts
