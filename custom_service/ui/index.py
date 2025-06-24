from typing import Dict, List, Tuple

from csapp import AuthChecker
from csapp import CSUserSession
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from settings import __version__
from settings import SOLUTION_NAME
from dependencies import get_rpc_client
from dependencies import get_templates

router = APIRouter(include_in_schema=False)

INDEX = {}  # type: Dict[str, List[Tuple[str, str]]]


@router.get('/', response_class=HTMLResponse)
async def get_index(
        request: Request,
        templates: Jinja2Templates = Depends(get_templates),
        csuser: CSUserSession = Depends(
            AuthChecker(
                rpc_client_function=get_rpc_client,
                companies='__prime__',
                minimal_role='PRIME',
                scope=None,
                auto_error=False
            )
        )
):
    context = {
        'request': request,
        'SOLUTION_NAME': SOLUTION_NAME,
        '__version__': __version__,
        'INDEX': INDEX if csuser else {},
    }

    template = 'index.html' if csuser else 'assets/401.html'

    result = templates.TemplateResponse(template, context)

    return result
