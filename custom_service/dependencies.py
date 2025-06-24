from os.path import dirname
from os.path import join
from os.path import realpath
from typing import Optional

from csrpc import RPCClient
from csrpc import StreamProducer
from fastapi.templating import Jinja2Templates

from settings import SETTINGS

_RPC_CLIENT = None  # type: Optional[RPCClient]
_TEMPLATES = None  # type: Optional[Jinja2Templates]
_STREAM_PRODUCER = None  # type: Optional[StreamProducer]


async def get_rpc_client() -> RPCClient:
    global _RPC_CLIENT
    if not _RPC_CLIENT:
        _RPC_CLIENT = RPCClient(SETTINGS.CS_CORTEX_DATABASE_URL)
        _RPC_CLIENT.setup()

    return _RPC_CLIENT


async def get_stream_producer() -> StreamProducer:
    global _STREAM_PRODUCER
    if not _STREAM_PRODUCER:
        _STREAM_PRODUCER = StreamProducer(url_redis=SETTINGS.CS_CORTEX_DATABASE_URL)
        _STREAM_PRODUCER.setup()

    return _STREAM_PRODUCER


async def get_templates():
    """Retorna o gerenciador de templates."""
    global _TEMPLATES
    if not _TEMPLATES:
        dir_templates = join(dirname(realpath(__file__)), 'templates')
        _TEMPLATES = Jinja2Templates(directory=dir_templates)

    return _TEMPLATES
