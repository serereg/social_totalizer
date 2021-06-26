from totalizer.web.views import AnalysisView, IndexView, WallView


ROUTES = (
    ("/", "*", IndexView),
    ("/wall", "*", WallView),
    ("/analysis", "*", AnalysisView),
)
