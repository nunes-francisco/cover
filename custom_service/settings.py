__all__ = ['__version__', 'SOLUTION_NAME', 'URL_PREFIX', 'SETTINGS', 'TAG']

from os.path import dirname
from os.path import split
from socket import gethostname
import sys

from pydantic import Field
from pydantic import RedisDsn
from pydantic import ValidationError
from hiredis import __version__ as hiredis_version
from aioredis import __version__ as aioredis_version

from csapp import CSSettingsBase
from csapp import get_logger
from csapp import __version__ as csapp_version
from csrpc import __version__ as csrpc_version


__version__ = '0.1.1'
SOLUTION_NAME = 'CS.Custom_service-1'
URL_PREFIX = split(dirname(__file__))[1]


class _SolutionSettings(CSSettingsBase):
    """Parâmetros de execução.

    Extenda esta classe com os parâmetros de execução da aplicação.
    """
    CS_HTTP_PORT: int = Field(
            default=8080,
            env='CS_HTTP_PORT',
            description='Porta HTTP para servidão REST'
    )
    CS_CORTEX_DATABASE_URL: RedisDsn = Field(env='CS_CORTEX_DATABASE_URL',
                                             description='URL de acesso ao database CS.Cortex ( Redis )')


try:
    SETTINGS = _SolutionSettings()

    TAG = (
        f'\n\n{"-" * 100}\n'
        f'Python: {sys.version}\n'
        f'Hostname: {gethostname()}\n'
        f'Infomações do microsserviço:\n'
        f'    Solução: {SOLUTION_NAME}\n'
        f'    Versão: {__version__}\n'
        f'    Prefixo: {URL_PREFIX}\n'
        f'Parâmetros de execução:\n'
        f'    {SETTINGS}\n'
        f'Versão das bibliotecas críticas:\n'
        f'    CS.App: {csapp_version}\n'
        f'    CS.RPC: {csrpc_version}\n'
        f'    aioredis: {aioredis_version}\n'
        f'    hiredis: {hiredis_version}\n'
        f'{"-" * 100}\n'
    )

    get_logger().info(TAG)

except ValidationError as err:
    get_logger().critical(
            '🚨 Alguma variável de ambiente não foi definida. Confira na documentação. Erros: \n%s',
            err
    )
    sys.exit(1)
