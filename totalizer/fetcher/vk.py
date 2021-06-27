# Todo: import libraries for working in vk like
#  async aiovk, Vkwave, Vkbottle
import logging
from datetime import datetime
from typing import Dict, List

import vk_api

logging.basicConfig(level=logging.DEBUG)


class Wall:
    """A class for getting information from VK wall.

    Attributes:
        owner_id: id of wall. If owner of wall is group,
            type sign "-" before id.
    """

    def __init__(self, owner_id: int):
        # Todo: check if owner is user or group
        self.owner_id = owner_id
        self._posts = None

    def update(self, login: str, password: str, stop_filter=None):
        """Connect to VK and fetch info.

        Args:
            login: login of user to vk.
            stop_filter: function for stopping fetching, according
                https://vk-api.readthedocs.io/en/latest/vk_api.html.
        """
        vk_session = vk_api.VkApi(login, password)

        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            logging.error(error_msg)
            return

        tools = vk_api.VkTools(vk_session)
        # Todo: use get_all, but then could be
        #  troubles with stop function
        #  max_count should be calculated
        self._posts = tools.get_all_slow(
            method="wall.get",
            max_count=50,
            values={"owner_id": self.owner_id},
            stop_fn=stop_filter,
        )

    def get_posts_info(self) -> List[Dict]:
        """Return list of dictionaries with info from the wall.

        Return:
            A list of dict mapping keys of pasts fetched.
            For example:[{
                "date": datetime of creation,
                "id": id,
                "text": text of past,
                "likes": likes,
                "req_count": count of reposts,
                "attachs_count": count of attaches,
                "com_count": count of comments,
            }, ...].
        """
        if not self._posts:
            return [{}]

        rows = []
        for post in self._posts["items"]:
            (
                date,
                id_,
                text,
                likes,
                reposts_count,
                comments_count,
                attach_count,
                li_attachs,
            ) = (
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
                "req_count": reposts_count,
                "attachs_count": attach_count,
                "com_count": comments_count,
            }

            # Todo: read types dinamically
            types_of_attaches = {
                "link": ["url"],
                "audio": ["url"],
                "photo": ["id", "owner_id"],
                "video": ["id", "owner_id"],
                "doc": ["id", "owner_id"],
            }
            attach_props = []
            for attach in li_attachs:
                converted_attach = {
                    type_: {
                        sub_prop: attach[type_][sub_prop]
                        for sub_prop in types_of_attaches[type_]
                    }
                    for type_ in types_of_attaches
                    if type_ in attach
                }
                attach_props.append(converted_attach)

            row.update({"attach": attach_props})
            rows.append(row)
        return rows


def time_filter(date_time: datetime):
    """Stop fetching posts from vk wall.

    Args:
        date_time: time of first post for searching.
    """
    timestamp = date_time.timestamp()

    def stop(posts):
        return any([float(p["date"]) < timestamp for p in posts])

    return stop


# Now this class is not used in this project, as vk_api is used.
class Vk:
    """A class for working with data from VK social network.

    Attributes:
        token: token. Detailed instruction for
            getting token https://vk.com/dev/access_token.
    """

    # import libraries for working in vk like VK Api, Vkwave, Vkbottle
    # MAX_NUM_WALLS = 10  # For controlling server load
    def __init__(self, token: str):
        self.token = token
        self._owner_id = None
        self._walls: List[Wall] = []

    def add_wall(self, wall: Wall):
        self._walls.append(wall)
