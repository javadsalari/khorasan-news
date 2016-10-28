from Handlers import index
from Handlers.body import BodyHandler
urlList = [
    (r'/', index.IndexHandler,None),
    (r'/news/(.+)', BodyHandler,None)


]
