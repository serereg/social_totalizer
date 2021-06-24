# import asyncio
# import logging

from aiohttp import web


class IndexView(web.View):
    @staticmethod
    async def get():
        return web.FileResponse("totalizer/static/index.html")


class HTTPView(web.View):
    async def get(self):
        print("httpview get")
        pass

    async def post(self):
        return web.json_response(
            await self.handle(
                await self.request.text(),
                self.request.headers,
            )
        )
