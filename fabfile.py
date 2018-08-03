import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/Ninjamannn/smart_home.git'
BRANCH = ''  # ??????
env.hosts = ['http://127.0.0.1:2222']
env.user = 'vagrant'
env.venvpyton = '/home/{user}/env/iot/bin'.format(user=env.user)
env.key_filename = '/path/to/keyfile.pem'


def deploy():
    site_folder = '/home/{user}/project/'.format(user=env.user)
    run('mkdir -p {site_folder}'.format(site_folder=site_folder))
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()


def _get_latest_source():
    if exists('.git'):
        print("-----------git fetch------------")
        run('git fetch')
    else:
        print("-----------git clone------------")
        run('git clone {REPO_URL} . -b develop'.format(REPO_URL=REPO_URL))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('git reset --hard {current_commit}'.format(current_commit=current_commit))


def _update_virtualenv():
    if not exists('{venvpyton}/pip'.format(venvpyton=env.venvpyton)):
        run('python3 -m venv /home/{user}/env/iot'.format(user=env.user))
    run('{venvpyton}/pip install -r requirements.txt'.format(venvpyton=env.venvpyton))


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', 'SITENAME={host}'.format(host=env.hosts))
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', 'DJANGO_SECRET_KEY={new_secret}'.format(new_secret=new_secret))


def _update_static_files():
    run('{venvpyton}/python manage.py collectstatic --noinput'.format(venvpyton=env.venvpyton))


def _update_database():
    run('{venvpyton}/python manage.py migrate --noinput'.format(venvpyton=env.venvpyton))
