"""Inicialização do artefato"""

from os.path import dirname
from os.path import realpath

from csapp import run_csapp

from settings import __version__
from settings import SETTINGS
from settings import SOLUTION_NAME
from settings import URL_PREFIX
from finalization import finalization
from initialization import initialization

if __name__ == '__main__':
    run_csapp(
        solution_name=SOLUTION_NAME,
        solution_version=__version__,
        http_port=SETTINGS.CS_HTTP_PORT,
        url_prefix=URL_PREFIX,
        app_dir=dirname(realpath(__file__)),
        url_cortex=SETTINGS.CS_CORTEX_DATABASE_URL,
        rpc_max_workers=50,
        eda_max_workers=50,
        start_rpc=True,
        start_eda=True,
        on_startup=[initialization],
        on_shutdown=[finalization],
    )
