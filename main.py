from aiohttp import web
import asyncio
import logging

from web.routes import ROUTES

# from config import CONFIG


def db_connect(dsn, db):
    pass
    # client = DBClient(dsn=dsn, db=db)
    # client.connect()
    # client.add_fixtures(FIXTURES)
    # return client


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    app = web.Application()

    loop = asyncio.get_event_loop()
    # db_client = db_connect("sqlite:///db/db.sqlite3", Base)
    # app["database"] = db_client

    for path, method, view in ROUTES:
        app.router.add_route(method, path, view)
    app.router.add_static("/", "static")

    web.run_app(app, port=80)


def foo():
    """Return True."""
    return True
