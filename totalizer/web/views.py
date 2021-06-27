import logging
from datetime import datetime
from pathlib import Path

from aiohttp import web

from ..fetcher.vk import Wall, time_filter
from .utils import form_csv

logging.basicConfig(level=logging.DEBUG)


class IndexView(web.View):
    @staticmethod
    async def get():
        return web.FileResponse("totalizer/static/index.html")


class HTTPView(web.View):
    async def get(self):
        logging.debug("httpview get")
        logging.debug(self.request.rel_url.query)

    # async def post(self):
    #     logging.debug(self.request)


class WallView(web.View):
    async def get(self):
        logging.debug("wallview get")
        logging.debug(self.request.rel_url.query)

        wall_id = self.request.rel_url.query["wall_id"]
        login = self.request.rel_url.query["login"]
        password = self.request.rel_url.query["password"]
        dt_stopping_search = datetime.strptime(
            self.request.rel_url.query["date_time"], "%d-%m-%Y"
        )

        # vk = self.request.app["vk"]
        logging.debug("Attempt to authorize in VK")
        wall = Wall(owner_id=int(wall_id))
        logging.debug("Authorization is done")
        # vk.add_wall(wall)

        logging.debug("Attempt to fetch posts")
        wall.update(login, password, stop_filter=time_filter(dt_stopping_search))
        logging.debug("Posts fetched")

        logging.debug("Extraction information from posts")
        posts_info = wall.get_posts_info()
        # Todo: use web.StreamResponse for transferring

        # Todo: Generate temporary file
        temp_file_to_transfer = Path(__file__).parent / "data/tmp.csv"

        columns = [
            "date",
            "id",
            "likes",
            "req_count",
            "attach_count",
            "com_count",
            "attach",
        ]
        logging.debug("Forming a csv file")
        form_csv(temp_file_to_transfer, columns, posts_info)

        # Todo: need to delete the unused file
        logging.debug("Sending the csv file")
        return web.FileResponse(temp_file_to_transfer)


class AnalysisView(web.View):
    async def get(self):
        logging.debug("analysisview get")
        logging.debug(self.request.rel_url.query)

        logging.debug("Sending the jupyter file")
        return web.FileResponse("totalizer/static/data/VK_Analysis.ipynb")
