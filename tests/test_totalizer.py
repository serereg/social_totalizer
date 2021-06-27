import json
import logging

from totalizer.fetcher.vk import Wall
from pathlib import Path


def test_etting_posts():
    wall = Wall(0)
    path = Path(__file__).parent / "data/club205427305.json"
    wall_infos = json.loads(path.read_text())
    wall._posts = wall_infos["response"]
    posts = wall.get_posts_info()
    logging.warning("Parsed posts are: \n{}".format("\n ".join(map(str, posts))))
    assert len(posts) == 7
    assert posts[0] == {
        "date": "2021-06-25T17:36:23",
        "id": 10,
        "text": "tt.ru",
        "likes": 0,
        "req_count": 0,
        "attachs_count": 1,
        "com_count": 0,
        "attach": {"photo": {"id": 456239316, "owner_id": 106017}},
    }
