from os.path import dirname
from os.path import join
from os.path import realpath
from typing import Optional


from settings import SETTINGS


TEMPLATES = None  # type: Optional[Jinja2Templates]
STREAM = None  # type: Optional[StreamProducer]


async def get_stream_producer() -> StreamProducer:
    global STREAM
    if not STREAM:
        STREAM = StreamProducer(url_redis=SETTINGS.DATABASE_URL)
        STREAM.setup()

    return STREAM


async def get_templates():
    """Retorna o gerenciador de templates."""
    global TEMPLATES
    if not TEMPLATES:
        dir_templates = join(dirname(realpath(__file__)), 'templates')
        TEMPLATES = Jinja2Templates(directory=dir_templates)

    return TEMPLATES
