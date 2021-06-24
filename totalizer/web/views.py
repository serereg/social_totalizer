# import asyncio
# import logging
# import time

from aiohttp import web


class IndexView(web.View):
    @staticmethod
    async def get():
        return web.FileResponse("totalizer/static/index.html")


class HTTPView(web.View):
    async def get(self):
        print("httpview get")
        print(self.request.rel_url.query)


class WallView(HTTPView):
    async def get(self):
        print("httpview get")
        print(self.request.rel_url.query)
        wall_id = self.request.rel_url.query["wall_id"]
        vk = self.request.app["vk"]
        return web.Response(text=f"{wall_id=}, {vk.token=}")
