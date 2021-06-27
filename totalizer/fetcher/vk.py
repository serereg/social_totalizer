# Todo: import libraries for working in vk like
#  async aiovk, Vkwave, Vkbottle
import logging
from datetime import datetime
from typing import List

import vk_api

logging.basicConfig(level=logging.DEBUG)


class Wall:
    def __init__(self, owner_id: int):
        # Todo: check if owner is user or group
        self.owner_id = owner_id
        self.posts = None

    def update(self, login: str, password: str, stop_filter=None):
        vk_session = vk_api.VkApi(login, password)

        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            logging.error(error_msg)
            return

        tools = vk_api.VkTools(vk_session)
        self.posts = tools.get_all(
            method="wall.get",
            max_count=50,
            values={"owner_id": self.owner_id},
            stop_fn=stop_filter,
        )

    def get_posts_info(self):
        rows = []
        for post in self.posts["items"]:
            date, id_, text, likes, req_count, attach_count, com_count, li_attachs = (
                post["date"],
                post["id"],
                post["text"],
                post["likes"]["count"],
                post["reposts"]["count"],
                post["comments"]["count"],
                len(post.get("attachments", [])),
                post.get("attachments", []),
            )
            row = {
                "date": datetime.fromtimestamp(date).isoformat(),
                "id": id_,
                "text": text,
                "likes": likes,
                "req_count": req_count,
                "attachs_count": attach_count,
                "com_count": com_count,
            }

            types = {"link": ["url"], "audio": ["url"], "photo": ["id", "owner_id"]}
            attach_props = {}
            for attach in li_attachs:
                prop = {
                    type_: {
                        sub_prop: attach[type_][sub_prop] for sub_prop in types[type_]
                    }
                    for type_ in types
                    if type_ in attach
                }
                attach_props.update(prop)
            row.update({"attach": attach_props})
            rows.append(row)
        return rows


def time_filter(date_time: datetime):
    timestamp = date_time.timestamp()

    def stop(posts):
        return any([float(p["date"]) < timestamp for p in posts])

    return stop


class Vk:
    # import libraries for working in vk like VK Api, Vkwave, Vkbottle
    # MAX_NUM_WALLS = 10  # For controlling load
    def __init__(self, token: str):
        self.token = token
        self.owner_id = None
        self.walls: List[Wall] = []

    def add_wall(self, wall: Wall):
        self.walls.append(wall)
