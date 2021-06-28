import io
import logging
from datetime import datetime

from aiohttp import web

from ..fetcher.vk import Wall, time_filter
from .utils import form_csv

logging.basicConfig(level=logging.DEBUG)


class IndexView(web.View):
    @staticmethod
    async def get():
        return web.FileResponse("totalizer/static/index.html")


class WallView(web.View):
    """A class for extracting and sending information from a VK wall."""

    async def get(self):
        """Send .csv file with info from the wall.

        From given information (wall id, login, password and time for
            stopping extracting posts from the wall) form csv file.
            Now there is a nowing issue with working just with one file
            tmp.csv."""
        logging.debug("wallview get")
        logging.debug(self.request.rel_url.query)

        wall_id = self.request.rel_url.query["wall_id"]
        login = self.request.rel_url.query["login"]
        password = self.request.rel_url.query["password"]
        try:
            dt_stopping_search = datetime.strptime(
                self.request.rel_url.query["date_time"], "%d-%m-%Y"
            )
        except ValueError:
            dt_stopping_search = datetime.now()

        # vk = self.request.app["vk"]
        wall = Wall(owner_id=int(wall_id))
        # vk.add_wall(wall)

        logging.debug("Attempt to authorize in VK and fetch posts")
        wall.update(login, password, stop_filter=time_filter(dt_stopping_search))
        logging.debug("Posts fetched")

        logging.debug("Extraction information from posts")
        posts_info = wall.get_posts_info()
        # Todo: use web.StreamResponse for transferring

        io_to_transfer = io.StringIO()
        columns = [
            "date",
            "id",
            "likes",
            "req_count",
            "attachs_count",
            "com_count",
            "attach",
        ]
        logging.debug("Forming a csv file")
        form_csv(io_to_transfer, columns, posts_info)

        logging.debug("Sending the csv file")
        return web.Response(content_type="text/csv", text=io_to_transfer.getvalue())


class AnalysisView(web.View):
    """A class for sending statistic info."""

    async def get(self):
        logging.debug("analysisview get")
        logging.debug(self.request.rel_url.query)

        logging.debug("Sending the jupyter file")
        return web.FileResponse("totalizer/static/data/VK_Analysis.ipynb")
