# import asyncio
# import logging
# import time

import csv

from aiohttp import web
from pathlib import Path

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

        vk = self.request.app["vk"]
        wall = Wall(owner_id=int(wall_id))
        vk.add_wall(wall)

        wall_info = wall.get_posts_info()
        # Todo: use web.StreamResponse
        #  https://gist.github.com/
        #  igorzakhar/35c04d4052be3749145d9bdb89962502
        #  or tempfile
        temp_file_to_transfer = Path(__file__).parent / "tmp.csv"
        with temp_file_to_transfer.open(mode="w", newline="") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=";", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            for item in wall_info:
                row = [v[1] for v in item.items()]
                writer.writerow(row)
        # Todo: need to clear folder
        return web.FileResponse(temp_file_to_transfer)
