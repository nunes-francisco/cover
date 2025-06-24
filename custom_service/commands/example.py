from csrpc import RPCRouter

router = RPCRouter(context_name='example')


@router.rpc_route('echo')
async def echo(phrase: str = 'Olá Mundo') -> str:
    return f'Prase: {phrase}'
