# Todo: import libraries for working in vk like
#  VK Api, ar async Vkwave, Vkbottle
from typing import List


class Wall:
    def __init__(self, owner_id: int):
        # Todo: check if owner is user or group
        self.owner_id = owner_id
        self.posts = None

    @staticmethod
    def get_posts_info(params=None):
        # Todo: check parameters for wall
        if params is None:
            params = {}

        # Temp testing data
        row = {"id": 1, "text": "", "apps": 0, "likes": 0, "reposts": 0, "comments": 0}
        table = [row, row, row]

        return table


class Vk:
    # import libraries for working in vk like VK Api, Vkwave, Vkbottle
    # MAX_NUM_WALLS = 10  # For controlling load
    def __init__(self, token: str):
        self.token = token
        self.owner_id = None
        self.walls: List[Wall] = []

    def add_wall(self, wall: Wall):
        self.walls.append(wall)
