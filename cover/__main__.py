
from os.path import dirname
from os.path import realpath


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
        http_port=SETTINGS.HTTP_PORT,
        url_prefix=URL_PREFIX,
        app_dir=dirname(realpath(__file__)),
        url_cortex=SETTINGS.DATABASE_URL,
        start_rpc=True,
        start_eda=True,
        on_startup=[initialization],
        on_shutdown=[finalization],
    )
