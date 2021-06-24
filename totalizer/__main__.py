from aiohttp import web

# import asyncio
# import logging

from .web.routes import ROUTES

from .config import CONFIG
from .fetcher.vk import Vk


def main():
    # logger = logging.getLogger(__name__)

    # Todo: get several tokens, or generate its.
    print(CONFIG)
    vk = Vk(token=CONFIG["vk"]["token"])

    app = web.Application()

    app["vk"]: Vk = vk

    # loop = asyncio.get_event_loop()

    for path, method, view in ROUTES:
        app.router.add_route(method, path, view)
    app.router.add_static("/", "totalizer/static")

    web.run_app(app, port=80)


if __name__ == "__main__":
    main()


def foo():
    """Return True."""
    return True
