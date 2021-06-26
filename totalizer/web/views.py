# import asyncio
# import time

import csv
import json
import logging

from aiohttp import web

from datetime import datetime
from pathlib import Path
from typing import Dict, List

from ..fetcher.vk import Wall, time_filter


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

        dt_stopping_search_str = self.request.rel_url.query["date_time"]
        dt_stopping_search = datetime.strptime(dt_stopping_search_str, "%d-%m-%Y")
        logging.warning(dt_stopping_search)

        vk = self.request.app["vk"]
        # time_to_stop = datetime(2021, 6, 25)

        wall = Wall(owner_id=int(wall_id))
        vk.add_wall(wall)

        wall.update(login, password, stop_filter=time_filter(dt_stopping_search))
        logging.warning("Wall updated")

        posts_info = wall.get_posts_info()
        # Todo: use web.StreamResponse for transferring

        temp_file_to_transfer = Path(__file__).parent / "tmp.csv"

        columns = [
            "date",
            "id",
            "likes",
            "req_count",
            "attach_count",
            "com_count",
            "attach",
        ]
        form_csv(temp_file_to_transfer, columns, posts_info)

        # Todo: need to clear folder
        return web.FileResponse(temp_file_to_transfer)


class AnalysisView(HTTPView):
    async def get(self):
        return web.FileResponse("totalizer/static/data/VK_Analysis" ".ipynb")


def form_csv(file: Path, columns: List[str], rows: List[Dict]):
    with open(file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v) for k, v in row.items() if k in columns})
