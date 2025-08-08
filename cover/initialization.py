"""Inicialização de todas as tarefas auxiliares presentes neste artefato."""

__all__ = ['initialization']

from logging import getLogger
from settings import INFO


async def initialization():
    getLogger().info(INFO)
