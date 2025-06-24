"""Inicialização de todas as tarefas auxiliares presentes neste artefato."""

__all__ = ['initialization']

from csapp import get_logger

from settings import TAG


async def initialization():
    get_logger().info(TAG)
