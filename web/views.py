# import asyncio
# import logging

from aiohttp import web


class IndexView(web.View):
    @staticmethod
    async def get():
        return web.FileResponse("static/index.html")
