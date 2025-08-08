__all__ = ['__version__', 'SOLUTION_NAME', 'URL_PREFIX', 'SETTINGS', 'INFO']

from os.path import dirname
from os.path import split
from socket import gethostname
import sys
from logging import getLogger

from pydantic import Field
from pydantic import RedisDsn
from pydantic import ValidationError
from pydantic import BaseSettings

from hiredis import __version__ as hiredis_version
from aioredis import __version__ as aioredis_version


__version__ = '0.1.0'
SOLUTION_NAME = 'COVER'
URL_PREFIX = split(dirname(__file__))[1]


class Settings(BaseSettings):
    """Parâmetros de execução.

    Extenda esta classe com os parâmetros de execução da aplicação.
    """
    HTTP_PORT: int = Field(
            default=8080,
            env='HTTP_PORT',
            description='Porta HTTP para servidão REST'
    )
    DATABASE_URL: RedisDsn = Field(env='DATABASE_URL', description='URL de acesso ao database Redis')


try:
    SETTINGS = Settings()

    INFO = (
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
        f'    aioredis: {aioredis_version}\n'
        f'    hiredis: {hiredis_version}\n'
        f'{"-" * 100}\n'
    )

    getLogger().info(INFO)

except ValidationError as err:
    # :TODO: Melhorar a mensagem de erro
    #       para incluir o nome da variável que não foi definida.
    #       Exemplo: HTTP_PORT não foi definido.
    #       Exemplo: DATABASE_URL não foi definido.
    getLogger().critical(
            '🚨 Alguma variável de ambiente não foi definida. Confira na documentação. Erros: \n%s',
            err
    )
    sys.exit(1)
