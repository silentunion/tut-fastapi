import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template(template_file='home/index.pt')
def index(user: str = 'anon'):
    return {
        'package_count': 315_000,
        'release_count': 2_343_124,
        'user_count': 73_234,
        'packages': [
            {'id': 'skynet', 'summary': "Totally not going to take over the world"},
            {'id': 'dot_nukem', 'summary': "The safest malware"},
            {'id': 'hello_world', 'summary': "World never says hello back"}
        ]
    }


@router.get('/about')
@template()
def about():
    return {}