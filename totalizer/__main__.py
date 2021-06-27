import logging

from aiohttp import web

from .config import CONFIG

# from .fetcher.vk import Vk
from .web.routes import ROUTES

logging.basicConfig(level=logging.DEBUG)


def main():
    logging.debug(f"{CONFIG=}")

    # Todo: get several tokens, or generate its.
    # vk = Vk(token=CONFIG["vk"]["token"])

    app = web.Application()

    # app["vk"]: Vk = vk

    for path, method, view in ROUTES:
        app.router.add_route(method, path, view)
    app.router.add_static("/", "totalizer/static")

    web.run_app(app, port=CONFIG["server"]["port"])


if __name__ == "__main__":
    main()
