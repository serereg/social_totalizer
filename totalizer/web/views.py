# import asyncio
# import logging
# import time

import csv
import json

from aiohttp import web

# from datetime import datetime
from pathlib import Path
from typing import Dict, List

from ..fetcher.vk import Wall


class IndexView(web.View):
    @staticmethod
    async def get():
        return web.FileResponse("totalizer/static/index.html")


class HTTPView(web.View):
    async def get(self):
        print("httpview get")
        print(self.request.rel_url.query)

    async def post(self):
        print(self.request)


class WallView(HTTPView):
    async def get(self):
        print("httpview get")
        print(self.request.rel_url.query)
        wall_id = self.request.rel_url.query["wall_id"]
        login = self.request.rel_url.query["login"]
        password = self.request.rel_url.query["password"]

        vk = self.request.app["vk"]
        # time_to_stop = datetime(2021, 6, 25)

        wall = Wall(owner_id=int(wall_id))
        vk.add_wall(wall)

        wall.update(login, password, stop_filter=None)
        print("updated")
        posts_info = wall.get_posts_info()
        # Todo: use web.StreamResponse for transferring

        temp_file_to_transfer = Path(__file__).parent / "tmp.csv"

        columns = ["id", "likes", "req_count", "attach_count", "com_count", "attach"]
        form_csv(temp_file_to_transfer, columns, posts_info)

        # Todo: need to clear folder
        return web.FileResponse(temp_file_to_transfer)


def form_csv(file: Path, columns: List[str], rows: List[Dict]):
    with open(file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v) for k, v in row.items() if k in columns})
