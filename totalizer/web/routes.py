from totalizer.web.views import IndexView, WallView


ROUTES = (
    ("/", "*", IndexView),
    ("/wall", "*", WallView),
    ("/average", "*", WallView),
)
